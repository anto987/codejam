# -*- coding: utf-8 -*-

# import time

# start = time.time()
    
cases = int(raw_input())
for i in range(0, cases):

    credit = int(raw_input())
    items = int(raw_input())
    item_costs = raw_input().split()
    item_cost = []
    for item in item_costs:
        # Convert the items to integers
        item_cost.append(int(item))

    for j in range(0, items):
        for k in range(j+1, items):
            if item_cost[j] + item_cost[k] == credit:
                # Solution Found!
                print "Case #" + str(i+1) + ": " + str(j+1) + " " + str(k+1)
                    

# end = time.time()
# print end - start
