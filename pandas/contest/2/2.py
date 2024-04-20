import pandas as pd
import numpy as np

A_path = input()
b_path = input()
A = np.matrix(pd.DataFrame(pd.read_csv(A_path, sep=' ', header=None), dtype=np.float64))
b = np.matrix(pd.read_csv(b_path, sep=' ', header=None), dtype=np.float64)
X = np.matrix(list(map(np.float64, input().split())))
print((np.dot(np.dot(X, np.dot(A, A)), b.T).astype(np.float64)).item())
