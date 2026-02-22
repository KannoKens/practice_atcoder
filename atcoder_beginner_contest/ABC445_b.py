N = int(input())
list_S = [input() for _ in range(N)]
x = max([len(i) for i in list_S])

for s in list_S:
    if x - len(s) == 0:
        print(s)
    else:
        a = (x - len(s))//2
        b = "."* a + s + "." * a
        print(b)