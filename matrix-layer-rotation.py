# Complete the matrixRotation function below.
def matrixRotation(matrix, m, n, r):
    l = []
    for i in range(min((m//2),n//2)) :
        l.append(2*(m+n-2-4*i))
    for i in range(m) :
        for j in range(n) :
            small = min(m,n)
            for k in range(small//2) :
                if i == k or j == k or m-1-i == k or n-1-j == k :
                    s = l[k]
                    break
            rot = r % s
            if(j > k and j < n-k-1) :
                if i == k :
                    if(rot <= n-1-k-j) :
                        print(matrix[i][j+rot], end = " ")
                    elif (rot <= n-1-k-j+(m-(2*k)-1)) :
                        print(matrix[k+(rot-(n-k-1-j))][n-1-k], end = " ")
                    elif (rot <= n-1-k-j+(m-(2*k)-1) + ((n-2*k)-1)) :
                        print(matrix[m-k-1][n-1-k-(rot-(n-1-k-j)-(m-(2*k)-1))], end = " ")
                    elif (rot <= n-1-k-j+(2*(m-(2*k)-1)) + ((n-2*k)-1)):
                        print(matrix[m-k-1-(rot-(n-1-k-j) - (m-(2*k)-1) - (n-(2*k)-1))][k], end = " ")
                    else :
                        print(matrix[k][j-(s-rot)], end = " ")
                elif (i == m-k-1) :
                    if (rot <= j-k) :
                        print(matrix[m-k-1][j-rot],end = " ")
                    elif (rot <= j-k + m-(2*k)-1) :
                        print(matrix[m-k-1-(rot - (j-k))][k],end = " ")
                    elif (rot <= j-k + m-(2*k)-1 + (n-(2*k)-1)) :
                        print(matrix[k][k + rot-(j-k) - (m-(2*k)-1)],end = " ")
                    elif (rot <= j-k + 2*(m-(2*k)-1) + (n-(2*k)-1)):
                        print(matrix[k+rot-(j-k) - (m-(2*k)-1) - (n-(2*k)-1)][n-k-1],end = " ")
                    else :
                        print(matrix[m-k-1][j+(s-rot)],end = " ")
            elif (j==k) :
                if (rot <= i-k) :
                    print(matrix[i-rot][k],end = " ")
                elif (rot <= i-k + n-(2*k) - 1) :
                    print(matrix[k][k + rot - (i-k)],end = " ")
                elif (rot <= i-k + n-(2*k)-1 + m-(2*k)-1) :
                    print(matrix[k + rot - (i-k) - (n-(2*k)-1)][n-1-k],end = " ")
                elif (rot <= i-k + 2*(n-(2*k)-1) + m-(2*k)-1) :
                    print(matrix[m-k-1][n-1-k - (rot - (i-k) - (n-(2*k)-1) - (m-(2*k)-1))], end = " ")
                else :
                    print(matrix[i + (s-rot)][k], end = " ")
            else :
                if (rot <= m-k-1-i) :
                    print(matrix[i+rot][n-1-k],end = " ")
                elif(rot <= m-k-1-i + n-(2*k)-1) :
                    print(matrix[m-k-1][n-1-k-(rot - (m-1-k-i))],end = " ")
                elif (rot <= m-k-1-i + n-(2*k)-1 + m-(2*k)-1) :
                    print(matrix[m-k-1-(rot-(m-k-1-i) - (n-(2*k)-1))][k],end = " ")
                elif (rot <= m-k-1-i + 2*(n-(2*k)-1) + m-(2*k)-1) :
                    print(matrix[k][k+rot-(m-k-1-i) - (n-(2*k)-1) - (m-(2*k)-1)],end = " ")
                else :
                    print(matrix[i-(s-rot)][n-k-1],end = " ")
        print()
 
if __name__ == '__main__':
    mnr = input().rstrip().split()
 
    m = int(mnr[0])
 
    n = int(mnr[1])
 
    r = int(mnr[2])
 
    matrix = []
 
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
 
    matrixRotation(matrix, m,n,r)
