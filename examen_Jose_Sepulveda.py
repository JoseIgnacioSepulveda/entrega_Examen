import os, time

os.system("cls")

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def stock_marcas(marca):
    for producto in marca:
        print()



def ver_marcas(marcas):
     for marcas in productos.items:
          print(marcas, [1])


def buscar_marca():
    for marca in productos.items:
        busca = input("ingrese la marca a buscar:")
        if busca == marca:
            print(marca)          


def menu():
    while True:
        try:
            print("***MENU PRINCIPAL***")
            print("1. Stock Marca.")
            print("2. Busqueda Actualizada.")
            print("3. Actualizar Precio.")
            print("4. Salir.")

            op = int(input("Seleccione una de las opciones >"))
            if op == 1:
                buscar_marca()
            elif op == 2: 
                print("buscar por precio.")
            elif op == 3:
                print("actualizar precio.")
            elif op == 4:
                print("Programa finalizado")
                break
            else:
                 input("seleccione una de las  opciones.")
                 os.system("cls")
        except:
            input("seleccione una de las opciones validas ")
            os.system("cls")
menu()