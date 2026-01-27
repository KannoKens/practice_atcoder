import sys

H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

# print(A[0][0])

# s を 0 から H-1 まで動かす（縦のずらし量）
for s in range(H):
    # その s に対して、t を 0 から W-1 まで動かす（横のずらし量）
    for t in range(W):
        # print(f"今は縦に{s}、横に{t}ずらしてチェック中...")

        is_match = True
        for i in range(H):
            for j in range(W):
                # Aの「ずらした後の位置」と Bの「元の位置」を比べる
                if A[(i+s)%H][(j+t)%W] != B[i][j]:
                    is_match = False
                    break
            if not is_match:
                break
        
        if is_match:
            print("Yes")
            sys.exit()

print("No")
