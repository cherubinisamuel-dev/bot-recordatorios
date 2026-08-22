#stack frame
nombre = cheru

def saludar():#cuando en puntero lee la pila de llamadas crea un marco temporal donde se guarda la variable de abajo 
	print("hola usuario", nombre)
	
print(saludar(nombre))#depues de ser ejecutada ese marco desaparece junto con la variable por eso es un varible de alcance local 