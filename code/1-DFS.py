def dfs(graph, start):
    visited = set()  
    stack = [start]  
    path = []

    while stack:
        node = stack.pop()  

        if node not in visited:
            visited.add(node)
            path.append(node)

            stack.extend(graph[node] - visited)

    print(path)
    return visited

graph = {"A": {"B","D","E"},
            "B": {"C","E","A"},
            "C": {"B","E","F","G"},
            "D": {"A","E"},
            "E": {"A","B","C","D","F"},
            "F": {"C","E","G"},
            "G": {"C","F"}}


print("DFS Traversal:")
dfs(graph, 'A')

# Output:-
# DFS Traversal:
# A
# B
# C
# E
# F
# G
# D