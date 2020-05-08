def has_negatives(a):

    hash = {}
    result = []

    for i in a:
        if i != 0:
            hash[i] = True
            if hash.get(-i, None) is not None:
                result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
