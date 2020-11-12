"""
Type integer numbers and after you wrote number greater than 100, you'll get all numbers that are in between 10 and 100 (10<= N <=100)
"""
#---DEFINITION---#
def dunno():
    result=[]
    while True:
        n=int(input("Type your number: "))
        if n<=100 and n>=10:
            result.append(n)
        elif n>100:
            break

    for el in result:
        print(el, sep='/n')
#---DEFINITION---#

#---EXECUTE---#
dunno()

'''If you want to print number after you wrote it

n=int(input("Type your number: "))
while n<=100:
    if n>=10:
        print(n)
    elif n>100:
        break
    n=int(input("Type your number: "))

'''