from datetime import datetime


class Parcela:
    _id_unico = set()

    def __init__(self, id_parcela, superficie_ha, cultivo_actual:str, estado="activa"):
        
        # Validaciones (id unico, valores positivos o existentes)
        if id_parcela in type(self)._id_unico: 
            raise Exception(f"El ID '{id_parcela}' ya existe")
        if superficie_ha <= 0: raise Exception("La superficie debe ser mayor a cero")
        if not cultivo_actual.split(): raise Exception("El atributo no puede estar vacio")
        type(self)._id_unico.add(id_parcela)
        
        self.id_parcela = id_parcela
        self.__superficie_ha = round(superficie_ha, 2)
        self.cultivo_actual = cultivo_actual
        self.estado = estado
        self.__historial_eventos = []
    
    # Funcion protegida para registrar eventos con marca de tiempo
    def _registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__historial_eventos.append(f"[{fecha}] [{tipo}] - {detalle}")

    @property
    def superficie_ha(self):
        return self.__superficie_ha

    def rectificar_superficie(self, nueva_superficie, motivo):
        if nueva_superficie < 1:
            raise Exception("La superficie debe ser mayor a cero")
        detalle = f"{motivo} | Valor previo: {self.__superficie_ha}. Nuevo valor: {nueva_superficie}."
        self._registrar_evento("Rectificacion superficie", detalle)
        self.__superficie_ha = round(nueva_superficie, 2)
        print("Se ha rectificado la superficie con exito")

    @property
    def historial_eventos(self):
        print("--- Historial eventos ---")
        for evento in self.__historial_eventos:
            print(evento)
        print("** Fin registro **")
        

    def actualizar_cultivo(self, nuevo_cultivo):
        if self.estado == "inactiva":
            raise Exception("No se puede actualizar un cultivo inactivo")
        if  not nuevo_cultivo.split():
            raise Exception("Se debe especificar el tipo de cultivo")
        detalle = f"Se ha actualizado el cultivo '{self.cultivo_actual}' a '{nuevo_cultivo}'"
        self._registrar_evento("Actualizacion cultivo", detalle)
        self.cultivo_actual = nuevo_cultivo
        print(detalle)

    def desactivar(self, motivo):
        if self.estado == "activa":
            self.estado = "inactiva"
            self._registrar_evento("Desactivacion", motivo)
            print("Se ha desactivado la parcela")
        else:
            print("Error: El cultivo ya esta inactivo")

    def activar(self, motivo):
        if self.estado == "inactiva":
            self.estado = "activa"
            self._registrar_evento("Activacion", motivo)
            print("Se ha activado la parcela")
        else:
            print("Error: El cultivo ya esta activo")