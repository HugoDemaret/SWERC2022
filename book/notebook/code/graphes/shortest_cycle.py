def path(tree, v):
    P = []
    while not P or P[-1] != v:
        P.append(v)
        v = tree[v]
    return P
def shortest_cycle(graph):
    best_cycle = float('inf')
    best_u = None
    best_v = None
    best_tree = None
    V = list(range(len(graph)))
    for root in V:
        tree, cycle_len, u, v = bfs(graph, root, best_cycle // 2)
        if cycle_len < best_cycle:
            best_cycle = cycle_len
            best_u = u
            best_v = v
            best_tree = tree
    if best_cycle == float('inf'):
        return None                   # no cycle found
    Pu = path(best_tree, best_u)      # combine path to make a cycle
    Pv = path(best_tree, best_v)
    cycle = Pu[::-1] + Pv   # last vertex equals first vertex
    return cycle[1:]        # remove duplicate vertex
def powergraph(graph, k):
    V = range(len(graph))
    # create weight matrix for paths of length 1
    M = [[float('inf') for v in V] for u in V]
    for u in V:
        for v in graph[u]:
            M[u][v] = M[v][u] = 1
        M[u][u] = 0
    floyd_warshall(M)
    return [[v for v in V if M[u][v] <= k] for u in V]