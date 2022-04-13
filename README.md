# Lists
Part 1:
The algorithm described for this assignment is known as the Sieve of Eratosthenes. The algorithm is designed to find all prime numbers within a given range in an interesting way - instead of testing each number to see if it is prime, it assumes that all numbers are prime. It then finds all "non prime" numbers and marks them as such. When the algorithm is finished you are left with a list of numbers along with their designation (Prime or Not Prime).

Ask the user for a positive integer greater than or equal to 10. Ensure the value is positive - if it isn't, re-prompt the user. This number will be referred to as n.
Create a list of n+1 values ... all of which are set to "P" (hint: use list repetition). This list represents the numbers 0 to n (based on the indexes in the list)
Set your "known" non-prime numbers (positions 0 and 1) to "N" for "Not Prime"
Set up some kind of loop that examines all numbers from 2 through n.
If the value stored at the position you are examining is holding the value "P" for "Prime" then you need to visit all positions that are multiples of that number and set those the value at those positions equal to "N" for "Not Prime". You will probably need another loop to do this.
If the value stored at the position you are examining is holidng the value "N" for "Not Prime" then you can effectively skip it and move onto the next number.
When you are finished examining all numbers your program should print out all of the prime numbers that you have found in neatly aligned columns (with up to 10 prime numbers on every row). 

Part 2a:
Imagine that you are helping to build a store management system for a fast food restaurant. Given the following lists, write a program that asks the user for a product name. Next, find out if the restaurant sells that item and report the status to the user. Allow the user to continually inquire about product names until they elect to quit the program.

Part 2b:
Next, extend your program so that it keeps track of how many products the store currently has to sell. Default the store to have 10 soft drinks, 5 onion rings and 20 small fries. You should modify your program to do the following:

Update the search feature to include a report of how many products the store currently has
Add a new feature that lists ALL products, their prices and the amount the store has available to sell

Part 2c:
Next, add in an "add" feature that lets users add a new product to the store. When you add a product you will need to ask the user for the name of the product, the cost of the product and how many items the store has available to sell. Validate this data - you cannot add a product that already exists and both the price and inventory amount must be positive.

Part 2d:
Next, add in a "remove" feature that lets users remove products from the database.

Part 2e:
Add in the ability to modify a product. Users should be able to modify the name, cost or quantity of a product. Note that you will need to perform data validation as needed. 

Part 2f:
Finally, add in a reporting feature to your program that finds the highest priced product, the lowest priced product and the total value of all inventory in the store (product cost * product quantity). 

Part 3:
Imagine that the most of the functions that we have been using to process lists in Python do not exist. For the problems below you are not allowed to use any list methods (append, remove, insert, etc) or certain core Python functions specified in each problem. You may, however, use your own custom-written functions to solve these problems (i.e. if you find that your listlen() function would be useful in writing another function you are welcome to use it). Given these restrictions, write a series of functions that do the following:

1. Write a new function called "listlen" based on the following IPO:

function:    listlen
 INPUT:       a list
 PROCESSING:  determines the size of the list
 OUTPUT:      an integer representing the size of the list
 
2. Write a new function called "listmax" based on the following IPO

 function:    listmax
 INPUT:       a list
 PROCESSING:  obtains the largest element in the list
 OUTPUT:      returns the largest element in the list

3. Write a new function called "listcopy" based on the following IPO

 function:    listcopy
 INPUT:       a list
 PROCESSING:  creates a new list which serves as a copy of the supplied list
 OUTPUT:      returns a new copy of the list

4. Write a new function called "listappend" based on the following IPO

 function:    listappend
 INPUT:       a list and an element to add to the list (any data type)
 PROCESSING:  creates a new list which includes the new element appended
              to the end of the list
 OUTPUT:      returns a new copy of the list

5. Write a new function called "listinsert" based on the following IPO

 function:    listinsert
 INPUT:       a list, a location (integer) and a data 
              element (can be a string, float, Boolean or 
              int)
 PROCESSING:  inserts the supplied data element into the 
              list at the desired location
 OUTPUT:      return a new copy of the list that contains
              the inserted element

6. Write a new function called "listremove" based on the following IPO

 function:    listremove
 INPUT:       a list and a data element (can be a string, 
              float, Boolean or int)
 PROCESSING:  removes all occurrences of the supplied 
              data element from the list.  You can assume 
              that the data element is present in the list 
              somewhere.
 OUTPUT:      return a new copy of the list with the
              desired element removed

7. Write a new function called "listreverse" based on the following IPO

 function:    listreverse
 INPUT:       a list
 PROCESSING:  creates a copy of the supplied list that
              contains the same elements as the original
              list, but in reverse order
 OUTPUT:      return a new copy of the list in reverse order
