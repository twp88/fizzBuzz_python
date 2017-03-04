
def fizzbuzz(x):
    if x % 3 == 0 and x % 5 != 0:
        print ('fizz')
    elif x % 3 != 0 and x % 5 == 0:
        print ('buzz')
    elif x % 3 == 0 and x % 5 == 0:
        print ('fizzbuzz')
    else: 
        print ('nothing')
