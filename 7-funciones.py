#Nayely Karen Salas Mayta
#Funciones 

print("hola, Juan")
print("Bien venido al sistema")
print("-----------------------")

print("hola, Karen")
print("Bien venido al sistema")
print("-----------------------")

print("hola, Pepito")
print("Bien venido al sistema")
print("-----------------------") 


lista_nombres = ["Juan", "Karen", "Pepito"]
for i in lista_nombres:
    print("hola,",i)
    print("Bienvenido al sistema")
    print("------------------------------")

def saludar(nombre):  
    print("Hola,",nombre)
    print("Bienvenido al sistema")
    print("----------------------------")

saludar("Juan") 
saludar("Karen")
saludar("Pepito")

#Funciones con retrno
def suma(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    return(resultado)
print(suma(2,2))



#Funciones sin retorno return()
def suma2(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    print(resultado)
suma2(2,2)


 
