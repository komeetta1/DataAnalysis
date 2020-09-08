search_words = ["the", "red", "blue"]
def word_frequencies(file_name):
    d = {}
    with open(file_name, 'r') as f:
        for line in f:
            line = line.lower().split()
            stripped = [x.strip('''!"#$%&'()*,-./:;?@[]_''') for x in line]
            for word in stripped:
                try:
                    d[word] += 1
                except KeyError:
                    d[word] = 1
    return d

def main():
    d = word_frequencies("Python2/alice.txt")
    
    for key, value in d.items():
        if key in search_words:
            print(key, value)

if __name__ == "__main__": 
    main()  


