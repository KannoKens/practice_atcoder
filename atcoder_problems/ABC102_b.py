N = int(input())
A = list(map(int,input().split()))

ans = abs(max(A) - min(A))
print(ans)

# print(max(A)-min(A))