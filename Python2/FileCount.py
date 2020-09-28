file_name = "Python2/filecount.txt"
def file_count(file_name):
    lines = 0
    words = 0
    characters = 0
    with open(file_name, "r") as f:
        for i in f:
            word = i.split()

            lines += 1
            words += len(word)
            characters += len(i)

    return lines, words, characters
print(file_count(file_name))