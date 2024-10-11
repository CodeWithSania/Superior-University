tree = {
    '1' : ['2', '3'],
    '2' : ['4', '5'],
    '3' : ['6', '7'],
    '4' : [],
    '5' : [],
    '6' : [],
    '7' : [],
}

visited=list()

def preorder(node,visited):
    if node is not visited:
        print(node ,end=' ')
        visited.append(node)
        for neighbours in tree[node]:
            preorder(neighbours,visited)
def inorder(node,visited):
    if node not in visited:
        visited.append(node)
        if tree[node]:
            inorder(tree[node][0],visited)
        print(node,end=' ')
        if len(tree[node])>1:
            inorder(tree[node][1],visited)

def postorder(node,visited):
    if node not in visited:
        for neighbor in tree[node]:
            postorder(neighbor,visited)
        print(node,end=' ')

print("pre_order DFS:")
visited=list()
preorder('1',visited)

print('\nin_order DFS:')
visited=list()   
inorder('1',visited)

print('\npost_order DFS:')
visited=list()
postorder('1',visited)