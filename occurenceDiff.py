arr = [1,2,2,1,5,1,2,3,3,1,1]

arr_checked = []
ar_counts = []

for i in arr :
    if i not in arr_checked:
        ar_counts.append(arr.count(i));
        arr_checked.append(i);

if len(arr_checked) > 1 :
    diff = max(ar_counts) - min(ar_counts)
    print(diff)
else:
    print(0)

        