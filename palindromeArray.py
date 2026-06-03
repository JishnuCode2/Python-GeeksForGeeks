arr = [111, 222, 333, 555];

for num in arr:
    s = str(num);
    s_rev = s[::-1];

    if s != s_rev:
        print(False);
        break;

    if num == arr[-1]:
        print(True);

