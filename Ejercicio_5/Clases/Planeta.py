from math import pi
from Ejercicio_5.Clases.CuerpoCeleste import CuerpoCeleste


class Planeta(CuerpoCeleste):   
    def __init__(self, nombre, masa_kg, radio_km, distancia_sol_km):
        super().__init__(nombre, masa_kg)
        if radio_km <= 0: raise Exception("El radio debe ser mayor a cero")
        if distancia_sol_km <= 0: raise Exception("La distancia debe ser mayor a cero")

        self.__radio_km = radio_km
        self.__distancia_sol_km = distancia_sol_km

    @property
    def radio_km(self):
        return self.__radio_km
    
    @radio_km.setter
    def actualizar_radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise Exception("El nuevo radio debe ser mayor a cero")
        super()._registrar_historial("Radio", self.__radio_km, nuevo_radio)
        print(f"Radio actualizado de {self.radio_km} km a {nuevo_radio} km")
        self.__radio_km = nuevo_radio
        self._conteo_modificaciones += 1

    @property
    def distancia_sol_km(self):
        return self.__distancia_sol_km
    
    @distancia_sol_km.setter
    def actualizar_distacia_sol(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise Exception("La nueva distancia debe ser mayor a cero")
        super()._registrar_historial("Radio", self.__distancia_sol_km, nueva_distancia)
        print(f"Distancia actualizada de {self.distancia_sol_km} km a {nueva_distancia} km")
        self.__distancia_sol_km = nueva_distancia
        self._conteo_modificaciones += 1

    def calcular_densidad(self):
        volumen = (4/3) * pi * (self.__radio_km ** 3)
        densidad = self.masa_kg / volumen
        print(f"Densidad del planeta {self.nombre}: {densidad:2e} kg/km³")

    def comparar_distancia(self, otro_planeta):
        if not isinstance(otro_planeta, Planeta):
            raise Exception("El argumento debe ser un objeto clase 'Planeta'")
        if self.__distancia_sol_km > otro_planeta.distancia_sol_km:
            print(f"El planeta {otro_planeta.nombre} esta mas cerca del sol")
        elif self.__distancia_sol_km == otro_planeta.distancia_sol_km:
            print("Los planetas estan a la misma distancia")
        else:
            print(f"El planeta {self.nombre} esta mas cerca del sol")