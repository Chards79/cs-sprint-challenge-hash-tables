#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.next = None


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    return route


# for this problem the source will be the key with the destination as its value
# the tickets should be linked together like a linked list starting at a source and moving to a destination which then is linked next to the source that is the same as the previous destination until one arrives at None
#
