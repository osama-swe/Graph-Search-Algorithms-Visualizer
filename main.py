
def dfs(node, goals, G):
    visited = []
    stack = [node]
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            if str(node) in goals:
                return visited
        for neighbour in G[node]:
            if not neighbour in visited:
                stack.append(neighbour)

