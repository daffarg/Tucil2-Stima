def partisiMatrixAbsisBased(M, i, j):
    '''
        Membagi matriks M[i][n] menjadi submatriks A[i..q][n] dan A[q+1..j][n]
        Masukan: matriks m x n dengan setiap elemennya terdiri dari 2 elemen (absis dan oordinat)
        Keluaran: submatriks A[i..q][n] dan A[q+1..j][n] dengan
                  A[i..q][n] lebih kecil dari A[q+1..j][n]
    '''
    pivot = M[i][0] # ambil elemen pertama sbg pivot
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
    if (i < j):
        k = partisiMatrixAbsisBased(M, i, j)
        quickSortAbsis(M,i,k-1)
        quickSortAbsis(M,k + 1,j)

def bubbleSortAbsis(M, isInc):
    '''
        Mengurutkan matriks M berdasarkan absis yang teurut menaik
        menggunakan algoritma bubble sort
        Jika ada nilai absis yang sama, maka diurutkan dengan nilai ordinat yang menaik
    '''
    for i in range(len(M)-1):
        for k in range(0, len(M)-1-i):
            if (isInc):
                test = M[k+1][0] < M[k][0] or (M[k+1][0] == M[k][0] and M[k+1][1] < M[k][1])
            else:
                test = M[k+1][0] > M[k][0] or (M[k+1][0] == M[k][0] and M[k+1][1] > M[k][1])
            if (test):
                temp = M[k]
                M[k] = M[k+1]
                M[k+1] = temp

