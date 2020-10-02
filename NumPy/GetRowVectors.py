import numpy as np

def get_row_vectors(a):
    rows, columns = np.shape(a)
    return(np.vsplit(a, rows))

def get_column_vectors(a):
    rows, columns = np.shape(a)
    return(np.hsplit(a, columns))

def main():
    a = np.array([[5, 0, 3], [3, 7, 9]])
    print("Row vectors:")
    print(get_row_vectors(a))
    print("Column vectors:")
    print(get_column_vectors(a))

if __name__ == "__main__":
    main()