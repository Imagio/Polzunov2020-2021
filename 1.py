import itertools
i = int(input())
a = list(itertools.permutations([str(i) for i in range(0,i)],2))
print(len(a))
for item in a:
    print(" ".join(list(item)))
