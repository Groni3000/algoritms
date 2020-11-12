"""
Type 2 integer numbers: a,b and you'll get average of all integer numbers in [a,b].
"""
#---DEFINITION---#
def aver(a,b):
    res=[el for el in range(a,b+1) if el%3==0]
    print(sum(res)/len(res))
#---DEFINITION---#

#---EXECUTE---#
a,b=int(input()),int(input())
aver(a,b)



"""
If you wanna make it "smarter" and without loops.

#---DEFINITION---#
def aver(a,b):
    a += -a%3
    b -= b%3
    print((a+b)/2)
#---DEFINITION---#

#---EXECUTE---#
a,b = int(input()), int(input())
aver(a,b)
"""