#A - Century
N=int(input())

a= N%100
if a==0:
    print(N//100)
else:
    print(N//100 + 1)

# 別解
# print((N-1)//100 + 1)
# print((N+99)//100)