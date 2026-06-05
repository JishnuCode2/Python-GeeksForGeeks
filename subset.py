a1 = [1,5,2,7,3,62,23,5,3];
a2 = [1,2,4];

for i in a2:
    if i not in a1:
        print("not a subset");
        break;
    if i== a2[-1]:
        print("subset");