def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    HashTable = {}

    for x in weights:
        if x is not None:
            HashTable[x] =  # the list index

    Arr = []

    for x in HashTable:
        if limit == x + x:
            Arr.append(x)
            return Arr
        else:
            return None


# need to be able to find 2 weights in a list that add up to the given limit
# need to return the indices of those 2 weights in a tuple, or None if there is no combination that adds up to the limit
# probably want to iterate through the list of weights
# want to store each weight as a key with a value of its list index inside of a hash table/dictionary
#
