'''
listas diccionario set tuplas son las tipos de coleccion
crud= create ,read ,update ,and ,delate

lista=[1,2,3,4,5]
print(2)
########################
lista=[1,2,3,4,5]
lista.append(6)
for i in lista:
  print(i)
###########################
lista=[1,2,3,4,5]
lista.insert(3,"nata")
for i in lista:
  print(i)
###########################
lista=[1,2,3,"nata",4,5]
lista.remove("nata")
for i in lista:
  print(i)
###########################
lista=[5,4,3,2,1]
lista.reverse() # desordena
lista.sort() # ordena
for i in lista:
  print(i)
  '''
# listas=[]
# def agre():
#     global listas
#     inser=input("ingrese un producto: ")
#     listas.append(inser)
# def elim():
#     global listas
#     listas.sort()
#     print(listas)
#     while True:
#         try:
#             inser=input("que poducto quieres eliminar: ")
#             listas.remove(inser)
#             break
#         except Exception:
#             print("producto no existente")
#             break
# def mos():
#     global listas
#     listas.sort()
#     print(listas)    
# while True:
    # op=int(input('''seleccione una opcion
    #              1.- agregar un producto
    #              2.- eliminar un producto
    #              3.- mostrar todos los productos
    #              4.- salir 
    #              '''))
    
    # match op:
    #     case 1:
    #         agre()
    #     case 2:
    #         elim()
    #     case 3:
    #         mos()
    #     case 4:
    #         break
    #     case _:
    #         print("numero in valido")

#       -5-4 -3 -2-1 
numeros=[7,5,33,24,9]
#      0 1 2  3  4

# print(numeros[:])

# for numero in numeros:
#   print(f"numero {numero}")

# print(numeros)

# numeros.append(64)

# print(numeros)

# numeros.insert(3,100)

# print(numeros)

# nombres=[]
# apellidos=[]
# con=0
# while True:
#   op=int(input('''seleccionar una opcion
#                 1.-insertar nombre
#                 2.-mostar nombre y apellido
#                 3.-buscar nombres
#                 4.-salir 
#                 '''))
#   match op:
#     case 1:
#       nom=input("ingrese un nombre: ")
#       nombres.append(nom)
#       ape=input("ingrese su apellido: ")
#       apellidos.append(ape)
#     case 2:
#       # for i in nombres:
#       #   print(i,apellidos[con])
#       #   con+=1
#       for e in range(len(nombres)):
#         print(nombres[e],apellidos[e])
#     case 3:
#       nomb=input("ingrese un nombre: ")
#       if nomb in nombres:
#         print(f"{nomb}")
#       else:
#         print(f"no exsiste el usuarion {nomb}")
#     case 4:
#       break
#     case _:
#       print()

productos=["leche","yogurd","mantequilla"]
precios=[1500,100,1250]
carrito=[]

while True:
  op=int(input('''seleccionen una opcion
               1.-ingresar in producto
               2.-comprar
               3.-crear boleta
               4.-salir
               '''))
  match op:
    case 1:
      agregar=input("ingrese un producto")
      productos.append(agregar)
      agregarpre=int(input("ingrese el precio"))
    case 2:
      for i in range(len(productos)):
        print(f"{i+1}-{productos[i]} ${precios[i]}")
      comprar=int(input("seleccione un producto: "))
      carrito.append(comprar-1)
      print(carrito)
    case 3:
      total=0
      for i in carrito:
        print()

    case 4:
      break