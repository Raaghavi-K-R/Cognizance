import numpy as np
a=np.array([1, 0, 0, 0, 1, 0])
print("First array :", a)
b=np.array([0, 0, 1, 1, 0, 1])
print("Second Array :", b)
c= a==b
for i in range(0,a.__len__()):
    if a[i]==b[i]:
        c=True
    else:
        c=False
        break
print(c)
