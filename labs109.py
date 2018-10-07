### 1

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

### 2

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

#is_ascending([0,1,2,3,4])

### 3




