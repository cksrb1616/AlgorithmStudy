def countTriplets(arr, r):
    count = 0
    bef = {}
    aft = {}
    for v in arr:
        if v in aft:
            aft[v] += 1
        else:
            aft[v] = 1
            
    for v in arr:
        aft[v] -= 1
        if v//r in bef and v%r ==0 and v*r in aft:
            count += bef[v//r]*aft[v*r]
        if v in bef:
            bef[v] += 1
        else:
            bef[v] = 1
    return(count)
