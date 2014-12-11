# -*- coding: utf-8 -*-
import sys
import time

def main():

    cases = int(raw_input())
    for i in range(0, cases):

        credit = int(raw_input())
        items = int(raw_input())  # We don't use it, but read input it anyway.
        item_cost_raw = raw_input().split()
        item_cost = []

        # Convert the items input to integers
        for index in range(0, len(item_cost_raw)):
            # We also save the item initial index for giving the correct result output later
            item_cost.append((int(item_cost_raw[index]), index))
        item_cost.sort()   # Sort by first value (item price)

        print solution(i, item_cost, credit)


def solution(case, item_cost, credit):
    for j in range(0, len(item_cost)):
        lo = 0
        hi = len(item_cost)
        # The item we want to find is the remaining credit after buying current item.
        diff = credit - item_cost[j][0]

        # We try to find the item with difference value with Binary search
        while lo < hi:
            mid = (lo+hi)//2
            midval = item_cost[mid][0]

            if midval < diff:
                lo = mid + 1
            elif midval > diff:
                hi = mid
            else:

                # Solution found!

                # We get the initial item indexes from the second element of the list
                index1 = item_cost[mid][1] + 1
                index2 = item_cost[j][1] + 1

                # Requirement: The lower index should be output first.
                # As we changed initial order, we might get the first item index to be smaller than
                # the second, so, we swap orders
                if index2 < index1:
                    index2, index1 = index1, index2

                return "Case #" + str(case+1) + ": " + str(index1) + " " + str(index2)


if __name__ == "__main__":
    # start = time.time()
    main()
    # end = time.time()
    # print end - start
    sys.exit()

