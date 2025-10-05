from datetime import datetime
from Ejercicio_4.Clases.Vehiculo import Vehiculo


class Auto(Vehiculo):
    def __init__(self, id_vehiculo, patente, peso_kg, asientos_totales, 
                 ocupantes_actuales, sistema_retencion_infantil, estado="habilitado"):
        super().__init__(id_vehiculo, patente, peso_kg, estado)

        if asientos_totales <= 0: raise Exception("El numero de asientos debe ser mayor a cero")
        if ocupantes_actuales < 0: raise Exception("El numero de ocupantes debe ser un numero positivo")

        self.asientos_totales = asientos_totales
        self.__ocupantes_actuales = ocupantes_actuales
        self.sistema_retencion_infantil = sistema_retencion_infantil
        self._eventos_ocupacion = []
    
    def _registrar_evento(self, accion, cantidad, cantidad_anterior, cantidad_nueva):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._eventos_ocupacion.append(
            f"[{fecha}] "
            f"Accion: {accion} "
            f"Cantidad: {cantidad} - "
            f"Ocupantes anterior: {cantidad_anterior} |"
            f"Ocupantes actualizado: {cantidad_nueva}"
            )

    @property
    def ocupantes_actuales(self):
        return self.__ocupantes_actuales
    
    def subir_personas(self, cantidad):
        if self.estado == "inhabilitado":
            raise Exception("El vehiculo esta inhabilitado")
        if cantidad <= 0:
            raise Exception("La cantidad de pasajeros debe ser mayor a cero")
        if cantidad + self.ocupantes_actuales > self.asientos_totales:
            print("La cantidad de pasajeros excede numero de asientos disponibles")
        else:
            asientos_ocupados = cantidad + self.ocupantes_actuales
            asientos_disponibles = self.asientos_totales - cantidad
            self._registrar_evento("Subida de pasajeros", cantidad, self.ocupantes_actuales, asientos_ocupados)
            self.__ocupantes_actuales += cantidad
            print(f"Subieron {cantidad} personas al vehiculo. Asientos disponibles: {asientos_disponibles}")

    def bajar_personas(self, cantidad):
        if self.estado == "inhabilitado":
            raise Exception("El vehiculo esta inhabilitado")
        if cantidad <= 0:
            raise Exception("La cantidad de pasajeros debe ser mayor a cero")
        if self.ocupantes_actuales - cantidad < 0:
            print("La cantidad de pasajeros excede numero de ocupantes actuales")
        else:
            ocupantes = self.ocupantes_actuales - cantidad
            asientos_disponibles = self.asientos_totales - ocupantes
            self._registrar_evento("Bajada de pasajeros", cantidad, self.ocupantes_actuales, ocupantes)
            self.__ocupantes_actuales -= cantidad
            print(f"Bajaron {cantidad} personas del vehiculo. Asientos disponibles: {asientos_disponibles}")
        
        
    def reconfigurar_asientos(self, nuevo_total, motivo):
        if self.estado == "inhabilitado":
            raise Exception("El vehiculo esta inhabilitado")
        if nuevo_total < 1:
            raise Exception("El numero de asientos debe ser mayor a cero")
        if nuevo_total < self.ocupantes_actuales:
            print(f"El numero de asientos debe ser mayor a {self.ocupantes_actuales}")
        else:
            evento = f"Reconfiguracion asientos. Motivo: '{motivo}'"
            self._registrar_historial(evento, self.asientos_totales, nuevo_total)
            self.asientos_totales = nuevo_total
            print(f"Se reconfiguro el numero de asientos. Nuevo monto: {nuevo_total}")

    def vaciar_auto(self, motivo):
        if self.estado == "inhabilitado":
            raise Exception("El vehiculo esta inhabilitado")
        evento = f"Vaciar auto. Motivo '{motivo}'"
        self._registrar_evento(evento, self.ocupantes_actuales, self.ocupantes_actuales, 0)
        self.__ocupantes_actuales = 0
        print("Se ha vaciado el auto con exito")
    
    # Aqui se obtienen los datos derivados pedidos: asientos_libres y tasa_ocupacion
    # Sentia que hacer un metodo para obtener cada uno de esos datos quizas iba a ser un poco innecesario
    def consultar_ocupacion(self):
        asientos_libres = self.asientos_totales - self.ocupantes_actuales
        tasa_ocupacion = self.ocupantes_actuales / self.asientos_totales * 100
        print(f"Ocupantes actuales: {self.ocupantes_actuales}\n"
              f"Asientos libres: {asientos_libres}\n"
              f"Tasa ocupacion: {tasa_ocupacion}%\n")
        
    # Dato derivado: Número de eventos de subida/bajada en un rango de fechas (creo)  
    def ver_eventos(self):
        print("--- Eventos ocupacion ---\n"
              f"Numero eventos: {len(self._eventos_ocupacion)}")
        for evento in self._eventos_ocupacion:
            print(evento)
        print("** Fin registros **")

