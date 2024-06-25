import numpy as np
from numpy import linalg


v=np.array([1,2,3])
print(v)

m=np.array([[1,2,3],[0,1,4],[5,6,0]])

print(m)
print(m[0,0])

print(v@m)

m_inv= linalg.inv(m)
print(m_inv)

print(m@m_inv)