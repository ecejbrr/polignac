#!/usr/bin/env python
# Author: Juan Bautista Ruiz
# Date: 2017-10
# Quick script to show Polignac Odd numbers > 1 till integer given as argument
# Since the conjecture was proven false, the numbers which prove
# that conjecture false are named "Polignac" numbers by some. I take this as well. 

import sys

def usage():
    print("")
    print("polignac.py till_integer")
    print("")
    exit(1)

def primestill(fro, till):
    # get prime numbers from "fro" to "till" integers
    # returns a list
    primes = list()
    for num in range(fro+1, till+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return(primes)


def p2(till):
    # returns a list of the powers of 2 less or equal than "till" integer
    powersOfTwo = list()
    for i in range(0, till):
        if 2**i <= till:
            powersOfTwo.append(2**i)
        else:
            break
    return(powersOfTwo)

if len(sys.argv) != 2:
    usage()

# Take argument. convert it to integer. 
argum = int(sys.argv[1])

primes = [1]

hundred = 0

p_numbers_in_hundred = list()
counter = 0
glob_counter = 0
t = tuple()
p_numbers = list()

# Loop over all natural numbers untill integer given as argument
for i in range(2, argum+1):

    # initially assuming current number is a polignac
    pol = "no"


    if i % 100 == 0:
        t=hundred*100, counter
        # not smart, but valid since there are no polignac numbers in 0th hundred
        p_numbers_in_hundred.append(t)
        hundred = hundred + 1
        counter = 0

    # get prime numbers until current integer
    for item in primestill(primes[-1], i):
        primes.append(item)

    # get powers of 2 less than current integer
    if i % 2 == 0:
        powers=p2(i)
        # discard even numbers. We are just interested in odd ones.
        continue

    #print(powers)
    # Loop all prime numbers less than target 
    for r in primes:
        # Loop all powers of 2 less than target
        for w in powers:
            if (w + r) == i:
                # polignac conjecture confirmed for this integer. 
                # so, this is NOT a polignac number 
                pol="yes"

    if pol == "no":
        # print Polignac numbers
        print("POLIGNAC: " + str(i))
        p_numbers.append(i)
        counter = counter + 1
        glob_counter += 1

t=hundred*100, counter
p_numbers_in_hundred.append(t)


print("#############################################################################")
print("# TOTAL POLIGNAC numbers found: " + str(glob_counter))
print("##############################################")
print("# LIST of POLIGNAC_NUMBERS: " + str(p_numbers))
print("#############################################################################")
print("# LIST of Hundreds*100 and Polignac numbers in it: " + str(p_numbers_in_hundred))
print("##############################################")
print("# LIST of HUNDREDs*100 with 0 POLIGNAC numbers: " + str(list(filter(lambda x: x[1] == 0, p_numbers_in_hundred))))
print("##############################################")
print("# HUNDRED*100 with MAX POLIGNAC numbers: " + str(max(p_numbers_in_hundred, key=lambda x: x[1])))
print("#############################################################################")

# Remove following lines if no graph is required or comment out following line
#exit(0)

import matplotlib.pyplot as plt

x_val = [x[0] for x in p_numbers_in_hundred]
y_val = [x[1] for x in p_numbers_in_hundred]

_ = plt.bar(x_val, y_val, width=100,  align='edge')
_ = plt.xlim(xmin=0)
_ = plt.ylim(ymin=0)
_ = plt.xlabel('Integers', fontsize=20)
_ = plt.ylabel('Number of Polignac numbers per hundred', fontsize=20)
_ = plt.xticks(x_val, x_val, rotation=80)
_ = plt.title("Polignac")
_ = plt.grid()
plt.show()


