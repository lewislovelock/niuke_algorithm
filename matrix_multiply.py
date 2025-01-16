def matrix_multiply():
    x = int(input())
    y = int(input())
    z = int(input())
    
    A = []
    for i in range(x):
        A.append(list(map(int, input().split())))

    B = []
    for i in range(y):
        B.append(list(map(int, input().split())))

    C = [[0] * z for _ in range(x)]
    for i in range(x):
        for j in range(z):
            for k in range(y):
                C[i][j] += A[i][k] * B[k][j]

    for row in C:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    matrix_multiply()