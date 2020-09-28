

class prepend():

    def __init__(self, start):
        self.start = start

    def write(self, writeText):
        print(self.start, writeText)

def main():
    s = prepend("+++")
    s.write("Hello")

if __name__ == "__main__": 
    main() 