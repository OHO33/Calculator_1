import math
import sys
import re
from time import sleep
from colorama import Style,Fore,Back

red=Fore.RED
white=Fore.WHITE
yellow=Fore.YELLOW
yellowbg=Back.YELLOW
purple=Fore.MAGENTA
whitebg=Back.WHITE
intro="*****WELCOME*****"
for ch in intro:
    print(ch,end="")
    sys.stdout.flush()
    sleep(0.1)
print('\n')

#interface of the calculator,it doesnt work it's only for displaying
print("-------"+purple+"CALCULATOR"+white+"-------")
print("|  "+red+"7  "+white+"|"+red+"\t 8  "+white+"|"+red+"  9  "+white+"|  "+yellow+"+ "+white+"|")
print("|----------------------|")
print("|  "+red+"4  "+white+"|"+red+"\t 5  "+white+"|"+red+"  6  "+white+"|  "+yellow+"- "+white+"|")
print("|----------------------|")
print("|  "+red+"1  "+white+"|"+red+"\t 2  "+white+"|"+red+"  3  "+white+"|  "+yellow+"* "+white+"|")
print("|----------------------|")
print("|  "+red+"0  "+white+"|"+red+"\t ."+white+"  |"+red+"  "+yellowbg+red+"AC"+Style.RESET_ALL+" |  "+yellow+"/"+white+" |")
print("------------------------")
print(red+"ATTENTION: "+white+"you are only allowed to use parantheses!"+Style.RESET_ALL)
#end of the interface


check=None
exp=input('Enter your expression: ')
while True:
    try:   
        print(whitebg+red+"ANSWER of [",exp,"]:",eval(exp),Style.RESET_ALL)
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
        print("press 'C' to use the calculator again or type anything to quit!")
        check=input()
        if check=='c' or check=='C':
            exp=input('Enter your expression: ')
        else:
            print("GOOD LUCK")
            break
    except Exception as e:
        print('your expression is invalid,TRY AGAIN!')
        print('oops! ',e.__class__,' occured')
        print('type anything to "Exit" or press C to "Continue"')
        check=input()
        if check=='Q' or check=='q':
            print("GOOD LUCK")
            break
        elif check=='C' or check=='c':
            exp=input('Enter a valid expression: ')
        else:
            print("GOOD LUCK")
            break

