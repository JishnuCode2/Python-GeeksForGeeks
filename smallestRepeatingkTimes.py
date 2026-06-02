arr = [2,5,1,2,5,3,1,7,9];
k = 2;

ar_checked = [];
ar_noc = [];

ar_k = [];

for i in arr:
    if i not in ar_checked:
        ar_checked.append(i);
        ar_noc.append(arr.count(i));

print(ar_noc)
print(ar_checked)

for j in ar_checked:
    if ar_noc[ar_checked.index(j)] == k:
        ar_k.append(j);

min_matching_el = min(ar_k);

print("The Minimum Element Repeating k times is: ", min_matching_el);
