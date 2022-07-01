
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

def bfs(value: int):
    keys = list(graph.keys())
    firstKey = keys[0]
    childs = graph[firstKey]

    print(childs)


if __name__ == "__main__":
    bfs(4)