tree = {
    '1' : ['2', '3'],
    '2' : ['4', '5'],
    '3' : ['6', '7'],
    '4' : [],
    '5' : [],
    '6' : [],
    '7' : []
}
visited = []
def BFS(current_level):
    if not current_level:
        return
    next_level = []  
    for node in current_level:
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
            for neighbor in tree[node]:
                if neighbor not in visited:
                    next_level.append(neighbor)
    BFS(next_level)
current_level = ["1"]
BFS(current_level)