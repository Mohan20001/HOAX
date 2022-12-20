import ip_tracer.ip_tracer as ip_trac
import pyfiglet
import hoax
import colorama
from colorama import Fore
import os
# from GetIP.manipulate_records import *
from GetIP.getip import home
os.system("cls")
colorama.init()

# print(" █████   █████    ███████      █████████   █████ █████")
# print("░░███   ░░███   ███░░░░░███   ███░░░░░███ ░░███ ░░███ ")
# print(" ░███    ░███  ███     ░░███ ░███    ░███  ░░███ ███  ")
# print(" ░███████████ ░███      ░███ ░███████████   ░░█████   ")
# print(" ░███░░░░░███ ░███      ░███ ░███░░░░░███    ███░███  ")
# print(" ░███    ░███ ░░███     ███  ░███    ░███   ███ ░░███ ")
# print(" █████   █████ ░░░███████░   █████   █████ █████ █████")
# print("░░░░░   ░░░░░    ░░░░░░░    ░░░░░   ░░░░░ ░░░░░ ░░░░░ ")
                                 
                                                      
                                                      

ascii_banner = pyfiglet.figlet_format(" HOAX!", 'smkeyboard')
print()
print(ascii_banner)
print("====================================")
print("+        developed by: mohan putta +")
print("====================================")
print()
# print("developed by: mohanputta.")
# print(" "+"*"*16 + " HOAX " + "*"*16)

# print(" ["+Fore.YELLOW+"Info"+Fore.WHITE+"] Choose the option..!")
print(" ["+Fore.CYAN+"a"+Fore.WHITE+"] IP Tracing\t\t["+Fore.CYAN+"b"+Fore.WHITE+"] Phishing")
print(" ["+Fore.CYAN+"c"+Fore.WHITE+"] Uknown-IP\t\t["+Fore.CYAN+"0"+Fore.WHITE+"] Exit")

history = "a"

def options(cmd):
    match cmd:
        case "a":
            ip_trac.main()
        case "b":
            hoax.main()
        case "c":
            home()
        case "-1":
            options(history)
        case "0":
            exit()
        

def main_home():
    while True:
        print()
        user_input = input("HOAX>> ")
        options(user_input)
        main_home()

main_home()