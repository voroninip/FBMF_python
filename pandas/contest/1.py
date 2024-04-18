import pandas as pd
import numpy as np

N, M = list(map(int, input().split()))
arr = np.ndarray(shape=(N, M), dtype=int)
for i in range(N):
    arr[i] = list(map(int, input().split()))

df = pd.DataFrame(arr)
print(df[df < -5].notna().sum().sum())
print(int(abs(df[df < 0].sum().sum())))
print(int(df.max().max()))