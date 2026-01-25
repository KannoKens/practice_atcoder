PQ=[]
XY=[]
a = [list(map(int,input().split())) for _ in range(2)]
for i in range(2):
  PQ.append(a[i][0])
  XY.append(a[i][1])
  
P_b = PQ[0]+100
Q_b = XY[0]+100
print(PQ)
print(XY)
if PQ[0]<=PQ[1]<P_b and XY[0]<=XY[1]<Q_b:
  print("Yes")
else:
  print("No")