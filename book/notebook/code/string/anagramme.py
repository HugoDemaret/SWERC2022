def anagrams(w):
    w = list(set(w)) #retire les doublons
    d = {}
    for i in range(len(w)):
        s = ''.join(sorted(w[i]))
        if s in d:
            d[s].append(i)
        else:
            d[s] = [i]
    answer = []
    for s in d:
        if len(d[s]) > 1:
            answer.append([w[i] for i in d[s]])
    return answer

