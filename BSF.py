
# FUNCTION FOR BFS
def bfs(adj, start):
    visited = [0] * len(adj)
    queue = [start]
    visited[start] = 1

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


# MAIN PROGRAM
print("******** PROGRAM PREPARED BY NAYAN AHIRE ********")
print("======== PRACTICAL NO-09 (BFS) ========")
print("******** BREADTH FIRST SEARCH *********\n")


# TAKE NUMBER OF NODES AND EDGES BY USER
nodes = int(input("ENTER TOTAL NUMBER OF NODES: "))
edges = int(input("ENTER NUMBER OF EDGES: "))


# CREATE ADJACENCY LIST
adj = [[] for _ in range(nodes)]


# ACCEPT THE EDGES
print("\nENTER THE EDGES:")

for i in range(edges):
    a = int(input("ENTER THE STARTING NODE: "))
    b = int(input("ENTER THE END NODE: "))

    adj[a].append(b)
    adj[b].append(a)


# DISPLAY ADJACENCY LIST AFTER ADDING EDGES
print("\nADJACENCY LIST:")

for i in range(nodes):
    print(i, "->", adj[i])


# TAKE STARTING NODE
start = int(input("\nENTER START NODE: "))


# PERFORM BFS TRAVERSAL
print("\nBFS TRAVERSAL:")

bfs(adj, start)

print()
