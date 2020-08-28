import requests
import json
import datetime
from os import path

today = datetime.datetime.now()
ymd = (str(today)).split(' ')[0]

def fl_key(ymd):
    global file_name
    file_name = f'./rates--{ymd}.json'
    # access data
    key = '825c07d7bc2238ec3c43cbe5ac7aefef'
    global endpoint
    endpoint = 'http://data.fixer.io/api/' + ymd + '?access_key=' + key

fl_key(ymd)


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

def convert(your_money, your_val, our_val ):
    exch = your_money * our_val / your_val
    return round(exch, 3)

def rate():
    if data['success'] is False:
        print("CANNOT ACCESS DATA")
    else:
        global eur, mdl, usd, rub
        eur = 1.0
        mdl = data['rates']['MDL']
        usd = data['rates']['USD']
        rub = data['rates']['RUB']
rate()


def disp():
    a = " -- "
    print(f"Valuta disponibila la data de {ymd}")
    print(f"Referinta valutei la EUR dupa fixer.io")
    print("\n")
    print(f"EUR:  [{a:^12}]")
    print(f"MDL:  [{round(mdl, 4):^12}] ")
    print(f"USD:  [{round(usd, 4):^12}]")
    print(f"RUB:  [{round(rub, 4):^12}]")


def tod():
    global ymd
    y = str(input("y: ")).split()
    ymd = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))
    ymd.strftime("%Y-%m-%d")
    ymd = str(ymd.strftime("%Y-%m-%d"))
    fl_key(ymd)
    fl_operation()
    rate()
    disp()


def menu():
    global ymd
    try:
        option = -1
        while option != 0:
            fl_key(ymd)
            fl_operation()
            rate()
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
                print(convert(eval(input("introduceti suma pentru schimb valutar: ")),
                              eval(input("Introduceti valuta de care dispuneti: ").lower()),
                              eval(input("Introduceti valuta in care va avea loc schimbul valutar: ").lower())))
            if option == 2:
                disp()
            if option == 3:
                tod()
                today = datetime.datetime.now()
                ymd = (str(today)).split(' ')[0]
    except ValueError:
        menu()
menu()