# Passing list inside function.py

# check if number is even or odd

def lst_to_fun(numlist):
    even = 0
    odd = 0

    for num in numlist:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


numlist = [1,2,3,4,5,6,7,8,9]
even,odd = lst_to_fun(numlist)
print(even)
print(odd)