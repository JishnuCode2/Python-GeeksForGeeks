arr= [2,8,5,11,14,2];

arr.sort();

is_ap = True
k = arr[0] - arr[1]

for i in range(len(arr)-1):
    if arr[i] - arr[i+1] != k:
        is_ap = False;
        break

if is_ap:
    print("Yes, an AP can be formed using this array");
else:
    print("AP not possible")