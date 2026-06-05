arr_1 = [5,6,7,1];
arr_2 = [1,5,9, 10];

arr_1.extend(arr_2);
arr_1 = list(set(arr_1));

arr_1.sort();

print(arr_1);