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
	#print(output)
	# for m in output:
	# 	m = list(m)
	# 	print(m)

	for i,l in zip(output,range(len(output))):
		if l & 1:
			i = list(i)
			i.reverse()
			full.append(i)
		else:
			i = list(i)
			full.append(i)
	print(full)
		
#create_zigzag(3, 5)

### Bingo bango bongo, I don't want to leave the Python ###
def contains_bingo(card, numbers, centerfree = False):
	cf = centerfree
	cfn = card[2][2]
	checklist = [
	[card[0][0], card[1][1], cfn, card[3][3], card[4][4]],
	(card[4][0], card[3][1], cfn, card[1][3], card[0][4]),
	(card[0][0], card[0][1], card[0][2], card[0][3], card[0][4]),
	(card[1][0], card[1][1], card[1][2], card[1][3], card[1][4]),
	(card[2][0], card[2][1], cfn, card[2][3], card[2][4]),
	(card[3][0], card[3][1], card[3][2], card[3][3], card[3][4]),
	(card[4][0], card[4][1], card[4][2], card[4][3], card[4][4]),
	(card[0][0], card[1][0], card[2][0], card[3][0], card[4][0]),
	(card[0][1], card[1][1], card[2][1], card[3][1], card[4][1]),
	(card[0][2], card[1][2], cfn, card[3][2], card[4][2]),
	(card[0][3], card[1][3], card[2][3], card[3][3], card[4][3]),
	(card[0][4], card[1][4], card[2][4], card[3][4], card[4][4])
	]
	for line,tag in zip(checklist,range(len(checklist))):
		sumsum = 0
		for num in line:
			if num in numbers:
				num = 0
				sumsum+=num
			elif num == cfn and cf == True:
				num = 0
				sumsum+=num
			# elif num == cfn and cf == False:
			# 	num = 1
			# 	sumsum+=num
			else:
				num = 1
				sumsum+=num
		if sumsum == 0:
			result = "True"
			break
		elif sumsum > 0:
			result = "False"
			continue

	# print(result)
	# print("Winning line is:",checklist[tag])
	

contains_bingo([
[89, 23, 61, 94, 67], 
[19, 85, 90, 70, 32], 
[36, 98, 57, 82, 20], 
[76, 46, 25, 29, 7], 
[55, 14, 53, 37, 44]
],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 31, 33, 
35, 36, 37, 38, 39, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 
65, 68, 70, 71, 73, 75, 76, 77, 79, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 94, 98])


### Group equal consecutive elements into sublists ###
result = []
def group_equal(items):
	new = []
	for i,n in zip(items,range(len(items))):
		if new == []:
			if items[-1] == i:    
				if i == items[(n-1)]:
					new.insert(len(new),i)
				elif i!= items[(n-1)]:
					result.insert(len(result),new)
					new = []
					new.insert(len(new),i)
			else:
				new.insert(len(new),i)
		elif new != []:
			if i == items[(n-1)]:
				new.insert(len(new),i)
			elif i!= items[(n-1)]:
				result.insert(len(result),new)
				new = []
				new.insert(len(new),i)
	result.insert(len(result),new)
	print(result)

#group_equal([1, 1, 4, 4, 4, "hello", "hello", 4])

### Recamán's sequence ############################################################################
#http://mathworld.wolfram.com/RecamansSequence.html
#def recaman(n):



### Running median of three ###
import statistics as st

def running_median_of_three(items):
	new = []
	for i,n in zip(items,range(len(items))):
		if i == items[0]:
			new.insert(len(new),i)
		elif i == items[1]:
			new.insert(len(new),i)
		else:
			med = st.median([items[(n-2)], items[(n-1)], items[(n)]])
			new.insert(len(new),med)
	print(new)

#running_median_of_three([5, 2, 9, 1, 7, 4, 6, 3, 8])

### Deteb ###
def detab(string, n = 5, sound = "+"):
    result = ""
    pos = 0
    yes = (string[(n-1)::n])
    for char,num in zip(string,range(len(string))):
        if char == "\t":
            if string[(num+1)] in yes:
                char = ""
            else:
                char = sound * (n - pos % n)
                pos = 0
        else:
            pos += 1
        result += char
    print("\""+result+"\"")

#detab("Hello\tthereyou\tworld")
#detab("Ilkka\tMarkus\tKokkarinen")
#detab("Tenser,\tsaid\tthe\ttensor")


### Reverse every ascending sublist ###
def reverse_ascending_sublists(items):
    newlist = []
    cool = []
    for i,n in zip(items,range(len(items))):
        if n == 0:
            cool.insert(len(items),i)
        elif i > items[(n-1)]:
            cool.insert(len(items),i)
        elif i <= items[(n-1)]:
            cool.reverse()
            for x in cool:
                newlist.append(x)
            cool = []
            cool.insert(len(items),i)
    cool.reverse()
    for x in cool:
        newlist.append(x)
    print(newlist)

#reverse_ascending_sublists([1, 2, 3, 4, 5])
#reverse_ascending_sublists([5, 7, 10, 4, 2, 7, 8, 1, 3])
#reverse_ascending_sublists([5, 4, 3, 2, 1])
#reverse_ascending_sublists([1, 2, 2, 3])

### The hand that's hard to get ###

def hand_is_badugi(hand):
	new_stuff = []
	bad_stuff = []
	for card in hand:
		for x in card:
			if x not in new_stuff:
				new_stuff.append(x)
			elif x in new_stuff:
				bad_stuff.append(x)
	if len(bad_stuff) == 0:
		print("True")
	else:
		print("False")

new = [("queen", "hearts"), ("six", "diamonds"), ("deuce", "spades"), ("jack","clubs")]
new1 = [("queen", "hearts"), ("six", "diamonds"), ("deuce", "spades"), ("queen","clubs")]
#hand_is_badugi(new)


### Brangelina ###

def brangelina(first, second):
	combined = ""
	vowel = ["a", "e", "i", "o", "u"]
	for x in first:
		if x not in vowel:
			combined += x
		elif x in vowel:
			break
	for y,z in zip(second,range(len(second))):
		if y in vowel:
			combined += second[z:]
			break
	print(combined)

#brangelina("brad", "angelina")
#brangelina("sheldon", "amy")
#brangelina("rachada", "andrew")


### Fulcrum ###

import operator


def can_balance(items):
	number = int(len(items)/2)
	front = items[:number]
	inverse = (number - number - number)
	back = items[inverse:]
	print(front)
	print(permutations(items, r=None))
	# sum_front = 0
	# sum_back = 0
	# for x in front:
	# 	sum_front += x
	# for y in back:
	# 	sum_back += y
	
	# if sum_back > sum_front:
	# 	print(sum_back-sum_front)
	
	# print(sum_front)
	# print(sum_back)

	


#can_balance([6,1,10,5,4])



### Sort integers by their digit counts ###

def sort_by_digit_count(items):
	thing = []
	for x in items:
		x = str(x)
		if "9" in x:
			thing.append(x)
	print(thing)
	thing.sort()

sort_by_digit_count([98, 19, 4321, 9999, 73, 241, 111111, 563, 33])


