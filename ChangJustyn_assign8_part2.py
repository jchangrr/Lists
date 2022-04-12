"""
Assignment #8, Part 2
Justyn Chang
"""
#create lists for names, costs, and quantity of items
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_stock = [10, 5, 20]

#ask for action and validate
action = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
while action != "s":
        if action == "q":
            break
        elif action == "l":
            break
        elif action == "a":
            break
        elif action == "r":
            break
        elif action == "u":
            break
        elif action == "e":
            break
        else:
            print("Invalid option, try again")
            print()
            action = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
while action != "q":
    #if action = s, then ask for product name
    if action == "s":
        name = input("Enter a product name: ")
        #determine if product is available and if so, how much is in stock and at what price
        if name in product_names:
            num = product_names.index(name)
            print('We sell "', name, '" at ', product_costs[num], " per unit", sep = "")
            print("We currently have", product_stock[num], "in stock")
            print()
        else:
            print("Sorry, we don't sell ", '"', name, '"', sep = "")
            print()
    #if action = l, then list out products, costs, and quantity
    elif action == "l":
        print(format("Product", "<25s"), format("Price", "<6s"), "Quantity")
        count = 0
        for i in range(0, len(product_names), 1):
            fcost = format(product_costs[count], ".2f")
            print(format(product_names[count], "<25s"), format(fcost, "<6s"), product_stock[count])
            count += 1
        print()
    #if action = a, ask for product name
    elif action == "a":
        new = input("Enter a new product name: ")
        #determine if new product is already sold or not
        while new in product_names:
            print("Sorry, we already sell that product. Try again.")
            new = input("Enter a new product name: ")
        #add new product to old list
        product_names.append(new)
        #ask for cost of new product and validate
        cost = float(input("Enter a new product cost: "))
        while cost <= 0:
            print("Invalid cost. Try again.")
            cost = float(input("Enter a new product cost: "))
        #add new cost to old list
        product_costs.append(cost)
        #ask for quantity of new product and validate
        inv = int(input("How many of these products do we have? "))
        while inv <= 0:
            print("Invalid quantity. Try again.")
            inv = int(input("How many of these products do we have? "))
        #add new quantity to old list
        product_stock.append(inv)
        print("Product added!")
        print()
    #if action = r, ask for product name and validate
    elif action == "r":
        choice = input("Enter a product name: ")
        if choice not in product_names:
            print("Product doesn't exist. Can't remove.")
            print()
        else:
            #find product in list and remove
            num1 = product_names.index(choice)
            product_names.remove(choice)
            cost1 = product_costs[num1]
            stock1 = product_stock[num1]
            product_costs.remove(cost1)
            product_stock.remove(stock1)
            print("Product removed!")
            print()
    #if action = u, ask for product name and validate
    elif action == "u":
        up = input("Enter a product name: ")
        if up not in product_names:
            print("Product doesn't exist. Can't update.")
            print()
        else:
            #find product in list and ask if name, cost, or quantity should be updated and validate
            up = product_names.index(up)
            print("What would you like to update?")
            choose = input("(n)ame, (c)ost or (q)uantity: ")
            list1 = ["n", "c", "q"]
            if choose not in list1:
                print("Invalid option")
                print()
            #if n is chosen, enter new name and validate
            elif choose == "n":
                newname = input("Enter a new name: ")
                while newname in product_names:
                    print("Duplicate name!")
                    newname = input("Enter a new name: ")
                product_names[up] = newname
                print("Product name has been updated")
                print()
            #if c is chosen, enter new cost and validate
            elif choose == "c":
                newcost = float(input("Enter a new cost: "))
                while newcost <= 0:
                    print("Invalid cost!")
                    newcost = float(input("Enter a new cost: "))
                product_costs[up] = newcost
                print("Product cost has been updated")
                print()
            #if q is chosen, enter new quantity and validate
            elif choose == "q":
                newstock = int(input("Enter a new quantity: "))
                while newstock <= 0:
                    print("Invalid quantity!")
                    newstock = int(input("Enter a new quantity: "))
                product_stock[up] = newstock
                print("Product quantity has been updated")
                print()
    #if action = e, then find max and min costs and determine corresponding products
    elif action == "e":
        big = max(product_costs)
        index1 = product_costs.index(big)
        bigname = product_names[index1]
        small = min(product_costs)
        index2 = product_costs.index(small)
        smallname = product_names[index2]
        counting = 0
        total = 0
        #find total cost of all products in stock
        for i in range(0, len(product_costs), 1):
            total = (product_costs[counting] * product_stock[counting]) + total
            counting += 1
        total = format(total, ".2f")
        #print results
        print(format("Most expensive product: ", "<29s"), big, " (", bigname, ")", sep = "")
        print(format("Least expensive product: ", "<29s"), small, " (", smallname, ")", sep = "")
        print(format("Total value of all products:", "<28s"), total)
        print()
    #repeat actions until q is chosen
    action = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    while action != "s":
        if action == "q":
            break
        elif action == "l":
            break
        elif action == "a":
            break
        elif action == "r":
            break
        elif action == "u":
            break
        elif action == "e":
            break
        else:
            print("Invalid option, try again")
            print()
            action = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
print("See you soon!")

