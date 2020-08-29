import requests
import json
import datetime
from os import path

today = datetime.datetime.now()
ymd = (str(today)).split(' ')[0]


def year_constructor(y):
    ymd = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))
    ymd.strftime("%Y-%m-%d")
    ymd = str(ymd.strftime("%Y-%m-%d"))
    return ymd


def option_4(val):
    start = datetime.datetime.strptime(year_constructor(str(input("Introduceti anul de la care incepem perioada afisarii (de ex. 2020 01 01): ")).split()), "%Y-%m-%d")

    end = datetime.datetime.strptime(year_constructor(str(input("Introduceti anul cu care se va incheia perioada afisarii (de ex. 2020 01 03): ")).split()), "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]

 #  global file_name este aici #######################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    for date in date_generated:
        global file_name
        ymd = date.strftime("%Y-%m-%d")
        file_name = f'./rates--{ymd}.json'
        # access data
        key = '825c07d7bc2238ec3c43cbe5ac7aefef'
        global endpoint
        endpoint = 'http://data.fixer.io/api/' + ymd + '?access_key=' + key
        fl_operation()
        tr4 = transform_rates(data['rates'])
        pr_tr4 = tr4['EUR']['to'][val]
        print(f'{ymd} - {pr_tr4}')
    return ymd, date_generated


 #  global file_este si aici, altfel nu lucreaza cum trebuie :DDD dar oricum nu e corect nici 2 global ?! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def fl_key():
    global file_name
    file_name = f'./rates--{ymd}.json'
    # access data
    key = '825c07d7bc2238ec3c43cbe5ac7aefef'
    global endpoint
    endpoint = 'http://data.fixer.io/api/' + ymd + '?access_key=' + key
    return ymd


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
        transform_rates[code1] = {"to": {}}
        for code2, rate2 in original.items():
            transform_rates[code1]['to'][code2] = original[code2] / original[code1]
    return transform_rates


tr = transform_rates(data['rates'])


def convert(your_money, your_val, our_val):
    # exch = your_money * asm
    exch = your_money * tr[your_val]['to'][our_val]

    return round(exch, 3)


def option_3(val):
    global ymd
    y = str(input("Introduceti anul (de ex. 2020 01 01) : ")).split()
    ymd = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))
    ymd.strftime("%Y-%m-%d")
    ymd = str(ymd.strftime("%Y-%m-%d"))
    fl_key()
    fl_operation()
    tr3 = transform_rates(data['rates'])
    pr_tr3 = tr3['EUR']['to'][val]
    print(pr_tr3)


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
            print("> 3. Rata monedei la o data anumita: ")
            print("> 4. Rata monedei la o anumita perioada")
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
                option_3(input("Introduceti denumirea monedei interesate: ").upper())
                today = datetime.datetime.now()
                ymd = (str(today)).split(' ')[0]
            if option == 4:
                option_4(input("Introduceti denumirea monedei interesate: ").upper())
    except ValueError:
        menu()


menu()
