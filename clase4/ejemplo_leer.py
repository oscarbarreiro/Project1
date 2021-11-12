# leer
# fichero = open("quijote_pg2000.txt", 'r')
# for linea in fichero:
#     print(linea)
# fichero.close()

# # Lee los primeros 200 caracteres de un fichero
# with open("quijote_pg2000.txt", 'r') as fichero:
#     contenido = fichero.read(200)
#     print(contenido)

# # Lee la primera l�nea de un fichero
# with open("quijote_pg2000.txt", 'r') as file:
#     contenido = file.readline()
#     print(contenido)

# # Lee los p�rrafos de un fichero.
# # Strip() evita una l�nea en blanco entre ellos.
# with open("quijote_pg2000.txt", 'r') as file:
#     contenidos = file.readlines(2000)
#     for c in contenidos:
#         print(c.strip())

# entrada = """Primera parte del ingenioso hidalgo don Quijote de la Mancha
#
#
# """
# # Creamos un fichero y pegamos el texto de la variable entrada
# with open("quijote-ext01.txt", 'x') as file:
#     file.write(entrada)
#
entrada_agregar = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
no ha mucho tiempo que viv�a un hidalgo de los de lanza en astillero, adarga antigua,
roc�n flaco y galgo corredor. Una olla de algo m�s vaca que carnero, ...

"""
# Abrimos el fichero y adjuntamos el texto de la variable ?entrada_agregar?
with open("quijote-ext01.txt", 'a') as file:
    file.write(entrada_agregar)

# Busca a partir del car�cter 18 e imprime los 42 caracteres siguientes
with open("quijote-ext01.txt", 'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)
