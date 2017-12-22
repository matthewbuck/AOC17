# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def main():
    with open('/users/matthewbuck/desktop/input.txt','r+') as f:
        x = f.read().strip()
        y = 0
        for n in range(len(x)):
            if int(x[n]) == int(x[(n+len(x)//2)%len(x)]):
                y+=int(x[n])
        print(y)
    return 0

if __name__ == "__main__":
    main()
    