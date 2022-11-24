def get_key():   
    f = open("ngrok_api_log.txt", "r")
    lines = f.read().split("\n")
    return lines[0]