num = 30025010;

def zero_to_five(n):
    li = list(str(n));
    for i in range(len(li)):
        if li[i] == '0':
            li[i] = '5';

    n = int("".join(li));
    return n;

print(zero_to_five(num));

