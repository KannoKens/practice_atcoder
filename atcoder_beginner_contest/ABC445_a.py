S = input()

for i,v in enumerate(S):
    if i == 0:
        a = v
    if i == len(S) - 1:
        b = v

if a == b:
    print("Yes")
else:
    print("No")
