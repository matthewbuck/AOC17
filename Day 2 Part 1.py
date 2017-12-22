import re

def main():
    with open('/users/matthewbuck/desktop/input.txt','r+') as f:
        x = f.read().splitlines()
        y = [line.split('\t') for line in x]
        z = [[int(number) for number in line] for line in y]
        result = sum([(max(line)-min(line)) for line in z])
        print(result)
            

if __name__ == "__main__":
    main()