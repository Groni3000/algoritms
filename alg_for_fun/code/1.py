import random as _
import numpy


'''
Just tossing a coin as many times as you wish and shows how many heads and tails you've got
'''

#---DEFINITION---#
def toss_a_coin_to_your_witcher():
    n=int(input("Type how many times do you want to toss a coin: "))
    res=[_.randint(0,1) for i in range(n)]

    print("There were", res.count(0), "heads and", res.count(1), "tails!")
    print("Dispersion:", numpy.var(res))
    print("Standart deviation:", numpy.std(res))
#---DEFINITION---#

#---EXECUTE---#
toss_a_coin_to_your_witcher()

