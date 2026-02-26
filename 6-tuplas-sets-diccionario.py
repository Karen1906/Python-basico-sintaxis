#Nayely Karen Salas Mayta
#Tuplas Sets y Diccionarios.

#Tuplas 
# Simbolos ()
# por default lo ordena 
# inmutables = no se puede hacer cambios 
# te acepta duplicados  

tupla = (1,2,1,2, 40, 10, 5, 11)
print(tupla)

#indices 
print(tupla[4])


#Sets
# Simbolo {}
# No ordena
# Mutable = si puedes hacer cambios 
# No te acepta duplicados 
sets ={1,2,3,1,2,3}
print(sets)

#add() agregar un nuevo dato 
sets.add(4)
print(sets)

#remove() eliminar un dato
sets.remove(3)
print(sets)


# Diccionarios
# Simbolo {key:value}
# Si Ordena 

estudiante = {
    "nombre" : "Nayely",
    "natalidad" : "Puno",
    "edad" : 21,
    "carrera" : "Ingenieria"
} 
print(estudiante)

print(estudiante["nombre"])
print(estudiante["edad"])
print(estudiante["natalidad"])
print(estudiante["carrera"])

estudiante["edad"] = 18
print(estudiante)

#Ciclo for en los Diccionarios
for clave, valor in estudiante.items():
    print("clave: ", clave, "Valor: ", valor)