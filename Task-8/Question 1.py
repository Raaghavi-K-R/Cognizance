import numpy as np
n=[]
a=np.array([0, 0, 0, 0, 0])
b=int(input("Enter First Number :"))
c=int(input("Enter Last Number :"))
for i in range(b, c+1):
      n.append(i)
      if i!=c:
       for j in a:
        n.append(j)

n=np.array(n)
print(np.float_(n))
