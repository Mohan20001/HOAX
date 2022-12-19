import requests
import json
# import colorama
# from colorama import Fore
import os

# colorama.init()

def getIpDetails():
    try:
        ip_adress = input("Enter IP-Adress: ")
        data = requests.get('http://ipinfo.io/'+ ip_adress +'?token=2e4a0a4cea187d').text
        ip_data = str(data)
        json_data = json.loads(ip_data)
        f = open("ip_records.txt", "a")
        print()
        print(" IP-Addres : {}".format(json_data["ip"]))
        f.write("\n=> IP_ADRESS: {}".format(json_data["ip"]))
        print(" City      : {}".format(json_data["city"]))
        print(" Region    : {}".format(json_data["region"]))
        print(" Country   : {}".format(json_data["country"]))
        print(" Lat       : {}".format(json_data["loc"].split(",")[0]))
        print(" Long      : {}".format(json_data["loc"].split(",")[1]))
        print(" Org       : {}".format(json_data["org"]))
        print(" Postel    : {}".format(json_data["postal"]))
        print(" Timezone  : {}".format(json_data["timezone"]))
        print(' location  : https://www.google.co.in/maps/@'+json_data["loc"].split(",")[0]+','+json_data["loc"].split(",")[1]+',21z')
        f.write(', location>> https://www.google.co.in/maps/@'+json_data["loc"].split(",")[0]+','+json_data["loc"].split(",")[1]+',21z')
        tmp_cmd = 'https://www.google.co.in/maps/@'+json_data["loc"].split(",")[0]+','+json_data["loc"].split(",")[1]+',21z'
        os.system("start " + tmp_cmd)
        f.close()

    except:
        print(" ["+Fore.RED+"ERR"+Fore.WHITE+"] Invalid Ip Adress!")

def readRecord():
    f = open('ip_records.txt', 'r')
    records = f.readlines()
    for item in records:
        print(item)


def clearRecord():
    f = open('ip_records.txt', 'r+')
    f.seek(0)
    f.truncate()


# getIpDetails()
# readRecord()
# clearRecord()