#!/usr/bin/env python3

"""Implements different deduplication methods and tests their efficiency."""
import timeit


def main():
    """
    Demonstrates the effectiveness and efficiency of deduplication methods.

    This program uses an arbitrary list full of duplicate entries. The program
    then demonstrates the effectiveness of various deduplication methods.
    Finally, the program displays data on the efficiency of the deduplication
    methods.
    """
    someList = ["Humble Bundle",
                "Steam",
                "Origin",
                "GOG.com",
                "Humble Bundle",
                "Steam",
                "Blizzard App",
                "Origin",
                "Origin",
                "Steam",
                "Steam",
                "GOG.com",
                "Steam"]

    # Demonstrate that all methods do remove duplicates.
    deduplicatedList1 = deduplicator1(someList)
    deduplicatedList2 = deduplicator2(someList)
    deduplicatedList3 = deduplicator3(someList)

    print("Deduplicated list (Method 1):")
    print("{}\n".format(deduplicatedList1))

    print("Deduplicated list (Method 2):")
    print("{}\n".format(deduplicatedList2))

    print("Deduplicated list (Method 3):")
    print("{}\n".format(deduplicatedList3))

    # Demonstrate the respective efficiencies of the methods.
    efficiencyTests(someList)


def deduplicator1(someList):
    """
    Create a list of the distinct elements from some other list.

    Args:
        someList: any abitrary list of items.
    Returns:
        someList with all duplicates removed.

    """
    deduplicatedList = []
    for item in someList:
        if item not in deduplicatedList:
            deduplicatedList.append(item)
    return deduplicatedList


def deduplicator2(someList):
    """
    Create a deduplicated list using Python's set datatype.

    Args:
        someList: any abitrary list of items.
    Returns:
        someList with all duplicates removed.

    """
    deduplicatedList = list(set(someList))
    return deduplicatedList


def deduplicator3(someList):
    """
    Create a deduplicated list by manipulating the original list.

    This method is most like the algorithm described in the first interview.

    Args:
        someList: any abitrary list of items.
    Returns:
        someList sorted with all duplicates removed.

    """
    listLength = len(someList)
    someList.sort()
    counter = 0
    while counter < listLength - 1:
        if someList[counter] == someList[counter + 1]:
            del someList[counter + 1]
            # Update list length as you delete and avoid out of bounds errors.
            listLength = len(someList)
        else:
            counter += 1
    return someList


def efficiencyTests(someList):
    """
    Test the efficiency of various deduplication functions.

    Args:
        someList: any arbitrary list of items.

    """
    print("Testing methods by running them 1000 times.")

    # Test deduplicator1 efficiency.
    start = timeit.default_timer()
    for i in range(0, 9999):
        deduplicatedList = deduplicator1(someList)
    finish = timeit.default_timer()
    runtime = finish - start
    print("Time for Method 1 to run 1000 times: {} seconds".format(runtime))

    # Test deduplicator2 efficiency.
    start = timeit.default_timer()
    for i in range(0, 9999):
        deduplicatedList = deduplicator2(someList)
    finish = timeit.default_timer()
    runtime = finish - start
    print("Time for Method 2 to run 1000 times: {} seconds".format(runtime))

    # Test deduplicator3 efficiency.
    start = timeit.default_timer()
    for i in range(0, 9999):
        deduplicatedList = deduplicator3(someList)
    finish = timeit.default_timer()
    runtime = finish - start
    print("Time for Method 3 to run 1000 times: {} seconds".format(runtime))


if __name__ == "__main__":
    main()
