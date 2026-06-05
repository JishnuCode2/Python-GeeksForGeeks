arr = [1,2,3,4,5,6,7,8];
k = 3;

def swap():
    el_1 = arr[k-1];
    el_2 = arr[-k];

    arr[k-1] = el_2;
    arr[-k] = el_1;

swap();
print(arr);