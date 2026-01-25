# 実験：数字を3桁のゼロ埋めにする
n = 45

# そのまま表示
print(f"AGC{n}")

# 魔法の呪文「:03」をつける
print(f"AGC{n:03}")

print(f"AGC{n+1 if n>=42 else n:03}")

print(f"AGC{n + (n >= 42):03}")