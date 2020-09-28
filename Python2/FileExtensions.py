file_name = "Python2/fileExtensions.txt"
def file_extensions(file_name):
    dictionary = {}
    lista = []
    with open(file_name, "r") as f:
        for i in f:
            if "." in i:
                i = i.strip("\n")
                f_extns = i.split(".")[-1]
                try:
                    dictionary[f_extns].append(i)
                except KeyError:
                    dictionary[f_extns] = [i]
            else:
                lista.append(i)
            
    return lista, dictionary

def main():
    d = file_extensions(file_name)
    print(d)

if __name__ == "__main__": 
    main() 
