def union(a, b):      return a | b
def intersect(a, b):  return a & b
def diff(a, b):       return a - b
def cartesian(a, b):  return {(x, y) for x in a for y in b}

def power_set(a):
    s = list(a)
    return [set(s[i] for i in range(len(s)) if m >> i & 1)
            for m in range(1 << len(s))]

if __name__ == "__&#8203;main__":
    A, B = {1, 2, 3}, {3, 4}
    print("A∪B =", union(A, B))
    print("A∩B =", intersect(A, B))
    print("A−B =", diff(A, B))
    print("A×B =", sorted(cartesian(A, B)))
    print("P(A) =", power_set(A))
