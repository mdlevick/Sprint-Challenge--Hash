#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hash = {}
    route = [None] * length

    for t in tickets:
        hash[t.source] = t.destination

    current = hash["NONE"]
    i = 0
    while current != "NONE":
        route[i] = current
        current = hash[current]
        i += 1
    route[i] = "NONE"
    return route
