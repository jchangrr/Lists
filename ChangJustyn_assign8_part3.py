"""
Assignment #9, Part 3
Justyn Chang
"""
# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list
def listlen(list1):
    count = 0
    for item in list1:
        count += 1
    return count

# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list
def listmax(list1):
    count = 0
    value = 0
    for item in list1:
        newvalue = list1[count]
        if newvalue > value:
            value = newvalue
        count += 1
    if value == 0:
        value = "None"
    return value

# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list
def listcopy(list1):
    count = 0
    value = 0
    list2 = []
    for item in list1:
        value = list1[count]
        list2 = list2 + [value]
        count += 1
    return list2

# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list
def listappend(list1, element):
    list2 = list1 + [element]
    return list2

# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element
def listinsert(list1, location, element):
    list2 = list1[0:location]
    list2 = list2 + [element]
    list3 = list1[location:len(list1)]
    list4 = list2 + list3
    return list4

# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed
def listremove(list1, element):
    count = 0
    for item in list1:
        if list1[count] == element:
            list2 = list1[0:count]
            list3 = list1[(count + 1):len(list1)]
            list4 = list2 + list3
        count += 1
    return list4

# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order
def listreverse(list1):
    count = 0
    value = 0
    list2 = []
    for item in list1:
        value = list1[count]
        list2 = list2 + [value]
        count += 1
    count = 0
    for item in list2:
        new = list1[(len(list2) - 1) - count]
        list2[0 + count] = new
        count += 1
    return list2
