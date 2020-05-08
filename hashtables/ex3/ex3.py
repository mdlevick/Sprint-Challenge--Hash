def intersection(arrays):

    hash = {}

    for a in arrays:
        for i in a:
            if hash.get(i, None) is None:
                hash[i] = 0
            hash[i] += 1

    result = [ i for i, n in hash.items() if n == len(arrays) ]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
