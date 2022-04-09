def floyd_warshall(weight):
    """"O(|V|^3)"""
    for k, Wk in enumerate(weight):
        for _, Wu in enumerate(weight):
            for v, Wuv in enumerate(Wu):
                alt = Wu[k] + Wk[v]
                if alt < Wuv:
                    Wu[v] = alt
    for v, Wv in enumerate(weight):
        if Wv[v] < 0:      # negative cycle found
            return True
    return False