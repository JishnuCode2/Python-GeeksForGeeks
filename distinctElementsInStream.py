def getDistinct(arr):
    freq = {}
    distinct = 0
    ans = []

    for x in arr:
        if x > 0:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
                distinct += 1
        
        elif x < 0:
            v = -x
            if v in freq:
                if freq[v] == 1:
                    del freq[v]
                    distinct -= 1
                else:
                    freq[v] -= 1
        
        ans.append(distinct)

    return ans


arr = [2,1,3,4,0,-1,-3];

print(getDistinct(arr));