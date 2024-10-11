graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

def find_shortest_path(graph, start, goal):
    open_list = [start]
    goal_cost = {start: 0}
    came_from = {}

    while open_list:
        current = min(open_list, key=goal_cost.get)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]
        
        open_list.remove(current)

        for neighbor, move_cost in graph.get(current, []):
            tentative_goal_cost = goal_cost[current] + move_cost
            
            if neighbor not in goal_cost or tentative_goal_cost < goal_cost[neighbor]:
                open_list.append(neighbor)
                goal_cost[neighbor] = tentative_goal_cost
                came_from[neighbor] = current
    
    return None

start_node = 'A'
goal_node = 'F'

path = find_shortest_path(graph, start_node, goal_node)

if path:
    print("Shortest path:", path)
else:
    print("No path found")
