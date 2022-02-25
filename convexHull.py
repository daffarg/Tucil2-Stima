from sort import bubbleSortAbsis

def checkPointPosition(p1, p2, p3):
    '''
        p1, p2, p3 adalah matriks dgn 2 elemen (elemen pertama absis, elemen kedua oordinat)
        Mengembalikan 1 jika titik p3 berada di sebelah
        kiri atau atas garis yg dibentuk oleh p1 dan p2,
        -1 jika di bawahnya, 0 jika tepat pada garis
    '''

    det = (p3[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
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

def convexHull(M, p1, p2, points, side):
    '''
        Prosedur rekursif untuk mencari titik2 yg membentuk convex hull
        Menerima masukan array of titik M, titik p1 dan p2 sbg titik ekstrem,
        Titik2 hasil disimpan dalam points, side menentukan bagian yg
        dihitung (bernilai 1 jika sisi kiri atau -1 jika sisi kanan)

    '''
    max = 0
    max_point = [-999,-999]
    for point in M:
        dist = distanceBetweenLineAndPoint(p1, p2, point)
        if (dist > max):
            max = dist
            max_point = point

    if (max == 0): # tidak ditemukan titik lagi 
        if (p1 not in points):
            points.append(p1)
        if (p2 not in points):
            points.append(p2)
        return

    # Pembagian titik2 ke dalam dua sisi 
    if side == 1:
        side1 = getLeftSide(M, p1, max_point)
        side2 = getLeftSide(M, max_point, p2)
    else:
        side1 = getRightSide(M, p1, max_point)
        side2 = getRightSide(M, max_point, p2)

    # rekurens untuk pada dua sisi yang terbentuk akibat pembagian 
    convexHull(side1,p1,max_point,points,side)
    convexHull(side2,max_point,p2,points,side)

def findConvexHull(M):
    '''
        Menerima masukan array of titik yg ingin dicari convex hull-nya. 
        Mengembalikan array of titik yg membentuk convex hull dari array of titik M
    '''
    bubbleSortAbsis(M, True)
    points = []
    leftSide = getLeftSide(M, M[0], M[len(M)-1])
    rightSide = getRightSide(M, M[0], M[len(M)-1])

    # penerapan Divide & Conquer menentukan titik2 pada sisi atas (kiri) atau bawah (kanan)
    convexHull(leftSide, M[0], M[len(M)-1], points, 1) # sisi atas (kiri)
    convexHull(rightSide, M[0], M[len(M)-1], points, -1) # sisi bawah (kanan)
    bubbleSortAbsis(points, True)

    # Penyusunan dan pengurutan ulang array of titik hasil convex hull untuk diplot  
    p = points[0]
    q = points[len(points)-1]
    leftSide = getLeftSide(points, p, q) # titik2 yg berada di kiri (atau atas) garis yg dibentuk oleh p dan q
    rightSide = getRightSide(points, p, q) # titik2 yg berada di kanan (atau bawah) garis yg dibentuk oleh p dan q
    rightSide = rightSide + [p, q]
    bubbleSortAbsis(rightSide,True)
    bubbleSortAbsis(leftSide,False)
    result = rightSide + leftSide
    result.append(result[0]) # penambahan dgn elemen pertama untuk kebutuhan plotting
    return result