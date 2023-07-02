adj_list = {"A": ["B","D","E"],
            "B": ["B","D","E"],
            "C": ["B","D","E"],
            "D": ["B","D","E"],
            "E": ["B","D","E"],
            "F": ["B","D","E"],
            "G": ["B","D","E"]}
color = dict()
parent = dict()
trav_time = dict()
stack = []
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]

time = 0
def dfs_util(node):
    global time
    color[node] = "G"
    trav_time[node][0]=time
    stack.append(node)
    time+=1
    for v in adj_list[node]:
        if color[v] == "W":
            parent[v]=node
            dfs_util(v)
    color[node]="B"
    trav_time[node][1]=time
    time+=1
dfs_util("A")
print("\nColor of each node: ",color)
print("\nTravel time of each node: ",trav_time)
print("\nParent of each node: ",parent)
print("\nDFS Path: ",stack)


#Output:- 

# Color of each node:  {'A': 'B', 'B': 'B', 'C': 'W', 'D': 'B', 'E': 'B', 'F': 'W', 'G': 'W'}

# Travel time of each node:  {'A': [0, 7], 'B': [1, 6], 'C': [-1, -1], 'D': [2, 5], 'E': [3, 4], 'F': [-1, -1], 'G': [-1, -1]}

# Parent of each node:  {'A': None, 'B': 'A', 'C': None, 'D': 'B', 'E': 'D', 'F': None, 'G': None}

# DFS Path:  ['A', 'B', 'D', 'E'] 