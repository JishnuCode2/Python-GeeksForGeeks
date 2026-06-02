arr= [2,9,7,5,6,3,6];

while True:
    first = arr[0];
    last = arr[-1];

    if first > last or first==last:
        arr.pop(0);
    elif first < last:
        arr.pop(-1);

    if len(arr) == 1:
        break;

print(arr);