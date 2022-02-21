from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import threading
import time
from sklearn import datasets
from scipy.spatial import ConvexHull

# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size
data = datasets.load_iris()
# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
# kolom target adalah nama2 bunga --> data.target_names = ['setosa' 'versicolor' 'virginica']
print(df.shape)
df.head()

bucket = df[df['Target'] == 0] # membagi 3 dataset iris sesuai target (0, 1, 2)
bucket = bucket.iloc[:,[0,1]].values # mengambil atribut sepal width dan length lalu menjadikannya sbg array 2 dimensi
print("sebelum:")
print(bucket[:10])
print("\n")

def bubbleSortAbsis(M):
    '''
        Mengurutkan matriks M berdasarkan absis yang teurut menaik
        menggunakan algoritma bubble sort
    '''
    for i in range(len(M)-1):
        for k in range(0, len(M)-1-i):
            if (M[k+1][0] < M[k][0] or (M[k+1][0] == M[k][0] and M[k+1][1] < M[k][1])):
                temp = M[k]
                M[k] = M[k+1]
                M[k+1] = temp

print("setelah:")
x = bucket[:10].tolist()
print(type(x[0][0] < x[0][1]))
print('\n')
bubbleSortAbsis(x)
print(x)

def partisiMatrixAbsisBased(M, i, j):
    '''
        Membagi matriks M[i][n] menjadi submatriks A[i..q][n] dan A[q+1..j][n]
        Masukan: matriks m x n dengan setiap elemennya terdiri dari 2 elemen (absis dan oordinat)
        Keluaran: submatriks A[i..q][n] dan A[q+1..j][n] dengan
                  A[i..q][n] lebih kecil dari A[q+1..j][n]
    '''
    pivot = M[(len(M) - 1) // 2][0] # ambil elemen tengah sbg pivot
    p = i
    q = j
    while True:
        while (M[p][0] < pivot):
            p += 1
        # M[p][0] >= pivot
        while (M[q][0] > pivot):
            q -= 1
        # M[p][0] >= pivot
        if (p < q):
            # swap
            temp = M[p][0]
            M[p][0] = M[q][0]
            M[q][0] = temp
            p += 1
            q -= 1
        else:
            break
    return q

def quickSortAbsis(M, i , j):
    '''
        Mengurutkan matriks M[i][n] terurut menaik menurut absisnya
        Masukan: matriks m x n dengan setiap elemennya terdiri dari 2 elemen (absis dan oordinat)
        Keluaran: matriks M[i][n] yang teurut menurut absisnya
    '''
    count = 1
    if (i < j):
        k = partisiMatrixAbsisBased(M, i, j)
        quickSortAbsis(M,i,k)
        quickSortAbsis(M,k + 1,j)

