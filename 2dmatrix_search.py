
matrix = [
    [1, 2],
    [4],
    [22],
    [32],
    [1,9,10,11],
    [7,8,9]
]

x = 10
ylen = len(matrix);
present = False;

for j in range(ylen):
    xlen = len(matrix[j]);
    for i in range(xlen):
        if x == matrix[j][i]:
            present = True;
            break;
    if present:
        break;

if present :
    print("true");
else :
    print("false");