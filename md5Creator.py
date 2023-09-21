import hashlib

def generateMD5(text: str = None):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()


while 1:
    try:
        myText = str(input("text> "))
        print(generateMD5(myText))
        print("")
    except KeyboardInterrupt:
        print("exit")
        exit()
    
