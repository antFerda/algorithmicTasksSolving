
# model graph
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}


visited = []

def dfs(graph, value, start=None):
    print("Start node: ", start)

    if start is None:
        keyArr = list(graph.keys())
        key = keyArr[0]
        print("First key ", key)
    else:
        key = start

    if key == value:
        print("FOUND")
        return True
    else:
        visited.append(key)
        for node in graph[key]:
            if node not in visited:
                if dfs(graph, value, start=node):
                    return True
    return False

print(dfs(graph, '3'))