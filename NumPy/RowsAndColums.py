import numpy as np

def get_rows(a):
    rivitLista = []
    for row in a:
        rivitLista.append(row)
    return rivitLista

def get_columns(a):
    sarakeLista = []
    #rez = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    for i in a.T:
        sarakeLista.append(i)
    return sarakeLista

def main():
    #a = np.array([[5, 0, 3, 3],[7, 9, 3, 5],[2, 4, 7, 6],[8, 8, 1, 6]])
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("Rivit",get_rows(a))
    print("Sarake",get_columns(a)) 

if __name__ == "__main__": 
    main() 