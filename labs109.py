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

#is_ascending([0,91,90,773,3454])


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



