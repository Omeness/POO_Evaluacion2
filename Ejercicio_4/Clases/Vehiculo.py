from datetime import datetime
import re


class Vehiculo():
    _id_vehiculo = set()

    def __init__(self, id_vehiculo, patente:str, peso_kg, estado="habilitado"):

        # Validaciones (regex patente, id unico, valor positivo)
        if id_vehiculo in type(self)._id_vehiculo: 
            raise Exception(f"El identificador '{id_vehiculo}' ya existe")
        patente_regex = re.compile(r"^([A-Z]{2}[0-9]{4}|[A-Z]{4}[0-9]{2})$")
        if not patente_regex.match(patente): raise Exception("Patente invalida")
        if peso_kg <= 0: raise Exception("El peso debe ser mayor a cero")
        type(self)._id_vehiculo.add(id_vehiculo)
        
        self.id_vehiculo = id_vehiculo
        self.__patente = patente
        self.__peso_kg = peso_kg
        self.estado = estado
        self._historial_eventos = []
        self.conteo_cambios = 0

    def _registrar_historial(self, tipo_evento, detalle_anterior, detalle_nuevo):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(
            f"[{fecha}] "
            f"Usuario ID: {self.id_vehiculo} - "
            f"Detalle: {tipo_evento} - "
            f"Valor anterior: {detalle_anterior} |"
            f"Valor nuevo: {detalle_nuevo}"
            )
    
    @property
    def patente(self):
        return self.__patente
    
    @property
    def peso_kg(self):
        return self.__peso_kg

    @peso_kg.setter
    def actualizar_peso(self, nuevo_peso_kg):
        # Verificar validez de datos y que el vehiculo este habilitado para la modificacion
        if nuevo_peso_kg <= 0:
            raise Exception("El nuevo peso debe ser un valor mayo a cero")
        if self.estado == "inhabilitado":
            raise Exception("El vehiculo esta inhabilitado")
        # Dejar registro y actualizar datos
        self._registrar_historial("Actualizacion peso", self.__peso_kg, nuevo_peso_kg)
        self.__peso_kg = nuevo_peso_kg
        print(f"Se ha actualizado el peso a {nuevo_peso_kg} Kg.")
        
    def habilitar(self, motivo):
        if self.estado == "habilitado":
            print("El estado ya esta habilitado")
        else:
            detalle = f"Habilitacion. Motivo: '{motivo}'"
            self._registrar_historial(detalle, "habilitado", "inhabilitado")
            self.estado = "habilitado"
            self.conteo_cambios += 1
            return "Cambio de estado a 'habilitado'"

    def inhabilitar(self, motivo):
        if self.estado == "inhabilitado":
            print("El estado ya esta inhabilitado")
        else:
            detalle = f"Inhabilitacion. Motivo: '{motivo}'"
            self._registrar_historial(detalle, "habilitado", "inhabilitado")
            self.estado = "inhabilitado"
            self.conteo_cambios += 1
            return "Cambio de estado a 'inhabilitado'"

    def consultar_ficha(self):
        # Fecha y hora de la ultima modificacion
        ultimo_cambio = self._historial_eventos[-1].split(" ")[0]
        print(
            f"ID Vehiculo: {self.id_vehiculo}\n"
            f"Patente: {self.patente}\n"
            f"Peso: {self.peso_kg} Kg\n"
            f"Estado actual: {self.estado}\n"
            f"Conteo cambios de estado: {self.conteo_cambios}\n"
            f"Ultimo registro: {ultimo_cambio}"
            )
        
    def ver_historial(self):
        print("--- Historial actualizaciones ---\n"
              f"Numero de registros: {len(self._historial_eventos)}")
        for evento in self._historial_eventos:
            print(evento)
        print("** Fin registros **")