L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in L:
    if i % 2 == 0:
        L.remove(i)
print(L)