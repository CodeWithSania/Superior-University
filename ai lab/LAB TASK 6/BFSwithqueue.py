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
queue = []
def BFS(node):
    visited.append(node)
    queue.append(node)
    while queue:
        pop_itm = queue.pop(0)
        print(pop_itm,end = " ")
        for i in tree[pop_itm]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
BFS("1")