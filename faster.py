# -*- coding: utf-8 -*-

import time

#start = time.time()

cases = int(raw_input())

for i in range(0, cases):

    credit = int(raw_input())
    items = int(raw_input())
    item_cost_raw = raw_input().split()
    item_cost = []
    index = 0

    # Convert the items input to integers
    for index in range(0, items):
        # We also save the item initial index for giving the correct result output later
        item_cost.append((int(item_cost_raw[index]), index))

    item_cost.sort()   # Sort by first value (item price)

    for j in range(0, items):
        for k in range(j+1, items):

            cost = item_cost[j][0] + item_cost[k][0]
            if cost > credit:
                # As item_cost is ordered, if we get to the state when the sum of both items
                # is greater than credit, we stop searching for the solution in this iteration.
                break


            if cost == credit:
                # Solution found!

                # We get the initial item indexes from the second element of the list

                index1 = item_cost[k][1] + 1
                index2 = item_cost[j][1] + 1

                # Requirement: The lower index should be output first.
                # As we changed initial order, we might get the first item index to be smaller than
                # the second, so, we swap orders
                if index2 < index1:
                    index2, index1 = index1, index2

                print "Case #" + str(i+1) + ": " + str(index1) + " " + str(index2)
                break


#end = time.time()
#print end - start

