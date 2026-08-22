import json

productos = {
"huevos":{"precio":"125 BS","stock":50},
"1k queso":{"precio":"1280 BS","stock":20},
"desengrasante":{"precio":"950 BS","stock":25}
}

def ver_productos(productos):
	with open("inventario.json", "r") as archivo:
		productos = json.load(archivo)
	mostrar_productos = [(producto,valores["precio"]) for producto,valores in productos.items()]#puedes desempaquetar los valores de un dupla para usarlos individualmente
	for producto,precio in mostrar_productos:
		print(producto,precio)
		
	
def agregar_producto(productos):
	ag_producto = input("nombre del producto: ")
	precio = input("precio del producto: ")
	cantidad = int(input("cantidad de productos: "))
	productos[ag_producto] = {"precio":precio,"stock":cantidad}
	print("producto agregado con exito, escriba 'ver' en la consola para verificar")

def realizar_venta(productos):
	producto = input("escriba el nombre del producto: ")
	cantidad = int(input("cuantas unidades va vender: "))
	if producto in productos:
		stock_actual = productos[producto]["stock"] - cantidad
		productos[producto]["stock"] - cantidad
		print(f"producto: {producto},stock actual: {stock_actual}")
		
def eliminar_producto(productos):
	producto = input("ingrese el nombre del producto a eliminar: ")
	if producto in productos:
		productos.pop(producto)
		
def agotados(productos):
	lista_agotados = [producto for producto,valor in productos.items() if valor["stock"] < 4 ]
	print("los productos que estan por acabarse son:\n")
	print(lista_agotados)

def guardar(productos):
	with open("inventario.json","w") as archivo:
		json.dump(productos, archivo, indent = 4)
	print("su archivo ya se guardo como inventario.json")

		
	
while True:
	print("1. ver productos")
	print("2. agregar un producto")
	print("3. realizar una venta")
	print("4. eliminar producto")
	print("5. ver lista de agotados")
	print("6. guardar inventario")
	opcion = input("que quiere hacer??: ")
	
	if opcion == "1":
		ver_productos(productos)
	elif opcion == "2":
		agregar_producto(productos)
	elif opcion == "3":
		realizar_venta(productos)
	elif opcion == "4":
		eliminar_producto(productos)
	elif opcion == "5":
		agotados(productos)
	elif opcion == "6":
		guardar(productos)
	else:
		print("ingrese una opcion valida")
	

