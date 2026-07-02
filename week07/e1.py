import random as rd

numbers = rd.sample(range(100), 20)

def print_list(a):
    for n in a:
        print(n, end=' ')
    print()

def count_div(a, b):
    count = 0
    for n in a:
        if n % b == 0:
            count += 1
    
    return count

def sum_div(a, b):
    s = 0
    for n in a:
        if n % b == 0:
            s += n
    
    return s

def my_min(a):
    m = a[0]
    for i in range(1, len(a)):
        if a[i] < m:
            m = a[i]

    return m

def my_max(a):
    m = a[0]
    for i in range(1, len(a)):
        if a[i] > m:
            m = a[i]

    return m


# Gọi các hàm đã viết
print_list(numbers)
n = 10
print(f'Số các số chia hết cho {n}: {count_div(numbers, n)}')
print(f'Tổng các số chia hết cho {n}: {sum_div(numbers, n)}')
print(f'Min: {my_min(numbers)}, max: {my_max(numbers)}')