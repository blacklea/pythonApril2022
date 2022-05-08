
products = dict()
clients = dict()

manager_pwd = '123'
manager_name = 'steff'




def add_product():
    name = input('Ingresa el nombre del producto: ')
    quantity = int(input('Ingresa la cantidad de producto disponible: '))
    price = int(input('Ingresa el precio del producto: '))
    products[name.upper()] = [name.upper(), quantity , price]



def add_client():
    client_name = input('Ingresa el nuevo cliente: ')
    client_pwd =  input('Elige una contraseña: ')
    clients[client_name.upper()] = [ client_name.upper(), client_pwd.upper(), [] ]

def sale_product():
    client_name = input('Ingresa el nombre del cliente: ')
    if (client_name.upper() not in clients):
        raise Exception('Cliente inexistente')
    while True:
        product = input('Ingresa producto a comprar: ')
        if (product.upper() not in products):
            raise Exception('producto inexistente: ')

def app():
    choices = [1,2,3,4,5]
    while True:
        try:
            print("""
            1 => Cliente
            2 => Producto
            3 => Venta
            4 => Cerrar programa
            """)
            
            c = int(input('Ingresa una opción: '))
            if c not in choices:
                raise Exception('opción no válida')
            elif c == 1:
                while True:
                    print("""
                    1 => Agregar nuevo cliente
                    2 => Borrar cliente
                    3 => Lista de clientes
                    4 => Vuelve al menú principal
                    """)
                    choice = int(input('Ingresa una opción: '))
                    if not choice in choices[:-1]:
                        raise Exception('opción no válida ')
                    elif(choice == 1):
                        add_client()
                    elif(choice == 2):
                        client_name =input('Ingresa el nombre del cliente a borrar: ').upper()
                        if (not client_name in clients):
                            raise Exception('Cliente inexistente ')
                        pwd = input('Ingresa contraseña de cliente para confirmar ')
                        if (pwd != clients[client_name][-2]):
                            raise Exception ('contraseña incorrecta')
                        clients.pop(client_name)
                        print('Cliente borrado')
                    elif(choice == 3):
                        for val in clients.values():
                            print(val)
                    elif(choice == 4):
                        break
            elif c == 2:
                while True:
                    print(
                    """
                    1 => Agregar producto
                    2 => Borrar producto
                    3 => Lista de productos
                    4 => Volver al menú principal
                    """
                    )
                    choice = int(input('Elige una opción: '))
                    if choice == 1:
                        add_product()
                    elif choice == 2 :
                        product_name = input('Ingresa el producto a borrar: ')
                        if (product_name.upper() not in products):
                            raise Exception('Este producto no existe en nuestra tienda')
                        else:
                            products.pop(product_name.upper())
                            print('producto borrado')
                    elif choice == 3 :
                        for val in products.values():
                            print(val)
                    elif choice == 4 :
                        break
            elif c == 3:
                cart = list()
                client_name = input('Ingresa nombre del cliente:  ').upper()
                if (not client_name in clients):
                            raise Exception('Cliente inexistente ')
                while True:
                    try:
                        print('\n1- Agregar producto al carrito')
                        print('2- Borrar producto del carrito')
                        print('3- Ver carrito')
                        print('4- Confirmar compra\n')
                        
                        c = int(input('Elige una opción: '))
                        
                        if (not c in choices[:-1]):
                            raise Exception('opción inexistente ')
                        
                        elif c == 1:
                            product = input('Ingresa el nombre del producto: ').upper()
                            if (not product in products):
                                raise Exception("No tenemos stock")
                            
                            else:
                                quantity = int(input('Ingresa la cantidad: '))
                                if products[product][1] <  quantity:
                                    raise Exception('no suficientes items en stock ')
                                products[product][1] -= quantity
                                cart.append((product, quantity))
                        elif c == 2:
                            to_remove = input('Ingresa el producto a borrar: ').upper()
                            for i in range(len(cart)):
                                if cart[i][0] == to_remove:
                                    print(cart[i])
                                    products[product][1] += cart[i][1]
                                    cart.pop(i)
                                    continue
                                raise Exception("Producto fuera del carrito ")
                        elif c == 3:
                            for val in cart:
                                print(val)
                        elif c == 4:
                            total = 0
                            for val in cart:
                                total += (products[val[0]][-1] * val[1] )
                            
                            confirm = input('Escribe: "si" para confirmar la compra, u otra tecla para cancelar:  ').lower()
                            if (confirm == 'si'):
                                clients[client_name][-1].extend(cart)
                                cart.clear()
                                print(f'el total es {total} $ Págame ')
                                break
                            else:
                                print('\ncancelado')
                                break

                    except Exception as e:
                        print(e)
            elif c == 4:
                break
        except Exception as err:
            print(err)
        
        
def login():
    try:
        name = input('Ingresa tu usuario: ')
        pwd = input('Ingresa tu contraseña: ')
        if (name != manager_name or manager_pwd != pwd ):
            raise Exception('Usuario o contraseña incorrecto, por favor intente de nuevo')
        app()
    except Exception as err:
            print(err)


login()
