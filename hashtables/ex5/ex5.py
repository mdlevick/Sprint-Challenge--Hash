def all_paths(path):
    return [ "/".join(path.split("/")[1:][-i:])\
             for i in range(len(path.split("/"))) ]
             
def finder(files, queries):

    paths = {}

    for f in files:
        for p in all_paths(f):
            if paths.get(p, None) is not None:
                paths[p].append(f)
            else:
                paths[p] = [f]

    result = []
    for q in queries:
        if q[0] == "/":
            q = q[1:]
        if paths.get(q, None) is not None:
            result += paths[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
