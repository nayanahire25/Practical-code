# FUNCTION FOR DFS
def dfs(matrix, start, visited):
    print(start, end=" ")
    visited[start] = 1

    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, i, visited)


# MAIN PROGRAM
print("******** PROGRAM PREPARED BY NAYAN AHIRE ********")
print("======== PRACTICAL NO-09 (DFS) ========")
print("******** DEPTH FIRST SEARCH ********\n")


# TAKE NUMBER OF NODES AND EDGES BY USER
nodes = int(input("ENTER TOTAL NUMBER OF NODES: "))
edges = int(input("ENTER NUMBER OF EDGES: "))


# INITIALIZE ADJACENCY MATRIX
matrix = []

for i in range(nodes):
    row = [0] * nodes
    matrix.append(row)


# DISPLAY INITIAL ADJACENCY MATRIX
print("\nADJACENCY MATRIX:")

for row in matrix:
    print(row)


# ACCEPT THE EDGES
print("\nENTER THE EDGES:")

for x in range(edges):
    a = int(input("ENTER THE STARTING NODE: "))
    b = int(input("ENTER THE END NODE: "))

    matrix[a][b] = 1
    matrix[b][a] = 1


# DISPLAY ADJACENCY MATRIX AFTER ADDING EDGES
print("\nADJACENCY MATRIX AFTER ADDING EDGES:")

for row in matrix:
    print(row)


# INITIALIZE ALL NODES TO ZERO
visited = [0] * nodes


# TAKE STARTING NODE FOR DFS
start = int(input("ENTER THE STARTING NODE FOR DFS: "))


# PERFORM DFS TRAVERSAL
print("\nDFS TRAVERSAL:")

dfs(matrix, start, visited)

print()