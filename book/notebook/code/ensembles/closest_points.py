def dist(p, q):
    return hypot(p[0] - q[0], p[1] - q[1])  # Euclidean dist.
def cell(point, size):
    """ returns the grid cell coordinates containing the given point.
    size is the side length of a grid cell
    beware: in other languages negative coordinates need special care
    in C++ for example int(-1.5) == -1 and not -2 as we need
    hence we need floor(x / pas) in C++ using #include <cmath>
    """
    x, y = point                        # size = grid cell side length
    return (int(x // size), int(y // size))
def improve(S, d):
    G = {}                              # maps grid cell to its point
    for p in S:                         # for every point
        a, b = cell(p, d / 2)           # determine its grid cell
        for a1 in range(a - 2, a + 3):
            for b1 in range(b - 2, b + 3):
                if (a1, b1) in G:       # compare with points
                    q = G[a1, b1]       # in surrounding cells
                    pq = dist(p, q)
                    if pq < d:          # improvement found
                        return pq, p, q
        G[a, b] = p
    return None
def closest_points(S):
    shuffle(S)
    assert len(S) >= 2
    p = S[0]                # start with distance between
    q = S[1]                # first two points
    d = dist(p, q)
    while d > 0:            # distance 0 cannot be improved
        r = improve(S, d)
        if r:               # distance improved
            d, p, q = r
        else:               # r is None: could not improve
            break
    return p, q