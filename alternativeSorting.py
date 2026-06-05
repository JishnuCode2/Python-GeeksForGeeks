arr = [1, 6, 9, 4, 3];
max_arr = [];
min_arr = [];

while True:
    if len(arr) > 1:
        M = max(arr);
        m = min(arr);

        max_arr.append(M);
        min_arr.append(m);

        arr.remove(M);
        arr.remove(m);
    elif len(arr) <= 1:
        break;

fin_arr = []
l = len(max_arr) + len(min_arr);

for n in range(l):
    if n%2 == 0:
        fin_arr.append(max_arr[ int(n/2) ]);
    if n%2 == 1:
        fin_arr.append(min_arr[ int((n-1)/2) ]);

if len(arr) == 1:
    fin_arr.append(arr[0]);

print(fin_arr);