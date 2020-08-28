import requests
import json
import datetime
from os import path

today = datetime.datetime.now()

ymd = (str(today)).split(' ')[0]

file_name = f'./rates--{ymd}.json'

# access data
key = '825c07d7bc2238ec3c43cbe5ac7aefef'
endpoint = 'http://data.fixer.io/api/latest' + '?access_key=' + key

# check cache
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


def convert(your_money, your_val, our_val ):
    exch = your_money * our_val / your_val
    return round(exch, 3)


if data['success'] is False:
    print("CANNOT ACCESS DATA")
else:
    eur = 1.0
    mdl = data['rates']['MDL']
    usd = data['rates']['USD']
    rub = data['rates']['RUB']


def disp():
    a = " -- "
    print(f"Valuta disponibila la data de {ymd}")
    print(f"Referinta valutei la EUR dupa fixer.io")
    print("\n")
    print(f"EUR:  [{a:^12}]")
    print(f"MDL:  [{round(mdl, 4):^12}] ")
    print(f"USD:  [{round(usd, 4):^12}]")
    print(f"RUB:  [{round(rub, 4):^12}]")


def menu():
    try:
        option = -1
        while option != 0:
            print("\n")
            print("%%%%%%%%%% WELCOME TO EXCHANGE APP %%%%%%%%%%")
            print("$$$$$ MDL $$$$$ EUR $$$$ USD $$$$$ RUB $$$$$")
            print("> 1. EXCHANGE TERMINAL")
            print("> 2. Valuta disponibila")
            print("> 3. LATITUDE AND LONGITUDE OF CITY")
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
    except ValueError:
        menu()
menu()