'''
Type 2 integer numbers to get their lcm
'''
#---DEFINITION---#
def lcm_of_2_numbers():
    a=int(input("Type first number: "))
    b=int(input("Type second number: "))
    m = a*b
    while a!= 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(m // (a+b))
#---DEFINITION---#

#---EXECUTE---#
lcm_of_2_numbers()
