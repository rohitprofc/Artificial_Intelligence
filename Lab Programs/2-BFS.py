adj_list={
    'S':['A','B'],
    'A':['S','C'],
    'B':['S','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','F'],
    'E':['C','G'],
    'F':['D','G'],
    'G':['E','F']
    }
h={
    'S':6,
    'A':4,
    'B':4,
    'C':4,
    'D':3,
    'E':1,
    'F':1,
    'G':0
    }
start=input("Enter start state:")
goal=input("Enter goal state:")
visited=[]

def best(node):
    visited.append(node)
    if node==goal:
        return
    next_nodes = []
    next_hvalues = []
    for v in adj_list[node]:
        if v in adj_list[node]:
            next_nodes.append(v)
            next_hvalues.append(h[v])
    indx=next_hvalues.index(min(next_hvalues))
    best(next_nodes[indx])
best(start)
print(visited)

# Output:-
# Enter start state:S
# Enter goal state:G
# ['S', 'A', 'C', 'E', 'G']