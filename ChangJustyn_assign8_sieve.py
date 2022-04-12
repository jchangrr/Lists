"""
Assignment #8, Part 1
Justyn Chang
"""
#ask for positive integer greater than or equal to 10 and validate
num = int(input("Enter a positive integer greater than or equal to 10: "))
while num <= 9:
    print("Invalid integer, please try again.")
    print()
    num = int(input("Enter a positive integer greater than or equal to 10: "))

#set every number equal to P except 0 and 1
sieve = ["P"] * (num + 1)
sieve[0] = "N"
sieve[1] = "N"

#examine numbers from 2 through N and change any non-prime number to N
counter = 1
for i in range(2, len(sieve), 1):
    if sieve[i] == "P":
        counter += 1
        for i in range((counter + counter), len(sieve), counter):
            sieve[i] = "N"

#print prime numbers in rows of 10
count = 0
p = 0
while count <= num:
    if sieve[count] == "P":
        p += 1
        prime = format(str(count), "<7s")
        if p % 10 != 0:
            print(prime, end = "")
        elif p % 10 == 0:
            if p == 0:
                print(prime, end = "")
            else:
                print(prime)
    count += 1
