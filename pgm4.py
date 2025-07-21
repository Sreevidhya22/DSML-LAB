import numpy as np
a1=np.array([[2,5,8,10],[3,4,6,9]])
sum_all=np.sum(a1)
sum_row=np.sum(a1,axis=1)
sum_col=np.sum(a1,axis=0)
print("sum of all elements:",sum_all)
print("sum of each row:",sum_row)
print("sum of each column:",sum_col)
