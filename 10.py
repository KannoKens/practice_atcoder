# A - Health M Death
M, H = map(int, input().split())

if H % M == 0:
    print("Yes")
else:
    print("No")

#　別解
#print("Yes" if H % M == 0 else "No")