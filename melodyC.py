arr = [2,5,6,7,1,3];
arr_m = []

for i in range(len(arr)-1):
    arr_m.append(arr[i] + arr[i+1]);

print(max(arr_m));