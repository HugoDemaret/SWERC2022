def jarvis_march(points):
    a =  min(points, key = lambda point: point.x)
    index = points.index(a)
    l = index
    result = []
    result.append(a)
    while (True):
        q = (l + 1) % len(points)
        for i in range(len(points)):
            if i == l:
                continue
            d = direction(points[l], points[i], points[q])
            if d > 0 or (d == 0 and distance_sq(points[i], points[l]) > distance_sq(points[q], points[l])):
                q = i
        l = q
        if l == index:
            break
        result.append(points[q])
    return result