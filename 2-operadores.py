#Operadores en python
#Nayely Karen Salas Mayta

#1. Operadores Aritmeticos
suma = 5 + 5
resta = 10 - 6 
multiplicacion = 5 * 5 
division = 10 / 2
modulo = 10 % 2
exponente = 10 ** 2

print('El resultado de la suma es:',suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(exponente)
#2. Operadores de comparación
print( 5 == 5 )  #igual a
print( 5 != 5 )  #Diferente de 
print( 10 > 5 )  #Mayor que
print( 10 < 5 )  #Menor que 
print( 10 >= 5 ) #Mayor igual que 
print( 10 <= 5 ) #Menor igual que 

#3. operadores logicos 
v = True
f = False
 #3.1. and (y)
print('-----------------------------------AND')
print(v and v)
print(v and f)
print(f and v)
print(f and f)
 #3.2. or (o)
print('------------------------------------OR')
print(v and v)
print(v and f)
print(f and v)
print(f and f)
 #3.3. not (negation)
print('------------------------------------NOT')
print(not v)
print(not f)

#4. Operadores de Asignación
# suma y asigna (+-)
print('-------------------------------------+=')
edad = 20
edad += 5
print(edad)

#resta y asigna (-=)
print('--------------------------------------=')
saldo = 100
saldo -= 10 
print(saldo)

#multiplica y asigna (*=)
print('----------------------------------------*=')
precio = 30
precio *= 5
print(precio)

# Divide y asigna (/=)
print('---------------------------------------/=')
precio = 200
precio /= 2
print(precio) 