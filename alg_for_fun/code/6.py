"""
Type 4 integer numbers: a,b,c,d and you will get a multiplication table of all integer numbers in Cartesian product [a,b]x[c,d].
"""
#---DEFINITION---#
def mult_table(a,b,c,d):
    print('',end='\t')
    for i in range(c,d+1):
        if i!=d:
            print(i,end='\t')
        else:
            print(i)
    for i in range(a,b+1):
        print(i,end='\t')
        for j in range(c,d+1):
            if j!=d:
                print(i*j,end='\t')
            else:
                print(i*j)
#---DEFINITION---#
"""Ye, this is dumb output... But it was a task."""

#---EXECUTE---#
a,b,c,d=int(input()),int(input()),int(input()),int(input())
mult_table(a,b,c,d)