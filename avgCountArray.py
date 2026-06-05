arr = [2,4,8,6,2];
x = 2;

avg_arr = []

for i in arr:
    avg = int((i+x)/2);
    avg_arr.append(arr.count(avg));


print(avg_arr);
