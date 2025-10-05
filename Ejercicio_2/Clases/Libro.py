from datetime import datetime
from Ejercicio_2.Clases.Publicacion import Publicacion


class Libro(Publicacion):
    def __init__(self, id_publicacion, titulo, anio, paginas_totales, paginas_leidas=0):
        super().__init__(id_publicacion, titulo, anio)
        
        if paginas_totales <= 0: raise Exception("Las paginas totales deben ser mayor a 0")
        
        self.__paginas_totales = paginas_totales
        self.__paginas_leidas = paginas_leidas
        self.__eventos_lectura = []

    def __registrar_lectura(self, paginas_leidas, acumulado):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__eventos_lectura.append(f"[{fecha}] Leido: {paginas_leidas} Acumulado: {acumulado}")

    @property
    # Solo lectura. No hay setter para evitar la modificacion directa del atributo
    def paginas_totales(self):
        return self.__paginas_totales
    
    @property
    # Solo lectura. No hay setter para evitar la modificacion directa del atributo
    def paginas_leidas(self):
        return self.__paginas_leidas
    
    @property
    def evento_lectura(self):
        print("--- Eventos lectura ---\n")
        for evento in self.__eventos_lectura:
            print(evento)
        print("** Fin registros **")

    def leer(self, paginas):
        if paginas < 1:
            raise Exception("El numero de paginas debe ser mayor a cero")
        if self.__paginas_leidas + paginas <= self.__paginas_totales:
            self.__paginas_leidas += paginas
            self.__registrar_lectura(paginas,self.__paginas_leidas)
            print(f"Leiste {paginas} paginas")
        else:
            paginas_restantes = self.__paginas_totales - self.__paginas_leidas
            print(f"Error: Las paginas a leer ({paginas}) superan las paginas restantes ({paginas_restantes})")

    def consultar_progreso(self):
        print(f"Porcentaje de lectura: {self.__paginas_leidas / self.__paginas_totales * 100:.1f}%")