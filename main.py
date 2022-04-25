def dfs(node, goals, G):
    print("DFS starts")
    start = node
    visited = []
    stack = [node]
    parent = dict()  # dictionary to hold the parent of each node in order to find solution path
    solution_path = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if str(node) in goals:
                solution_path.append(node)
                curr = node
                while not curr == start:
                    val = parent.pop(curr)
                    solution_path.append(val)
                    curr = val
                solution_path.reverse()
                print(f"search path is {visited} \nsolution path is {solution_path} ")
                return
        for neighbour in G[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                parent[neighbour] = node
    print("Goal not found")

def bfs(node, goals, G):
    print("BFS starts")
    start = node
    visited = []
    queue = [node]
    parent = dict()  # dictionary to hold the parent of each node in order to find solution path
    solution_path = []
    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            if str(node) in goals:
                solution_path.append(node)
                curr = node
                while not curr == start:
                    val = parent.pop(curr)
                    solution_path.append(val)
                    curr = val
                solution_path.reverse()
                print(f"search path is {visited} \nsolution path is {solution_path} ")
                return
        for neighbour in G[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                parent[neighbour] = node
    print("Goal not found")

def depth_limited(node, goals, G, depthlimit):
    print(f"Depth limited with depth = {depthlimit} starts")
    start = node
    visited = []
    stack = [node]
    parent = dict()  # dictionary to hold the parent of each node in order to find solution path
    solution_path = []
    depth = 0
    number_of_nodes_in_current_level = len(stack)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if str(node) in goals:
                solution_path.append(node)
                curr = node
                while not curr == start:
                    val = parent.pop(curr)
                    solution_path.append(val)
                    curr = val
                solution_path.reverse()
                print(f"search path is {visited} \nsolution path is {solution_path} ")
                return
        number_of_nodes_in_current_level -= 1
        if number_of_nodes_in_current_level == -1:
            depth += 1
            number_of_nodes_in_current_level = len(stack)
        if depth < depthlimit:
            for neighbour in G[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    parent[neighbour] = node

    print("Goal not found")

"""
1 2
2 3
2 6
6 4
6 7
2 8
5 1
"""