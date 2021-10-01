m, n, r = map(int, input().split())
matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().split())))

nooflayers = min(m, n)//2
a = []
for i in range(nooflayers):
    b = []
    noofelements = 2*(m+n-(4*i)-2)
    m_temp = i
    for j in range(i, n-i-1):
        b.append(matrix[m_temp][j])
    n_temp = n-i-1
    for j in range(i, m-i-1):
        b.append(matrix[j][n_temp])
    m_temp = m-i-1
    for j in range(n-i-1, i, -1):
        b.append(matrix[m_temp][j])
    n_temp = i
    for j in range(m-i-1, i, -1):
        b.append(matrix[j][n_temp])
    a.append(b)
    # print(a[i])
    noofr = r % noofelements
    a[i] = a[i][noofr:]+a[i][:noofr]
    # print(a[i])
    m_temp = i
    count = 0
    for j in range(i, n-i-1):
        # b.append(matrix[m_temp][j])
        matrix[m_temp][j] = a[i][count]
        # print(count,a[count])
        count += 1

    n_temp = n-i-1
    for j in range(i, m-i-1):
        # b.append(matrix[j][n_temp])
        matrix[j][n_temp] = a[i][count]
        # print(count,a[count])
        count += 1

    m_temp = m-i-1
    for j in range(n-i-1, i, -1):
        # b.append(matrix[m_temp][j])
        matrix[m_temp][j] = a[i][count]
        # print(count,a[count])
        count += 1

    n_temp = i
    for j in range(m-i-1, i, -1):
        # b.append(matrix[j][n_temp])
        matrix[j][n_temp] = a[i][count]
        # print(count,a[count])
        count += 1

for l in range(m):
    for k in range(n):
        print(matrix[l][k], end=" ")
    print()
