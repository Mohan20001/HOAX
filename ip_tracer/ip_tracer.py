import requests
import json
import colorama
from colorama import Fore
import os

colorama.init()

def getIpDetails(uip):
    try:
        ip_adress = uip.strip()
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

def run_command(cmd):
    cmd = cmd.lower()
    cmd = cmd.split()
    if len(cmd) != 0 and len(cmd) > 1:
        match cmd[0]:
            case "ip":
                getIpDetails(str(cmd[1]))
    else:
        match cmd[0]:
            case "getr":
                readRecord()
            case "remr":
                clearRecord()
            case "0":
                exit()


def readRecord():
    f = open('ip_records.txt', 'r')
    records = f.readlines()
    for item in records:
        print(item)


def clearRecord():
    f = open('ip_records.txt', 'r+')
    f.seek(0)
    f.truncate()

def main():
    while True:
        print()
        user_input = input("HOAX/IP-Tracer>> ")
        run_command(user_input)

# main()
# getIpDetails()
# readRecord()
# clearRecord()