
s = "jnwiwffou";

arr = list(s)
print(arr);

vowels = ['a', 'i','o','u','e'];

for i in range(len(arr)-1):
    if i>0:
        if arr[i] in vowels:
            if arr[i-1] not in vowels and arr[i+1] not in vowels:
                arr.pop(i);

s= ''.join(arr);

print(s);
