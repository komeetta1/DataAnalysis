import re

def integers_in_brackets(teksti):
    numerot = re.findall(r'[-]?\b\d+\b', teksti)
    return numerot

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__": 
    main()   