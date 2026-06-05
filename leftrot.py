arr = [1,2,3,4,5,6];
k = 11;

for i in range(k):
    arr_o = arr[0];
    arr.pop(0);
    arr.append(arr_o)

print(arr);
