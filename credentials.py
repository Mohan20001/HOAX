def find_credentials(file_path):
    print("_"*15)
    print()
    f = open(file_path, "r")

    lines = f.read().split("\n")

    for line in lines:
        if line.startswith("email"):
            print(" "+line)
        if line.startswith("pass") or line.startswith("encpass"):
            print(" "+line)

    f.close()
    print("_"*15)

def del_credential(file_path):
    f = open(file_path, "w")
    f.truncate()
    f.close()