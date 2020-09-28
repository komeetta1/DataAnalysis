
def extractNumbers(teksti):
    t = teksti.split()
    lista = []
    for i in t:
        try:
            lista.append(int(i))
        except ValueError:
            try:
                lista.append(float(i))
            except ValueError:
                continue

    return lista
def main():
    print(extractNumbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()