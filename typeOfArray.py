""" You are given an array arr[] having unique elements. Your task is to return the type of array described below.

Return 1 if the array is in ascending order. 
Return 2 if the array is in descending order
Return 3 if the array is in descending rotated order
Return 4 if the array is in ascending rotated order """

arr = [1,3,2];

arr_sorted = sorted(arr)

if arr == arr_sorted:
    print("1");
elif arr[::-1] == arr_sorted:
    print("2");
else:
    for i in range(len(arr)):
        arr_0 = arr[0];
        arr.pop(0);
        arr.append(arr_0);

        if arr == arr_sorted:
            print("3");
            break;
        elif arr == arr_sorted[::-1]:
            print("4");
            break;