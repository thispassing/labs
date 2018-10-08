### these are lab tests, instuctions can be found at https://docs.google.com/document/d/1IbbZOHwH4gjZ70XtP_rH6QhX3BeDd1ANxj1DYaFUPXk/edit#heading=h.edyunj7uqfvj


### Ryerson letter grade ###
def ryerson_letter_grade(pct):
    if pct < 50:
        return 'F'
    elif 50 <= pct <=52:
        return 'D-'
    elif 53 <= pct <=56:
        return 'D'
    elif 57 <= pct <=59:
        return 'D+'
    elif 60 <= pct <=62:
        return 'C-'
    elif 63 <= pct <=66:
        return 'C'
    elif 67 <= pct <=69:
        return 'C+'
    elif 70 <= pct <=72:
        return 'B-'
    elif 73 <= pct <=76:
        return 'B'
    elif 77 <= pct <=79:
        return 'B+'
    elif 80 <= pct <=84:
        return 'A-'
    elif 85 <= pct <=89:
        return 'A'
    elif 90 <= pct <=120:
        return 'A+'
    else:
        return "This isn't a valid grade, or you cheated!"

#grade = int(input("enter grade: "))
#print(ryerson_letter_grade(grade))


### Ascending list ###
def is_ascending(items):
    this = True
    for i in range(len(items)):
        if i==0:
            continue
        elif items[i] <= items[i-1]:
            this = False
            break
        elif items[i] >= items[i-1]:
            continue
    if this:
        print("True")
    else:
        print("False")

#is_ascending([5,91,90,773,3454])


### Keep doubling ###
zero = '0'
one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9'
arr = [zero, one, two, three, four, five, six, seven, eight, nine]


def double_until_all_digits(n, giveup = 1000):
    attempts = 0
    while attempts != giveup:
        if all(x in str(n) for x in arr) == True:
            break
        n=n*2
        attempts = attempts + 1
    if attempts == giveup:
        print("-1")
    else:
        print(attempts)

#double_until_all_digits(1)  # answer should be 68


### cPS LOCK ###
from pynput.keyboard import Key, Controller
from win32api import GetKeyState 
from win32con import VK_CAPITAL 

keyboard = Controller()
this = 'bcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ '

def caps_lock_stuck(text):
    if GetKeyState(VK_CAPITAL) == 1:
        keyboard.press(Key.caps_lock)
    for i in text:
        if i in this:
            keyboard.type(i)
        else:
            keyboard.press(Key.caps_lock)
            keyboard.release(Key.caps_lock)
     
#caps_lock_stuck("Madder than Mad Brian of Madcastle")


### Scrabble value of a word ###
_scrabble_ = {
        "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4,
        "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3,
        "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
        "y": 4, "z": 10
}

def scrabble_value(word, multipliers):
    sum = 0
    word = word.lower()
    if len(word) == len(multipliers):
        for i, t in zip(word, multipliers):
            e = int(_scrabble_[i]*t)
            sum+=e
    else:
        print("Invalid scrabble value.\nScore:")
    print(sum)

#scrabble_value("hello", [1,1,1,1,1])


### Create zigzag array ###
import numpy as np

def create_zigzag(rows, cols, start = 1):
    full = []
    digits = start + rows * cols
    
    output = np.arange(start,digits,1).reshape(rows,cols)

    for i,l in zip(output,range(len(output))):
        if l & 1:
            i = list(i)
            i.reverse()
            full.append(i)
        else:
            i = list(i)
            full.append(i)
    print(full)
        
create_zigzag(4, 2)