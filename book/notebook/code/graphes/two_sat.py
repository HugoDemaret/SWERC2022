def vertex(lit):
    if lit > 0:
        return 2 * (lit - 1)
    else:
        return 2 * (-lit -1) +1
def two_sat(formula):
    n = max(abs(clause[p]) for p in (0,1) for clause in formula)
    graph = [[] for node in range(2*n)]
    for x,y in formula:
        graph[vertex(-x)].append(vertex(y))
        graph[vertex(-y)].append(vertex(x))
    sccp = kosaraju(graph)
    comp_id = [None] * (2*n)
    affectations = [None] * (2*n)
    for component in sccp:
        rep = min(component)
        for vtx in component:
            comp_id[vtx] = rep
            if affectations[vtx] == None:
                affectations[vtx] = True
                affectations[vtx ^ 1] = False
    for i in range(n):
        if comp_id[2*i] == comp_id[2*i+1]:
            return None
    return affectations[::2]

