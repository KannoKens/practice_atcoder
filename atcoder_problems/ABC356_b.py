N, M = map(int, input().split())

A = list(map(int, input().split()))

totals = [0] * M

for _ in range(N):
    X = list(map(int, input().split()))
    for j in range(M):
        totals[j] += X[j]

ans="Yes"
for j in range(M):
    if totals[j] < A[j]:
        ans = "No"
        break

print(ans)