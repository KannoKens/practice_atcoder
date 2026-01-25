Q = int(input())

volume = 0
b = False

for i in range(Q):
    A = int(input())
    
    if A == 1:
        volume = volume + 1
    elif A == 2 :
        if volume != 0:
            volume = volume - 1
    else:
        if not b:
            b = True
        else:
            b = False
    
    # print(f"volume = {volume}")

    if volume >= 3 and b:
        print("Yes")

    else:
        print("No")