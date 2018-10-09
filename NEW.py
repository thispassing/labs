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
                    result.insert(len(result),new)
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
