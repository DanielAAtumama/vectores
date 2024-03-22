# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
lista_mas_5_elementos = [1, 2, 3, 4, 5, 6, 7]

# 3. Encuentre la longitud de las dos listas creadas anteriormente.
longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_5_elementos = len(lista_mas_5_elementos)

# 4. Obtener el primer elemento, el elemento central y el último elemento de la lista.
primer_elemento = lista_mas_5_elementos[0]
elemento_central = lista_mas_5_elementos[len(lista_mas_5_elementos) // 2]
ultimo_elemento = lista_mas_5_elementos[-1]

# 5. Crear una lista llamada Datos_personales que contenga (nombre, edad, altura, estado civil, dirección), y agrega datos utilizando la funcion append().
Datos_personales = []
Datos_personales.append("Daniel")
Datos_personales.append(30)
Datos_personales.append(1.90)
Datos_personales.append("Soltero")
Datos_personales.append("Calle San Fernando")

# 6. Crea una lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Añadir una empresa a la lista it_companies utilizando la funcion insert().
it_companies.insert(1, "Twitter")

# 8. Comprobar si una determinada empresa existe en la lista it_companies.
empresa_existe = "Microsoft" in it_companies

# 9. Ordena la lista con el método sort()
it_companies.sort()

# 10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()

# 11. Elimine la primera empresa informática de la lista utilizando el metodo pop y delete.
primer_empresa = it_companies.pop(0)

# 12. Eliminar todas las empresas de la lista it_companies
it_companies.clear()

# Imprimir resultados
print("1. Lista vacía:", lista_vacia)
print("2. Lista con más de 5 elementos:", lista_mas_5_elementos)
print("3. Longitud de la lista vacía:", longitud_lista_vacia)
print("   Longitud de la lista con más de 5 elementos:", longitud_lista_mas_5_elementos)
print("4. Primer elemento:", primer_elemento)
print("   Elemento central:", elemento_central)
print("   Último elemento:", ultimo_elemento)
print("5. Datos personales:", Datos_personales)
print("6. Lista de empresas de TI:", it_companies)
print("7. ¿Microsoft existe en la lista de empresas de TI?:", empresa_existe)
print("10. Lista de empresas de TI en orden descendente:", it_companies)
