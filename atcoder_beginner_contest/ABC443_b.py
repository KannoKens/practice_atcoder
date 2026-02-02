N, K = map(int, input().split())

if N == K:
    print(0)
    exit()

mame = N
count = 1

while mame < K:
    mame = count + N + mame
    count += 1

print(count-1)