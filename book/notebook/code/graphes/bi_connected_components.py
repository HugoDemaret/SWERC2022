def cut_nodes_edges(graph):
    n = len(graph)
    time = 0
    num = [None] * n
    low = [n] * n
    parent = [None] * n        # parent[v] = None if root else parent of v
    critical_children = [0] * n  # cc[u] = #{children v | low[v] >= num[u]}
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:               # init DFS path
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                if times_seen[node] == 0:         # start processing
                    num[node] = time
                    time += 1
                    low[node] = float('inf')
                children = graph[node]
                if times_seen[node] == len(children):  # end processing
                    to_visit.pop()
                    up = parent[node]            # propagate low to parent
                    if up is not None:
                        low[up] = min(low[up], low[node])
                        if low[node] >= num[up]:
                            critical_children[up] += 1
                else:
                    child = children[times_seen[node]]   # next arrow
                    times_seen[node] += 1
                    if times_seen[child] == -1:   # not visited yet
                        parent[child] = node      # link arrow
                        times_seen[child] = 0
                        to_visit.append(child)    # (below) back arrow
                    elif num[child] < num[node] and parent[node] != child:
                        low[node] = min(low[node], num[child])
    cut_edges = []
    cut_nodes = []                                # extract solution
    for node in range(n):
        if parent[node] is None:                  # characteristics
            if critical_children[node] >= 2:
                cut_nodes.append(node)
        else:                                     # internal nodes
            if critical_children[node] >= 1:
                cut_nodes.append(node)
            if low[node] >= num[node]:
                cut_edges.append((parent[node], node))
    return cut_nodes, cut_edges