
def bellman_ford2(graph, weight, source):
    """     :complexity: `O(|V|*|E|)`"""
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0

    def relax():
        for nb_iterations in  range(n-1):
            for node in range(n):
                for neighbor in graph[node]:
                    alt = dist[node] + weight[node][neighbor]
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prec[neighbor] = node
    relax()
    intermediate = dist[:]  # is fixpoint in absence of neg cycles
    relax()
    for node in range(n):
        if dist[node] < intermediate[node]:
            dist[node] = float('-inf')
    return dist, prec, min(dist) == float('-inf')