import itertools

def main():
    with open('/users/matthewbuck/desktop/input.txt','r+') as f:
        x = f.read().splitlines()
        y = [line.split('\t') for line in x]
        z = [map(int,line) for line in y]
        total = 0
        for line in z:
            for a,b in itertools.permutations(line,2):
                if a%b == 0:
                    total += a//b
        print(total)
            

if __name__ == "__main__":
    main()