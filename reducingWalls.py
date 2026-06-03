arr = [1,5,11,54, 21];
k = 5;

numOfOps = 0;

for n in arr:
    if n > k:
        while n > k:
            n -= k;
            numOfOps += 1;

print(numOfOps)

numOfOps = 0;

for n in arr:
    if n>k:
        numOfOps += n//k;

print(numOfOps);