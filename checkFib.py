import math

num = int(input("Enter a number"));

def check_sqrt(n):
    sqrt = math.isqrt(n);

    return sqrt*sqrt == n;

x1 = 5 * num * num + 4;
x2 = 5 * num * num - 4;

print(check_sqrt(x1) or check_sqrt(x2));
