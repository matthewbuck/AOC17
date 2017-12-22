def main():
    seed = 277678
    start = 1
    while start**2 < seed:
        start +=2
    print("moves:",(((start-1)//2))+(((start-1)//2)-(start**2-seed)))
    return 0

if __name__ == "__main__":
    main()