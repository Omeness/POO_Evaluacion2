from datetime import datetime
from Ejercicio_3.Clases.Actividad import Actividad


class Carrera(Actividad):
    def __init__(self, id_actividad, nombre, duracion_min, distancia_km:float):
        super().__init__(id_actividad, nombre, duracion_min)

        if distancia_km < 1: raise Exception("La distancia debe ser mayor a cero")

        _fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__distancia_km = distancia_km
        self.__eventos_registro = [
            f"[{_fecha}] "
            f"- Duracion original:  {self.duracion_min} min "
            f"- Distancia original:    {distancia_km}km"
            ]

    def _registrar_evento(self, nueva_distancia, nueva_duracion):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__eventos_registro.append(
            f"[{fecha}] "
            f"- Duracion acumulada: {nueva_duracion} min "
            f"- Distancia actualizada: {nueva_distancia}Km"
            )
    
    @property
    def ver_eventos(self):
        for registro in self.__eventos_registro:
            print(registro)
    
    @property
    def duracion_min(self):
        return super().duracion_min

    @duracion_min.setter
    def actualizar_duracion(self, nueva_duracion):
        super().actualizar_duracion
        duracion_acumulada = super().duracion_min + nueva_duracion
        self._registrar_evento(self.distancia_km, duracion_acumulada)
        print("Duracion actualizada con exito")
        
    @property
    def distancia_km(self):
        return self.__distancia_km
    
    @distancia_km.setter
    def registrar_distancia(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise Exception("La nueva distancia debe ser un mayor a cero")
        self._registrar_historial("Distancia", self.__distancia_km, nueva_distancia)
        self._registrar_evento(nueva_distancia, self.duracion_min)
        print(f"Distancia actualizada a {nueva_distancia} km.")
    
    def calcular_ritmo(self):
        return f"Ritmo: {self.duracion_min / self.__distancia_km:.2f} km/h"