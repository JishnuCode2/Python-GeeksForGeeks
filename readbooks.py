k = 10

min_i = [1,6,3,2,7,2,3,4];

points_i = [1,10,3,4,7,6,5,5];

rew = []

for i in range(len(min_i)):
    rew.append((k//min_i[i]) * points_i[i]);

print(max(rew));