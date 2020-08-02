#-----------------------------
# Make rows and columns Zero
#-----------------------------

def zero_matrix(a):
    m = len(a)
    n = len(a[0])

    rowHasZero = []
    colHasZero = []

    for i in range(m):
        for j in range(n):
            if(a[i][j]==0):
                rowHasZero.append(i)
                colHasZero.append(j)

    for row in rowHasZero:
        nullify_rows(a,row)

    for col in colHasZero:
        nullify_cols(a,col)

    return a

def nullify_rows(a,row):
    for i in range(len(a[0])):
        a[row][i] = 0

def nullify_cols(a,col):
    for i in range(len(a)):
        a[i][col] = 0

def main():

    a = [
           [2,3,4,5,6],
           [5,6,8,9,10],
           [5,6,8,6,10],
           [5,6,4,9,10],
           [5,0,8,9,10]
         ]
    a = zero_matrix(a)
    print(a)

if __name__ == '__main__':
    main()