import pandas as pd
import numpy as np
from prepare_data import build_table

def least_squares(df):
    #1. Construct matrix X = [0, 30, 60, 90, 120]
    #2. Construct matrix Y = [61.0, 80.0, 62.0, 83.0, 68.0]
    #3. Transpose matrix X
    #4. Multiply matrix X by matrix from step 3
    #5. Multiply matrix Y by matrix from step 3
    #6. Inverse matrix from step 4
    #7. Mutiply matrix from step 6 with step 5
    
    x = build_x_matrix(df)
    y = build_y_matrix(df, 0)
    xT = transpose_matrix
    return

def build_y_matrix(df, column):
    y = df.iloc[:, column]
    return y.to_numpy()

def build_x_matrix(df):
    x = df.index
    df = pd.DataFrame({'0': [1, 1, 1, 1, 1], '1': x})
    return df.to_numpy()

# Reference
# pg 378 section 6.3.1
# The transpose of the m x n matrix A = a_ij is the n x m matrix A^T = b_ij in which b_ij = a_ji
def transpose_matrix(A):
    m, n = A.shape
    A_T = np.empty((n, m))
    for i in range(m):
        for j in range(n):
            A_T[j, i] = A[i, j]
    return A_T    
    
# Reference
# pg 381 section 6.3.2
# Fact 6: The ij^th element of product C = AB is the scalar product of row i of A and column j of B
def dot_product(A,B):
    return

# Reference
# pg 387 section 6.3.4 Determinants 
# det ([a b]
#      [c d])
# = ad-bc
def matrix_inversion(A):
    return
