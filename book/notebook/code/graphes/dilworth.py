def dilworth(graph):
    n = len(graph)
    match = max_bipartite_matching(graph)  # maximum matching
    part = [None] * n                      # partition into chains
    nb_chains = 0
    for v in range(n - 1, -1, -1):         # in inverse topological order
        if part[v] is None:                # start of chain
            u = v
            while u is not None:           # follow the chain
                part[u] = nb_chains        # mark
                u = match[u]
            nb_chains += 1
    return part