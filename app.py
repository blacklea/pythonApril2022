manager_pwd = '123'
manager_name = 'steff'

def login():
    name = input('Ingresa tu usuario: ')
    pwd = input('Ingresa tu contraseña: ')
    if (name !=manager_name or manager_pwd ):
        raise Exception('nombre de usuario o contraseña incorrecta')
    
