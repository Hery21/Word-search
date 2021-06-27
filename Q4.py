def word_find():
  T = int(input())
  C = []

  for _ in range(T):
    N = int(input())
    M = int(input())
    matx = [[str(j) for j in input()[:M]] for i in range(N)]
    W = str(input())
    
    #matriks horizontal
    hor = ["" for _ in range(N)]
    #matriks vertikal
    ver = ["" for _ in range(M)]
    #matriks diagonal
    dia1 = ["" for _ in range(N + M - 1)]
    dia2 = ["" for _ in range(len(dia1))]

    #matriks masukan dipetakan pada masing-masing matriks horizontal, vertikal, dan diagonal
    for i in range(M):
      for j in range(N):
        hor[j] += matx[j][i]
        ver[i] += matx[j][i]
        dia1[i + j] += matx[j][i]
        dia2[i - j + N - 1] += matx[j][i]

    dia = dia1 + dia2

    hor = hor + [k[::-1] for k in hor]
    ver = ver + [k[::-1] for k in ver]
    dia = dia + [k[::-1] for k in dia]

    X = 0

    if len(W) == 1:
      for i in filter(lambda l:W in l, hor):
        X += sum(1 for j in range(len(i)) if i.startswith(W, j))
      C.append(X/2)
    else:
      for i in filter(lambda l:W in l, hor):
        X += sum(1 for j in range(len(i)) if i.startswith(W, j))
      for i in filter(lambda l:W in l, ver):
        X += sum(1 for j in range(len(i)) if i.startswith(W, j))
      for i in filter(lambda l:W in l, dia):
        X += sum(1 for j in range(len(i)) if i.startswith(W, j))
        
      C.append(X)

  for i in range(len(C)):
    print("Case " + str(i+1) + ": " + str(C[i]))

word_find()