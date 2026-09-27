def is_reflexive(mat):
    return all(mat[i][i] for i in range(len(mat)))

def is_symmetric(mat):
    n = len(mat)
    return all(mat[i][j] == mat[j][i] for i in range(n) for j in range(n))

def is_transitive(mat):
    n = len(mat)
    return all(not (mat[i][j] and mat[j][k]) or mat[i][k]
               for i in range(n) for j in range(n) for k in range(n))

if __name__ == "__&#8203;main__":
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print("自反:", is_reflexive(M))
    print("对称:", is_symmetric(M))
    print("传递:", is_transitive(M))
