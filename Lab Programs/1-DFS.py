def dfs(graph, start):
    visited = set()  
    stack = [start]  

    while stack:
        node = stack.pop()  

        if node not in visited:
            visited.add(node)
            print(node)  

            stack.extend(graph[node] - visited)

    return visited

graph = {"A": {"B","D","E"},
            "B": {"B","D","E"},
            "C": {"B","D","E"},
            "D": {"B","D","E"},
            "E": {"B","D","E"},
            "F": {"B","D","E"},
            "G": {"B","D","E"}}


print("DFS Traversal:")
dfs(graph, 'A')
