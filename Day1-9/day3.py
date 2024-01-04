with open("day3.txt", "r") as data:
    tri_list = [list(map(int, line.split())) for line in data]

diff_tri_list = [
    [tri_list[i + x][y] for x in range(3)]
    for i in range(0, len(tri_list), 3)
    for y in range(3)
]

possible = 0
for tri in tri_list:
    tri.sort()
    if tri[0] + tri[1] > tri[2]:
        possible += 1

vert_poss = 0
for i in diff_tri_list:
    i.sort()
    if i[0] + i[1] > i[2]:
        vert_poss += 1

print(possible, vert_poss)
