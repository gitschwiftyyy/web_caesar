def encrypt(string, shift):
    
    shift = int(shift)
    shift = shift % 26
    newstring = ""
    for i in range(len(string)):
        chrnumber = ord(string[i])
        chrnumber = int(chrnumber)
        if chrnumber > 64 and chrnumber < 91:
            chrnumber = chrnumber + shift
            if chrnumber > 90 and chrnumber < 97:
                chrnumber =  chrnumber % 90
                chrnumber = chrnumber + 64
        elif chrnumber > 96 and chrnumber < 123:
            chrnumber = chrnumber + shift
            if chrnumber > 122:
                chrnumber = chrnumber % 122
                chrnumber = chrnumber + 96
        newchr = chr(chrnumber)
        newstring = newstring + newchr
    
    return newstring

def main():
    string = input("Enter text: ")
    shift = input("Encryption number: ")
    print(encrypt(string, shift))
  
if __name__ == "__main__":
    main()