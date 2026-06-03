k = 3;

arr = [6, 2, 5, 2, 2, 6, 6];

arr_unique = list(set(arr));

for el in arr_unique:
    if arr.count(el) != k:
        print(el);
        break;