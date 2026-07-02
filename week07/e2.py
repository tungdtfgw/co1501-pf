def print_hollow_triangle(n):
    print('*')

    for i in range(1, n-1):
        print('*', end=' ')
        for j in range(i-1):
            print(' ', end=' ')
        print('*', end=' ')

        print()

    for i in range(n):
        print('*', end=' ')
    
    print()


n = 8
print_hollow_triangle(n)