import ip_tracer.ip_tracer as ip_trac
import pyfiglet
import hoax

ascii_banner = pyfiglet.figlet_format("HOAX!")
print()
print(ascii_banner)
print(" "*10 + "Coded with <3, cj.")
print(" "+"*"*16 + " HOAX " + "*"*16)

print(" [Info] Choose the option..!")
print(" [a] IP Tracing\t\t[b] Phishing")
print(" [0] Exit")

history = "a"

def options(cmd):
    match cmd:
        case "a":
            ip_trac.getIpDetails()
        case "b":
            hoax.menu()
            hoax.main()
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