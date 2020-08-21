def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    HashTable = {}

    for index in range(length):
        hash_index = limit - weights[index]

        if hash_index in HashTable:
            value = HashTable[hash_index]
            output = (index, value)
            return output

        else:
            HashTable[weights[index]] = index

    return None

    # HashTable = {}

    # for weight in weights:
    #     if weight is not None:
    #         HashTable[weight[i]] = i  # the list index
    #     else:
    #         pass

    # Arr = []

    # for weight in HashTable:
    #     if limit - weight in HashTable:
    #         Arr.append(weight)
    #         return Arr
    #     else:
    #         return None


# need to be able to find 2 weights in a list that add up to the given limit
# need to return the indices of those 2 weights in a tuple, or None if there is no combination that adds up to the limit
# probably want to iterate through the list of weights
# want to store each weight as a key with a value of its list index inside of a hash table/dictionary
#
