arr = [7,98,56,43,45,23,12,8, 11];
k = 54;

req = []

for i in arr:
    if i<k and i>=10:
        req.append(i);

print(req);

for num in req:
    li = list(str(num));

    for i in range(len(li)-1):
        if abs(int(li[i]) - int(li[i+1])) != 1:
            req.remove(num);
            break;

print(req);
