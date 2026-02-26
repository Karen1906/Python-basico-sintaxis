    #Nayely Karen Salas Mayta
#Listas
lista = ["Nayely","Salas",25,True]
print(lista[0])
#Lista de Frutas
frutas = ["papaya", "platano", "pera", "uva", "mango"]
print(frutas[3])

frutas[1] = "Granada"
print(frutas)
for i in frutas:
    print(i)
#Matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print(matriz[2][2])

#lista de Numeros
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])

#ciclo For en las listas
for i in numeros:
    print(i)
for i in numeros:
    print(i*10)



#Metodos en las listas
print("----------------------------  Metodos")
frutas = ["papaya", "platano", "pera", "uva", "mango"]

#Agregar un nuevo dato
frutas.append("Ciruela")
print(frutas)

#Insert() = Insertar un dato
frutas.insert(2,"piña")
print(frutas)

#Remove() = Borrar un dato
frutas.remove( "uva")
print(frutas)

#Pop() = Para obtener o eliminar el ultimo dato
frutas.pop()
print(frutas)

#sort() = ordenar la lista
frutas.sort()
print(frutas)

#reverse() = revertir
frutas.reverse()
print(frutas)

#Len() = sirve para contar datos
cantidad = len(frutas)
print(cantidad)

#Index() = Encontrar el indice
Indice = frutas.index("papaya")
print(frutas)