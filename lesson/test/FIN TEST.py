import requests
import json
import datetime
from os import path

today = datetime.datetime.now()
ymd = (str(today)).split(' ')[0]


def fl_key():
    global file_name
    file_name = f'./rates--{ymd}.json'
    # access data
    key = '825c07d7bc2238ec3c43cbe5ac7aefef'
    global endpoint
    endpoint = 'http://data.fixer.io/api/' + ymd + '?access_key=' + key


fl_key()



# check cache
def fl_operation():
    global data
    if path.exists(file_name):
        file = open(file_name, 'r')
        data = json.loads(file.read())
    else:
        # get data
        response = requests.get(endpoint)
        data = json.loads(response.text)
        # save to file -> caching
        file = open(file_name, 'w')
        file.write(response.text)
        file.close()


fl_operation()


def transform_rates(original):
    transform_rates = {}
    for code1, rate1 in original.items():
        transform_rates[code1] = { "to" : {} }
        for code2, rate2 in original.items():
            transform_rates[code1]['to'][code2] = original[code2] / original[code1]
    return transform_rates


tr = transform_rates(data['rates'])

# print( tr['EUR']['to']['MDL'])
# print( tr['RUB']['to']['MDL'])
# print(200 * tr['MDL']['to']['EUR'])
# asd = tr['MDL']['to']['EUR']
# asm = tr['EUR']['to']['MDL']


def convert(your_money, your_val, our_val):
    # exch = your_money * asm
    exch = your_money * tr[your_val]['to'][our_val]

    return round(exch, 3)


def tod(val):
    global ymd
    y = str(input("y: ")).split()
    ymd = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))
    ymd.strftime("%Y-%m-%d")
    ymd = str(ymd.strftime("%Y-%m-%d"))
    fl_key()
    fl_operation()
    tg = transform_rates(data['rates'])
    asdz = tg['EUR']['to'][val]
    print(asdz)

def disp():
    a = " -- "
    print(f"Valuta disponibila la data de {ymd}")
    print(f"Referinta valutei la EUR dupa fixer.io")
    print("\n")
    print(f"EUR:  [{a:^12}]")
    print(f"MDL:  [{round(tr['EUR']['to']['MDL'], 4):^12}] ")
    print(f"USD:  [{round(tr['EUR']['to']['USD'], 4):^12}] ")
    print(f"RUB:  [{round(tr['EUR']['to']['RUB'], 4):^12}] ")



def menu():
    global ymd
    try:
        option = -1
        while option != 0:
            print("\n")
            print("%%%%%%%%%% WELCOME TO EXCHANGE APP %%%%%%%%%%")
            print("$$$$$ MDL $$$$$ EUR $$$$ USD $$$$$ RUB $$$$$")
            print("> 1. EXCHANGE TERMINAL")
            print("> 2. Valuta disponibila")
            print("> 3. introduceti valuta interesata: ")
            print("> 4. ORGANIZATION")
            print("> 5. Internet service provider IP/DOMAIN")
            print("> 0. Exit")
            print("$$$$$ MDL $$$$$ EUR $$$$ USD $$$$$ RUB $$$$$")
            print("CHOOSE OPTION > ")

            option = int(input())
            if option == 0:
                exit()
            if option == 1:
                print(convert(float(input("introduceti suma pentru schimb valutar: ")),
                              input("Introduceti valuta de care dispuneti: ").upper(),
                              input("Introduceti valuta in care va avea loc schimbul valutar: ").upper()))
            if option == 2:
                disp()
            if option == 3:
                tod(input("Introduceti valuta de care dispuneti: ").upper())
                today = datetime.datetime.now()
                ymd = (str(today)).split(' ')[0]
    except ValueError:
        menu()


menu()