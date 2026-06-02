arr = [3,5,6,16,4,27,14,22,7,1];
k = 8

smaller = [];
larger = [];

arr.sort();

for i in arr:
    if i<=k:
        smaller.append(i);

    if i>=k:
        larger.append(i);

print("No. of Smaller Elements: ", len(smaller))
print("No. of Larger Elements: ", len(larger))