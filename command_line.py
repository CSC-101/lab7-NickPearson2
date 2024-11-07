import sys

if __name__ == '__main__':
    print(sys.argv)
    total = 0
    for arg in sys.argv:
        try:
            total += float(arg)
        except ValueError:
            print("Enter number")
    print(total)