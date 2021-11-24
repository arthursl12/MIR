import numpy as np
import scipy.spatial as ss

def dtw_table_rec(X, Y):
    '''
    Retorna a matriz de DTW entre as músicas.
    
    Argumentos
    ----------
    X: matriz onde as colunas são tempo e as linhas são atributos
    Y: matriz onde as colunas são tempo e as linhas são atributos
    ''' 
    nx = X.shape[1]
    ny = Y.shape[1]
    
    D = np.zeros(shape=(nx, ny), dtype='d')
    
    
    def recurse(x,y):
        print("Recurse: ", x, y)
        print("D: ", D)
        
        if (x == nx-1) and (y == ny-1):
            return 1
        
        if (x < nx-1):
            if (D[x+1,y] != 0):
                return D[x+1,y] + 1
            else:
                return recurse(x+1, y) + 1
        if (y < ny-1):
            if (D[x,y+1] != 0):
                return D[x,y+1] + 1
            else:
                return recurse(x, y+1) + 1
        
        if (x < nx-1) and (y < ny-1):
            if (D[x+1,y+1] != 0):
                return D[x+1,y+1] + 1
            else:
                return recurse(x+1, y+1) + 1
            
    # ss.distance.cosine(chroma_classic[:, 0], chroma_amy[:, 0])
    recurse(0,0)
    return D

def dtw_table(X, Y):
    '''
    Retorna a matriz de DTW entre as músicas.
    
    Argumentos
    ----------
    X: matriz onde as colunas são tempo e as linhas são atributos
    Y: matriz onde as colunas são tempo e as linhas são atributos
    ''' 
    nx = X.shape[1]
    ny = Y.shape[1]
    
    # Os tempos de Y estão pelas colunas de D
    # Os tempos de X estão pelas linhas de D
    D = np.zeros(shape=(nx, ny), dtype='d')
    D.fill(np.nan)      # NaN's só para assegurar que estamos preenchendo
    
    # Inicializar a primeira coluna e a primeira linha como os custos somente
    # Primeira coluna: custo de atribuir o i-ésimo tempo de X ao tempo 0 de Y
    for i in range(nx):
        D[i,0] = ss.distance.cosine(X[:, i], Y[:, 0])
    # Primeira linha: custo de atribuir o tempo 0 de X ao j-ésimo tempo de Y  
    for j in range(ny):
        D[0,j] = ss.distance.cosine(X[:, 0], Y[:, j])

    # Iterar de (1,1) em diante para saber os outros custos
    # Lembrando que começamos a indexar de 0
    for i in range(1,nx):
        for j in range(1,ny):
            base_cost = ss.distance.cosine(X[:, i], Y[:, j])
            # print("Custo Base de (",i,j,"): ", base_cost)
            # print("\tCusto -1,-1: ", D[i-1,j-1])
            # print("\tCusto 0,-1: ", D[i,j-1])
            # print("\tCusto -1,0: ", D[i-1,j])
            cost = base_cost + min(D[i-1,j-1],D[i,j-1],D[i-1,j])
            D[i,j] = cost
            
    print(D)
    return D

if __name__ == "__main__":
    x = np.array([1, 4, 4, 2, -4, -4, 9])
    y = np.array([1, 3, 4, 3, 1, -1, -2, -1, 12])
    # x = np.array([1, 4])
    # y = np.array([1, 3])
    dtw_table(x[None], y[None])