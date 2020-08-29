import requests
import json
import datetime
from os import path

#input DATE



def year(y):
    ymd = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))
    ymd.strftime("%Y-%m-%d")
    ymd = str(ymd.strftime("%Y-%m-%d"))
    return ymd


def st1():
    start = datetime.datetime.strptime(year(str(input("y: ")).split()), "%Y-%m-%d")

    end = datetime.datetime.strptime(year(str(input("y: ")).split()), "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]

    for date in date_generated:
        global  file_name
        ymd = date.strftime("%Y-%m-%d")
        file_name = f'./rates--{ymd}.json'
        # access data
        key = '825c07d7bc2238ec3c43cbe5ac7aefef'
        global endpoint
        endpoint = 'http://data.fixer.io/api/' + ymd + '?access_key=' + key
        print(endpoint)
        fl_operation()
    return ymd, date_generated


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


x, date_generated = st1()
