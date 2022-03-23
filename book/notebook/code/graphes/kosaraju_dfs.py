def kosaraju_dfs(graph,nodes,order,sccp):
    times_seen = [-1] * len(graph)
    for start in nodes:
        if times_seen[start]  == -1:
            to_visit = [start]
            times_seen[start] = 0
            sccp.append([start])
            while to_visit:
                node = to_visit[-1]
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    order.append(node)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        times_seen[child] = 0
                        to_visit.append(child)
                        sccp[-1].append(child)
def reverse(graph):
    rev_graph = [[] for node in graph]
    for node in range(len(graph)):
        for neighbour in graph[node]:
            rev_graph[neighbour].append(node)
    return rev_graph
def kosaraju(graph):
    n = len(graph)
    order = []
    sccp = []
    kosaraju_dfs(graph, range(n), order, [])
    kosaraju_dfs(reverse(graph),order[::-1], [], sccp)
    return sccp[::-1]