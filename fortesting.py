### Group equal consecutive elements into sublists ###
result = []
def group_equal(items):
    new = []
    for i,n in zip(items,range(len(items))):
        # if it's the first item, we put put it into new []
        if n == 0:
            new.insert(len(new),i)
        # if i is not the last item AND i is not the FIRST item AND i does the previous item, we put it into new []
        elif items[-1] != i and n != 0 and i == items[(n-1)]:
            new.insert(len(new),i)
        # if i is not the last item AND i is not the FIRST item AND i does not the previous item, we push the previous new to result,
        # make new = [] again, then insert this item into new []
        elif items[-1] != i and n != 0 and i != items[(n-1)]:
            result.insert(len(result),new)
            new = []
            new.insert(len(new),i)
        # if i is the last item AND i doesn't = the previous item, we push the previous new, make new = [], insert this i into new, then push this one
        elif items[-1] == i and i != items[(n-1)]:
            result.insert(len(result),new)
            new = []
            new.insert(len(new),i)
            result.insert(len(result),new)
        # if i is the last item AND i does = the previous item, we put it into new and push it
        elif items[-1] == i and i == items[(n-1)]:
            new.insert(len(new),i)
            result.insert(len(result),new)
    print(result)

group_equal([1, 1, 4, 4, 4, "hello", "hello", 4])


#new.insert(len(new),i)
#result.insert(len(result),new)
#new = []