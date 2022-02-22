from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import threading
import time
from sklearn import datasets
from scipy.spatial import ConvexHull

#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size
data = datasets.load_iris()
# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
# kolom target adalah nama2 bunga --> data.target_names = ['setosa' 'versicolor' 'virginica']
print(df.shape)
df.head()

bucket = df[df['Target'] == 0] # membagi 3 dataset iris sesuai target (0, 1, 2)
bucket = bucket.iloc[:,[0,1]].values # mengambil atribut sepal width dan length lalu menjadikannya sbg array 2 dimensi
# print("sebelum:")
# print(bucket[:10])
# print("\n")

def bubbleSortAbsis(M):
    '''
        Mengurutkan matriks M berdasarkan absis yang teurut menaik
        menggunakan algoritma bubble sort
        Jika ada nilai absis yang sama, maka diurutkan dengan nilai ordinat yang menaik
    '''
    for i in range(len(M)-1):
        for k in range(0, len(M)-1-i):
            if (M[k+1][0] < M[k][0] or (M[k+1][0] == M[k][0] and M[k+1][1] < M[k][1])):
                temp = M[k]
                M[k] = M[k+1]
                M[k+1] = temp

# print("setelah:")
# x = bucket[:10].tolist()
# print(type(x[0][0] < x[0][1]))
# print('\n')
# bubbleSortAbsis(x)
# print(x)

def checkPointPosition(x1, y1, x2, y2, x3, y3):
    '''
        Mengembalikan true jika titik r(x3,y3) berada di sebelah
        kiri atau atas garis yg dibentuk oleh p(x1,y1) dan q(x2,y2),
        false jika tidak
    '''

    det = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3
    if (det > 0):
        return True
    else:
        return False


def partisiMatrixAbsisBased(M, i, j):
    '''
        Membagi matriks M[i][n] menjadi submatriks A[i..q][n] dan A[q+1..j][n]
        Masukan: matriks m x n dengan setiap elemennya terdiri dari 2 elemen (absis dan oordinat)
        Keluaran: submatriks A[i..q][n] dan A[q+1..j][n] dengan
                  A[i..q][n] lebih kecil dari A[q+1..j][n]
    '''
    pivot_index = i
    pivot = M[i][0] # ambil elemen tengah sbg pivot
    
    while i < j:
        while i < len(M) and M[i][0] <= pivot:
            i += 1
        # while (M[p][0] < pivot):
        #     p += 1
        # # M[p][0] >= pivot
        # while (M[q][0] > pivot):
        #     q -= 1
        # # M[p][0] >= pivot
        while M[j][0] > pivot:
            j -= 1
        if(i < j):
            M[i], M[j] = M[j], M[i]
        # while M[j][0] > pivot:
        #     j -= 1
        # if (p <= q):
        #     # swap
        #     temp = M[p]
        #     M[p] = M[q]
        #     M[q] = temp
        #     p += 1
        #     q -= 1
        # else:
        #     break
    M[j], M[pivot_index] = M[pivot_index], M[j]

    return j

def partisiMatrixAbsisBased2(M, i, j):
    '''
        Membagi matriks M[i][n] menjadi submatriks A[i..q][n] dan A[q+1..j][n]
        Masukan: matriks m x n dengan setiap elemennya terdiri dari 2 elemen (absis dan oordinat)
        Keluaran: submatriks A[i..q][n] dan A[q+1..j][n] dengan
                  A[i..q][n] lebih kecil dari A[q+1..j][n]
    '''
    pivot = M[i][0] # ambil elemen tengah sbg pivot
    pivot_y = M[i][1]
    p = i
    q = j + 1

    count = 1
    
    while True:
        while True:
            p = p + 1
            if (M[p][0] > pivot or (M[p][0] == pivot and M[p][1] >= pivot_y)):
                break
        while True:
            q = q - 1
            if (M[q][0] < pivot or (M[q][0] == pivot and M[q][1] <= pivot_y)):
                break
        M[p], M[q] = M[q], M[p]
        if p >= q:
            break
    M[p], M[q] = M[q], M[p]
    M[i], M[q] = M[q], M[i]

    return q    

def quickSortAbsis(M, i , j):
    '''
        Mengurutkan matriks M[i][n] terurut menaik menurut absisnya
        Masukan: matriks m x n dengan setiap elemennya terdiri dari 2 elemen (absis dan oordinat)
        Keluaran: matriks M[i][n] yang teurut menurut absisnya
    '''
    count = 1
    if (i < j):
        k = partisiMatrixAbsisBased2(M, i, j)
        quickSortAbsis(M,i,k-1)
        quickSortAbsis(M,k + 1,j)

x = bucket[:10].tolist()
print("Sebelum: ", x)
quickSortAbsis(x, 0, len(x)-1)
print("Setelah: ", x)