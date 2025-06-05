def lower_triangular(n):
    print("\nLower Triangular Pattern:")
    for i in range(1, n+1):
        print("* " * i)
def upper_triangular(n):
    print("\nUpper Triangular Pattern:")
    for i in range(n):
        print("  " * i + "* " * (n - i))
def pyramid(n):
    print("\nPyramid Pattern:")
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

n = int(input("Enter number of rows: "))
lower_triangular(n)
upper_triangular(n)
pyramid(n)
