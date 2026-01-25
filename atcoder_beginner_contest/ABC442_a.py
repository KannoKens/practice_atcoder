S = input()

s = list(S)
count = 0
#print(s)

for i in s:
    if i == "i" or i == "j":
        count = count + 1
    
print (count)