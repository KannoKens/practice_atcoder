N = int(input())
ans = 0
current_L = -1
current_R = -1

for i in range(N):
    line = input().split()
    A = int(line[0])
    S = line[1]

    if S == "L":
        if current_L != -1:
            ans += abs(A - current_L)
        
        current_L = A
    
    else:
        if current_R != -1:
            ans += abs(A - current_R)

        current_R = A

print(ans)
