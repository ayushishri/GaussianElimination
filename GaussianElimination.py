def ge_bw(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    if rows!=cols:
        return -1
    for i in range(rows-1,-1,-1):
        if (matrix[i][cols-1]!=0):
            temp=matrix[cols-1]
            matrix[cols-1]=matrix[i]
            matrix[i]=temp
            break
    for k in range(1,rows,1):
        for j in range (rows-k-1,-1,-1):
            temp=float(matrix[j][cols-k])/(matrix[rows-k][cols-k])
            for i in range(cols-k,-1,-1):
                matrix[j][i]=float(matrix[j][i])-temp*matrix[rows-k][i]
    print matrix
    return 0




def ge_fw(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    if rows!=cols:
        return -1
    for i in range(0,rows,1):
        if (matrix[i][0]!=0):
            temp=matrix[0]
            matrix[0]=matrix[i]
            matrix[i]=temp
            break
    for k in range (1,rows,1):
        for j in range (k,rows,1):
            temp=float(matrix[j][k-1])/(matrix[k-1][k-1])
            for i in range(k-1,cols,1):
                matrix[j][i]=float(matrix[j][i])-temp*matrix[k-1][i]
    print matrix
    return 0
