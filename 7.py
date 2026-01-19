#A - Maxi-Buying
n = int(input())

price=int(n * 1.08)

#計算の確認
#print(price)

if price<206:
    print("Yay!")
elif price==206:
    print("so-so")
else:
    print(":(")

#簡略版
#print("Yay!" if price < 206 else "so-so" if price == 206 else ":(")