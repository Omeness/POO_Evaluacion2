from Ejercicio_1.Clases.Parcela import Parcela
from Ejercicio_1.Clases.ParcelaConRiego import ParcelaConRiego
from Ejercicio_2.Clases.Libro import Libro
from Ejercicio_2.Clases.Publicacion import Publicacion
from Ejercicio_3.Clases.Actividad import Actividad
from Ejercicio_3.Clases.Carrera import Carrera
from Ejercicio_4.Clases.Vehiculo import Vehiculo
from Ejercicio_4.Clases.Auto import Auto
from Ejercicio_5.Clases.CuerpoCeleste import CuerpoCeleste
from Ejercicio_5.Clases.Planeta import Planeta


print("\n----------------- EJERCICIO 1 -----------------\n")

# Creacion de objeto Parcela y actualizacion de registro
parcela1 = Parcela(10, 10.50, "Trigo", "activa")
parcela1.actualizar_cultivo("Maiz")

print("\n### Visualizar el registro hecho")
parcela1.historial_eventos

print("\n### Creamos mas cambios para registrar")
parcela1.desactivar("vacaciones")
parcela1.activar("termino vacaciones")
parcela1.rectificar_superficie(15.40, "crecio el terreno")

print()
parcela1.historial_eventos

# Probar con valores invalidos
# Creamos varias parcelas para corroborar que funciona el verificador de ID
p1 = Parcela(20, 10.50, "Trigo", "activa")
p2 = Parcela(12, 10.50, "Maiz", "activa")
p3 = Parcela(13, 10.50, "Manzana", "activa")
p4 = Parcela(14, 10.50, "Habas", "activa")

print("\n### Error porque el id se repite")
try:
    p5 = Parcela(13, 10.50, "Trigo", "activa")
except Exception as e:
    print("Error:", e)

# No se como "asociar" asi que hice otro objeto :| no se si se referia a eso jjj
parcela2 = ParcelaConRiego(11, 10.50, "Maiz", 0, 1500, 2000)

print("\n### Nuevos registros y visualizarcion")
parcela2.cargar_agua = 20000
parcela2.regar_automatico("estricto")
print()
parcela2.eventos_riego

print()
parcela2.desactivar("Fin temporada")

print("\n### Intento de regar con parcela inactiva")
try:
    parcela2.regar_automatico("parcial")
except Exception as e:
    print("Error:", e)

print("\n### Activacion, riego y registros")
parcela2.activar("Comienzo temporada")
parcela2.regar_automatico("parcial")
print()
parcela2.eventos_riego

print("\n### Realizamos mas cambios para ver que dejen registro")
parcela2.configurar_tasa(2000)
parcela2.configurar_umbral(1000)
parcela2.habilitar_riego()
parcela2.inhabilitar_riego()
parcela2.habilitar_riego()
parcela2.regar_automatico("parcial")
print()
parcela2.historial_eventos
print()
parcela2.eventos_riego

print("\n### Litros disponibles solo se puede modificar a traves de cargar_agua")
try:
    parcela2.litros_disponibles = -11
except Exception as e:
    print("Error:", e)

print("\n### Carga de agua con valor invalido")
try:
    parcela2.cargar_agua = 0
except Exception as e:
    print("Error:", e)


print("\n----------------- EJERCICIO 2 -----------------\n")

# Creamos la publicacion
publicacion = Publicacion(10, "Don Quijote", 1605)

print("\n### Intentamos crear publicacion con fecha invalida")
try:
    publicacion2 = Publicacion(11, "Don Quijote", 1400)
except Exception as e:
    print("Error:", e)

print("\n### Creamos un libro, leemos y consultamos prograso")
publicacion2 = Libro(11, "Cien años de soledad", 1990, 500)
publicacion2.leer(120)
publicacion2.consultar_progreso()

print("\n### Intentamos leer mas paginas de las que hay")
publicacion2.leer(400)

print("\n### Actualizamos datos y revisamos registro")
publicacion2.actualizar_anio = 1967
publicacion2.actualizar_titulo = "100 años de soledad"
print()
publicacion2.historial_eventos()

print("\n### Intentos de modificar paginas leidas o totales")
try:
    publicacion2.paginas_leidas = 10
except Exception as e:
    print("Error:", e)

try:
    publicacion2.paginas_totales = 10
except Exception as e:
    print("Error:", e)

print("\n### Creamos otro libro y leemos varias paginas, revisamos registro")
lib1 = Libro(12, "Biblia", 1990, 1500)
lib1.leer(20)
lib1.leer(150)
lib1.leer(200)
lib1.leer(550)
lib1.leer(348)
print()
lib1.evento_lectura
lib1.consultar_progreso()


print("\n----------------- EJERCICIO 3 -----------------\n")

# Creamos una actividad
act1 = Actividad(10, "Yoga", 60)

print("\n### Intentamos crear una actividad con duracion cero y otra sin nombre")
# Duracion 0
try:
    act2 = Actividad(11, "Yoga", 0)
except Exception as e:
    print("Error:", e)

# Sin nombre
try:
    act2 = Actividad(12, "", 12)
except Exception as e:
    print("Error:", e)

print("\n### Creamos una carrera y calculamos el ritmo")
carrera = Carrera(11, "Maraton", 50, 10)
print(carrera.calcular_ritmo())

print("\n### Actualizamos datos y vemos el registro")
carrera.actualizar_duracion = 55
carrera.ver_eventos

print("\n### Intentamos cambiar la distancia a un numero negativo")
try:
    carrera.registrar_distancia = -3
except Exception as e:
    print("Error:", e)

print("\n### Intentamos modificar la distancia de manera directa")
try:
    carrera.distancia_km = 10
except Exception as e:
    print("Error:", e)


print("\n----------------- EJERCICIO 4 -----------------\n")

veh = Vehiculo(10, "ABCD12", 1450)

print("\n### Actualizamos el peso e intentamos actualizar a cero")
veh.actualizar_peso = 1500
try:
    veh.actualizar_peso = 0
except Exception as e:
    print("Error:", e)

print("\n### Inhabilitamos el vehiculo e intentamos actualizar peso")

veh.inhabilitar("mantencion")
try:
    veh.actualizar_peso = 1600
except Exception as e:
    print("Error:", e)

print("\n### Habilitamos y vemos registro")
veh.habilitar("mantencion finalizada")
veh.ver_historial()

# Creamos Auto
auto1 = Auto(11, "QWER12", 1600, 5, 0, "no")

print("\n### Intentamos crear un auto con patente invalida y otro con ID repetido")
# Patente invalida
try:
    a2 = Auto(14, "abc123", 1600, 5, 2, "no")
except Exception as e:
    print("Error:", e)

# ID repetido
try:
    a1 = Auto(10, "QWER12", 1600, 5, 0, "no")
except Exception as e:
    print("Error:", e)

print("\n### Subimos personas, consultamos ocupacion e intentamos subir mas de la capacidad")
auto1.subir_personas(3)
print()
auto1.consultar_ocupacion()
try:
    auto1.subir_personas(3)
except Exception as e:
    print("Error:", e)

print("\n### Bajamos gente e intentamos bajar mas de los que hay")
auto1.bajar_personas(2)

try:
    auto1.bajar_personas(5)
except Exception as e:
    print("Error:", e)

print("\n### Reconfiguramos el auto y tratamos de reconfigurar valoir cero")
auto1.reconfigurar_asientos(2, "reparacion")

try:
    auto1.reconfigurar_asientos(0, "reparacion")
except Exception as e:
    print("Error:", e)

print("\n### Vaciamos el auto y vemos el historial")
auto1.vaciar_auto("fin del turno")
print()
auto1.ver_eventos()
print("\n### Hacemos un par de cambios y revisamos la ficha")
auto1.inhabilitar("test")
auto1.habilitar("test")
auto1.inhabilitar("test")
auto1.habilitar("test")
auto1.consultar_ficha()
print()
auto1.ver_historial()


print("\n----------------- EJERCICIO 5 -----------------\n")


cc1 = CuerpoCeleste("Estrella X", 2*10e30)
pl1 = Planeta("Tierra", 5.97*10e24, 6371, 149600000)
pl2 = Planeta("Marte", 6.42*10e23, 3389, 227900000)

print("\n### Calculamos densidad del planeta y comparamos distancias con otro")
pl1.calcular_densidad()
pl1.comparar_distancia(pl2)

print("\n### Actualizamos datos y consultamos ficha")
pl1.actualizar_distacia_sol = 5900000000
pl1.actualizar_masa = 1.3*10e22
pl1.actualizar_radio = 1188
pl1.actualizar_nombre = "Pluto"
pl1.consultar_ficha()

print("\n### Intentamos crear un planeta con radio cero")
try:
    pl3 = Planeta("Pluto", 1.3*10e22, 0, 10)
except Exception as e:
    print("Error:", e)

print("\n### Intentamos crear un planeta con distancia negativa")
try:
    pl3 = Planeta("Pluto", 1.3*10e22, 1188, -10)
except Exception as e:
    print("Error:", e)

print("\n### Intentamos modificar atributo de manera directa")
try:
    pl1.masa_kg = 10
except Exception as e:
    print("Error:", e)

print("\n### Validacion ID")
# Primero creamos varios objetos.
cuerpo1 = CuerpoCeleste("ejemplo1", 10)
cuerpo2 = CuerpoCeleste("ejemplo2", 10)
cuerpo3 = CuerpoCeleste("ejemplo3", 10)
cuerpo4 = CuerpoCeleste("ejemplo4", 10)
planeta1 = Planeta("ejemplo5", 10, 10, 10)
planeta2 = Planeta("ejemplo6", 10, 10, 10)
planeta3 = Planeta("ejemplo7", 10, 10, 10)

print("### Aqui visualizamos que los ID se han ido generando de manera esperada")
print(cuerpo1.id_celeste)
print(cuerpo2.id_celeste)
print(cuerpo3.id_celeste)
print(cuerpo4.id_celeste)
print(planeta1.id_celeste)
print(planeta2.id_celeste)
print(planeta3.id_celeste)

print("\n----------------- Fin ejercicios -----------------\n")
print("Solo si quiere verificar que las fechas se estan almacenando correctamente, descomente la siguiente seccion:")

# Esta parte tiene cero logica, solo es para revisar jj


# import os
# if os.name == 'nt': os.system('cls') 
# else: os.system('clear')

# print("-- Creamos la clase y le cambiamos el nombre --\n")
# while True:
#     test = Carrera(33, "test", 10, 10)
#     test.actualizar_nombre = "test1"
#     input("Espere un poco y Enter\n")
#     test.actualizar_nombre = "test2"
#     input("Enter para continuar\n")
#     test.actualizar_nombre = "test"
#     input("Enter para ver ficha\n")
#     test.ver_historial
#     break