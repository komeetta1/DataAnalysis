import numpy as np

def diamond(n):
    d1 = np.fliplr(np.eye(n, dtype = int))
    d2 = np.eye(n, n-1, k = -1, dtype = int)
    d3 = np.eye(n-1, n, k = 1, dtype = int)
    d4 = np.fliplr(np.eye(n-1, k = 1))

    upper = np.concatenate((d1, d2), axis = 1)
    lower = np.concatenate((d3, d4), axis = 1)
    return (np.concatenate((upper, lower)))

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()