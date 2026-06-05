arr= [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
k = 5

val = arr[k];

arr_sorted = sorted(arr);

num_of_same_before_k = 0;

for i in range(k):
    if arr[i] == val:
        num_of_same_before_k+=1;


#For General
# for i in range(len(arr)):
#     for j in range(len(arr_sorted)):
#         if arr[i] == arr_sorted[j]:
#             print("Match:", i, arr[i], j, arr_sorted[j]);

#For Given k
new_before = 0;
for i in range(len(arr_sorted)):
    
    if arr[k] == arr_sorted[i] and new_before == num_of_same_before_k:
        print(i)

    if arr_sorted[i] == val:
        new_before += 1;
