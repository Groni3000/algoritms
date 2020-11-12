import random as _
import numpy


'''
Just tossing a coin as many times as needed to get # of heads you wish and shows how many heads and tails you've got
'''

#---DEFINITION---#
def get_n_heads():
    n=int(input("Type how many heads in a row do you want: "))
    res=[]
    k=0
    while k!=n:
        res.append(_.randint(0,1))
        if res[len(res)-1]==0:
            k+=1
        else:
            k=0

    print(len(res), 'times you tossed a coin *to your witcher* and, finally, got', n, 'heads in a row!')
    print("There were", res.count(0), "heads and", res.count(1), "tails!")
    print("Dispersion:", numpy.var(res))
    print("Standart deviation:", numpy.std(res))
#---DEFINITION---#

#---EXECUTE---#
get_n_heads()
