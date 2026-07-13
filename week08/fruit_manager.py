products = ['apple', 'mango', 'kiwi', 'lemon']
quantities = [100, 120, 80, 75]

def show_products():
    print('Fruits in store: ')
    n = len(products)
    for i in range(n):
        print(f'{products[i]:6}: {quantities[i]:3} qty')

def add_product():
    print('Add a fruit to the store')
    fruit = input('Enter a fruit: ')
    qty = int(input('Enter a quantity: '))

    products.append(fruit)  # add fruit to the list products
    quantities.append(qty)  # add qty to the list quantities

    print(f'{qty} {fruit} added to the store.')

def shell_product():
    print('Shell a product.')
    fruit = input('Enter a fruit: ')
    for i in range(len(products)):
        if products[i] == fruit: # found
            qty = int(input('Enter sold quantity: '))
            # update current quantity
            quantities[i] -= qty
            print(f'Sold {qty} {fruit}')
            return  # exit function
    
    # if not found
    print(f'{fruit} not found!')

def delete_product():
    print('Delete a product.')
    fruit = input('Enter a fruit: ')
    for i in range(len(products)):
        if products[i] == fruit: # found
            products.pop(i)
            quantities.pop(i)
            print(f'Remove {fruit} from store.')
            return
    
    print(f'{fruit} not found!')

def print_menu():
    print('Fruit management')
    print('1. Show fruits')
    print('2. Add a fruit')
    print('3. Sell a fruit')
    print('4. Remove fruit')
    print('5. Exit')

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            show_products()
        elif choice == 2:
            add_product()
        elif choice == 3:
            shell_product()
        elif choice == 4:
            delete_product()
        elif choice == 5:
            running = False
        else:
            print('Invalid choice!')


### MAIN ####
main()