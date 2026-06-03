import copy

arr = [0,1,4,2];

t = False;

for i in range(len(arr)):
    for j in range(len(arr)):
        arr_n = copy.deepcopy(arr);
        arr_n.pop(i);
        arr_n.pop(j-1);

        if arr[i]+arr[j] in arr_n and i !=j:
            t = True
            print(t);
            break;
    if t:
        break;

if not t :
    print(t);



