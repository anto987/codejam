# -*- coding: utf-8 -*-
import sys
import time

def main():

    cases = int(raw_input())
    for i in range(0, cases):

        credit = int(raw_input())
        items = int(raw_input())  # We don't use it, but read input it anyway.
        item_cost_raw = raw_input().split()


        # Convert item list to integers
        item_cost = []
        for index in range(0, len(item_cost_raw)):
            item_cost.append(int(item_cost_raw[index]))

        print solution(i, item_cost, credit)


def solution(case, item_cost, credit):
    
    # We create a dictionary with key = item cost, and value = item index.
    item_cost_dict = { item_cost[i]:i for i in range(len(item_cost)) }

    for i in range(len(item_cost)):

        # The key of the item we want to find is the remaining credit after buying current item.
        j = item_cost_dict.get(credit - item_cost[i])

        if j:
            index2 = i + 1
            index1 = j + 1

            # Requirement: The lower index should be output first.
            # As we changed initial order, we might get the first item index to be smaller than
            # the second, so, we swap orders
            if index2 < index1:
                index2, index1 = index1, index2

            return "Case #" + str(case+1) + ": " + str(index1) + " " + str(index2)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print end - start
    sys.exit()

