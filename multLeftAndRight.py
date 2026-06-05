arr = [1,2,3,4,5];

size = len(arr);

arr_left = arr[:size//2];
arr_right = arr[size//2:];

s_l = sum(arr_left);
s_r = sum(arr_right);

print(s_l * s_r);