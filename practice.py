#실습2

def gugudan_odd():
    odds = [1,3,5,7,9]
    for odd in odds:
        for i in range(1,10):
            print("%d * %d = %d" %(odd, i, odd*i))


def gugudan_even():
    evens = [2,4,6,8]
    for even in evens:
        for i in range(1,10):
            print("%d * %d = %d" %(even, i, even*i))

def gugudan_odd_or_even(a):
    if a%2 == 0:
        gugudan_even()
    else: gugudan_odd()


    #실습3
for i in range(2, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))

                    
