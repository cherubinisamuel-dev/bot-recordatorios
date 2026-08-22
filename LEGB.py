#al momento de que el puntero empieza a leer el valo de una variable lo hace en un orden especifico,a esto se le llama orden LEGB

usuario = "Cheru"#3G(GLOBAL)busca en las variables locales
usuario2 = "pepe"

def qlq():#2E(ENCLOSING)si la funcion esta dentro de otra,busca en la superior

	def hola():#1L(LOCAL)primero busca la variable que le pides en las funciones 
	
	    print("hola", usuario)#4B(BUILT-IN)busca en las palabras resevadas como print
	print("qlq mano", usuario2)