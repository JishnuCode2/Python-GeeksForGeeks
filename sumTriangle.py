arr= [4,7,3,6,7];


l = len(arr);
arr_pyramid = [];
arr_pyramid.append(arr);

for i in range(l):
    arr_i = []
    for j in range(len(arr)-1):
        arr_i.append(arr[j] + arr[j+1]);
    arr = arr_i;
    arr_pyramid.append(arr_i);

arr_pyramid = arr_pyramid[::-1];

arr_pyramid = arr_pyramid[1:];

print(arr_pyramid);

