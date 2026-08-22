def list_comprecion():
	nombres = ["pepe","cheru","martha"]
	ac_nombres = [nombre.upper() for nombre in nombres if len(nombre) > 4]
	print(nombres)
	print(ac_nombres)
	
print(list_comprecion(), end= "")
    
	


