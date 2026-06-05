arr = [1, 6, 7, 4];
l = 1;
r = 4;

arr_bef = arr[:l-1];
arr_r = arr[l-1:r];
arr_r = arr_r[::-1];
arr_aft = arr[r:];

print(arr_bef, arr_r, arr_aft);

arr_f = arr_bef;

arr_f.extend(arr_r)
arr_f.extend(arr_aft);

print(arr_f);