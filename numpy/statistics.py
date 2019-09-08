import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.max(stats, axis = 1)) 
print(np.min(stats, axis= 0))

# 0 la hang - 1 la cot