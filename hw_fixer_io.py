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


def convert(money_mdl):
    money_usd = money_mdl * usd / mdl
    return money_usd


if data['success'] is False:
    print("CANNOT ACCESS DATA")
else:
    eur = 1.0
    mdl = data['rates']['MDL']
    usd = data['rates']['USD']
    rub = data['rates']['RUB']
    print(convert(1_000_000))
