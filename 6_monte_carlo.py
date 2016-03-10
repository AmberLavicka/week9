# Pascal's Problem: Dice Simulation
#
# Would it be profitable to bet that within 24 rolls of a pair of dice,
# that you would roll a double 6?
#

import random
from random import choice

dice =[1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
count = 0

t = 10000

#as t gets bigger, probability gets more accurate

for i in range(t):
    for i in range(24):
        x = choice(dice)
        y = choice(dice2)
        if x == 6 and y == 6:
            count +=1
            break

# question is whether you get the double 6 roll once, would then stop

probability = count / t

print(probability)



        
