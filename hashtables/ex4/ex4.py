def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    HashTable = {}

    for x in a:
        if x >= 0:
            # trying to add x as key to HashTable/dictionary with value of True
            HashTable[x] = True
        else:
            pass

    Arr = []

    for x in a:
        if x < 0 and -x:
            Arr.append(-x)
        else:
            pass

    return Arr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


# The following is more or less what I think a brute force strategy might look like, although it doesn't work to pass any tests as such:
# for i in a:
#         for j in a:
#             if -i == j:

#                 return i
