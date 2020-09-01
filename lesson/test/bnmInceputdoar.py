import datetime
from os import path
import requests
import xml.etree.ElementTree as ET

# TIME
today = datetime.datetime.now()
ymd = str(today.strftime("%d.%m.%Y"))


# XML pars
def xml_pars():
    file_name = f'./rates-bnm-{ymd}.xml'
    r = requests.get(f'https://www.bnm.md/ro/official_exchange_rates?get_xml=1&date={ymd}')
    if path.exists(file_name):
        file = open(file_name, 'r')
        tree = ET.parse(file)
        root = tree.getroot()
        return root, tree, file_name
    else:
        root = ET.fromstring(r.text)
        tree = ET.ElementTree(root)
        tree.write(file_name)
        return root, tree, file_name


root, tree, file_name = xml_pars()


def valute(val):

    for Valute in root.findall('Valute'):
        rank = Valute.find('Value').text
        charCode = Valute.find('CharCode').text
        # print(root[0][3].text)
        # print(Valute.findtext('CharCode'))
        # print(Valute.findtext('Name'))
        val = f"{val}"
        if charCode == val:
            print(val, rank)
            return rank


val = valute(str(input("valuta: ")).upper())