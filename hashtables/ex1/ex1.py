def get_indices_of_item_weights(weights, length, limit):
    hash = {}

    for i, w in enumerate(weights):
        hash[w] = i

    for i, w in enumerate(weights):
        r = hash.get(limit - w, None)
        if r:
            return [ r, i ]

    return None
 
