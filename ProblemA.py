# Aysegul Alpay
# Belle Pensamiento

# Prime Charts and Bar Numbers

'''

The question arose during a conversation with Aysegul regarding Problem 3 on Project Euler.
The task is to get the prime factors of 600851475143. The lowest prime factor was found to be 71, through trial and error.
Aysegul was surprised that it wasn't a lower number. I didn't think that the there was a relationship formed between n and its primes as n increased.
Neither of us could really prove it so we got to work making a bar chart that would visualize the amount of times a number was someone else's prime.
Are bigger numbers are more likely to have 2 as their prime number? what about 3? what about 4, 5, etc? And does this bar chart method actually prove anything?

'''


'''ANSWER:  '''

import sympy as sp

n = 100

mylist = list(range(1,n+1))
print(mylist)

x = list(sp.primerange(1, n+1))

# print(x.index(5))

allnumbers = []

y = []
for j in x:
    n = 0
    # print(j)
    for i in mylist:
        
        if i % j == 0:
            n += 1
            # allnumbers.append(j)
    y.append(n)
    
print(y)
# print(x.index(2))

# # y = allnumbers
listofzeros = [0] * len(x)



# print(listofzeros)
# print(x)


import numpy as np
import matplotlib.pyplot as plt 


plt.bar(x,y)
plt.show()

''' We printed out bar charts for n = 100 and n = 1000 and noted the differences between the occurences of 2 and 3. more analysis should be done. possibly over soju or sake'''