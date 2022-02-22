from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.spatial import ConvexHull
from sort import bubbleSortAbsis, quickSortAbsis

#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size
data = datasets.load_iris()
# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
# kolom target adalah nama2 bunga --> data.target_names = ['setosa' 'versicolor' 'virginica']

def checkPointPosition(p1, p2, p3):
    '''
        p1, p2, p3 adalah matriks dgn 2 elemen (elemen pertama absis, elemen kedua oordinat)
        Mengembalikan 1 jika titik p3 berada di sebelah
        kiri atau atas garis yg dibentuk oleh p1 dan p2,
        -1 jika di bawahnya, 0 jika tepat pada garis
    '''

    det = p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]
    if (det > 0):
        return 1
    elif (det < 0):
        return -1
    else:
        return 0

def distanceBetweenLineAndPoint(p1, p2, p3):
    '''
        p1, p2, p3 adalah matriks dgn 2 elemen (elemen pertama absis, elemen kedua oordinat)
        Mengembalikan nilai yg sebanding dgn jarak antara titik p3
        dgn garis yg dibentuk oleh titik p1 dan p2. Pembilang dlm
        rumus asli perhitungan ini diabaikan sehingga yg dihitung hanya
        penyebutnya.
    '''
    return abs((p2[0]-p1[0])*(p1[1]-p3[1])-(p1[0]-p3[0])*(p2[1]-p1[1]))

def getLeftSide(M, p1, p2):
    '''
        Mendapatkan titik2 yang berada di kiri garis
        yg dibentuk oleh p1 dan p2
    '''
    leftSide = []
    for point in M:
        if checkPointPosition(p1,p2,point) == 1:
            leftSide.append(point)
    return leftSide

def getRightSide(M, p1, p2):
    '''
        Mendapatkan titik2 yang berada di kanan garis
        yg dibentuk oleh p1 dan p2
    '''
    rightSide = []
    for point in M:
        if checkPointPosition(p1,p2,point) == -1:
            rightSide.append(point)
    return rightSide

def convexHull(M, p1, p2, simplices, side):
    # menemukan titik dgn jarak terjauh dari garis p1 dan p2
    # cek semua titik untuk memastikan tidak ada titik yang sama
    #isUnique = len(M) == len(set(M))
    max = 0
    max_point = [-999,-999]
    for point in M:
        dist = distanceBetweenLineAndPoint(p1, p2, point)
        if (dist > max):
            max = dist
            max_point = point

    if (max == 0): # tidak ditemukan titik lagi 
        if (p1 not in simplices):
            simplices.append(p1)
        if (p2 not in simplices):
            simplices.append(p2)
        return

    if side == 1:
        side1 = getLeftSide(M, p1, max_point)
        side2 = getLeftSide(M, max_point, p2)
    else:
        side1 = getRightSide(M, p1, max_point)
        side2 = getRightSide(M, max_point, p2)

    convexHull(side1,p1,max_point,simplices,side)
    convexHull(side2,max_point,p2,simplices,side)

def findConvexHull(M):
    # quickSortAbsis(M, 0, len(M)-1)
    bubbleSortAbsis(M)
    simplices = []
    leftSide = getLeftSide(M, M[0], M[len(M)-1])
    rightSide = getRightSide(M, M[0], M[len(M)-1])
    convexHull(leftSide, M[0], M[len(M)-1], simplices, 1) # sisi atas
    convexHull(rightSide, M[0], M[len(M)-1], simplices, -1) # sisi bawah
    print(simplices)

bucket = df[df['Target'] == 0] # membagi 3 dataset iris sesuai target (0, 1, 2)
bucket = bucket.iloc[:,[0,1]].values # mengambil atribut sepal width dan length lalu menjadikannya sbg array 2 dimensi

#findConvexHull(bucket.tolist())