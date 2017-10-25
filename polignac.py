#!/usr/bin/python3
# Author: Juan Bautista Ruiz
# Date: 2017-10
# Quick script to show Polignac Odd numbers > 1 till integer given as argument

import sys

def usage():
    print("")
    print("polignac.py till_integer")
    print("")
    exit(1)

def primestill(fro, till):
    # get prime numbers from "fro" to "till" integers
    # returns a list
    primes=list()
    for num in range(fro+1, till):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return(primes)


def p2(till):
    # returns a list of the powers of 2 less or equal than "till" integer
    powersOfTwo=list()
    for i in range(0, till):
        if 2**i <= till:
            powersOfTwo.append(2**i)
        else:
            break
    return(powersOfTwo)

if len(sys.argv) != 2:
    usage()

# Take argument. convert it to integer. 
max=int(sys.argv[1])

primes=[1]

hundred=0

p_numbers=list()
counter=0
glob_counter=0
t=tuple()

hundreds_zero=list()

# Loop over all natural numbers untill integer given as argument
for i in range(2,int(max)):
    if i % 100 == 0:
        t=hundred*100, counter
        # not smart, but valid since there are no polignac numbers in 0th hundred
        p_numbers.append(t)
        if counter == 0:
            hundreds_zero.append(t)
        hundred = hundred + 1
        counter = 0

    # get prime numbers until current integer
    for item in primestill(primes[-1], i):
        primes.append(item)

    # get powers of 2 less than current integer
    if i % 2 == 0:
        powers=p2(i)

    #print(powers)
    # assuming current number is NOT polignac
    pol="no"
    # Loop all primes less than target 
    for r in primes:
        # Loop all powers of 2 less than target
        for w in powers:
            if (w + r) == i:
                # polignac number found
                pol="yes"

    if i % 2 == 0:
        # discard even polignac numbers
        pol="yes"

    if pol == "no":
        print("POLIGNAC: " + str(i))
        counter = counter + 1
        glob_counter += 1

t=hundred*100, counter
p_numbers.append(t)

#print(p_numbers)

print("TOTAL POLIGNAC numbers found: " + str(glob_counter))
print("HUNDREDs with 0 POLIGNAC numbers: " + str(hundreds_zero))

# Remove following lines if no graph is required

import matplotlib.pyplot as plt

x_val = [x[0] for x in p_numbers]
y_val = [x[1] for x in p_numbers]

_ = plt.bar(x_val, y_val, width=100,  align='edge')
_ = plt.xlim(xmin=0)
_ = plt.ylim(ymin=0)
_ = plt.xlabel('Integers', fontsize=20)
_ = plt.ylabel('Number of Polignac numbers per hundred', fontsize=20)
_ = plt.xticks(x_val, x_val, rotation=80)
_ = plt.title("Polignac")
_ = plt.grid()
plt.show()


