import random
import string
def encryption(a,num):
    result = ""
    for i in range(len(a)):
        char = a[i]
        if char ==' ':
            result+= random.choice(string.ascii_letters)
        else:
            if char.isupper():
                result+= chr((ord(char) + num -65) %26 + 65)
            else:
                
            
                result += chr((ord(char) + num -97) %26 + 97)
                
    return result
def main():
    e = input()
    b = ""
    n = int(input())
    b = encryption(e,n)
    print(b)
main()
#better logic
