import requests
import json

def getIpDetails():
    try:
        ip_adress = input("Enter IP-Adress: ")
        data = requests.get('http://ipinfo.io/'+ ip_adress +'?token=2e4a0a4cea187d').text
        ip_data = str(data)
        json_data = json.loads(ip_data)
        f = open("ip_records.txt", "a")
        print("")
        print(" IP_ADRESS: {}".format(json_data["ip"]))
        f.write("\n IP_ADRESS: {}".format(json_data["ip"]))
        print(" CITY: {}".format(json_data["city"]))
        print(" REGION: {}".format(json_data["region"]))
        print(" COUNTRY: {}".format(json_data["country"]))
        print(" LATITUDE: {}".format(json_data["loc"].split(",")[0]))
        print(" LONGITUDE: {}".format(json_data["loc"].split(",")[1]))
        print(" ORG: {}".format(json_data["org"]))
        print(" POSTAL: {}".format(json_data["postal"]))
        print(" TIMEZONE: {}".format(json_data["timezone"]))
        print(' location>> https://www.google.co.in/maps/@'+json_data["loc"].split(",")[0]+','+json_data["loc"].split(",")[1]+',12z')
        f.write(', location>> https://www.google.co.in/maps/@'+json_data["loc"].split(",")[0]+','+json_data["loc"].split(",")[1]+',12z')
        f.close()

    except:
        print(" [ERR] Invalid Ip Adress!")

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