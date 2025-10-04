from datetime import datetime


class CuerpoCeleste:
    # Otra forma de validar que el id sea unico entre objetos, se va generando solo
    _id_celeste = 10

    def __init__(self, nombre:str, masa_kg):
        if not nombre: raise Exception("El nombre no puede estar vacio")
        if masa_kg <= 0: raise Exception("La masa debe ser un valor mayor a cero")

        self.id_celeste = type(self)._id_celeste
        self.__nombre = nombre
        self.__masa_kg = masa_kg
        self._historial_eventos = []
        self._conteo_modificaciones = 0
        self._ultima_modificacions_masa = ""
        type(self)._id_celeste += 1

    def fecha_ultima_actualizacion(self):
        return self._ultima_modificacions_masa

    def numero_modificacion(self):
        return self._conteo_modificaciones

    def _registrar_historial(self, campo, valor_anterior, valor_nuevo):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(
            f"[{fecha}] Campo: '{campo}'. "
            f"Valor Anterior: {valor_anterior}. Valor nuevo: {valor_nuevo}"
            )
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise Exception("El nuevo nombre no puede estar vacio")
        self._registrar_historial("Nombre", self.__nombre, nuevo_nombre)
        print(f"Nombre actualizado de '{self.__nombre}' a '{nuevo_nombre}'")
        self.__nombre = nuevo_nombre
        self._conteo_modificaciones += 1
    
    @property
    def masa_kg(self):
        return self.__masa_kg
    
    @masa_kg.setter
    def actualizar_masa(self, nueva_masa):
        if nueva_masa <= 0:
            raise Exception("La nueva masa debe ser un valor mayor a cero")
        self._registrar_historial("Masa", f"{self.__masa_kg:2e}", f"{nueva_masa:2e}")
        print(f"Masa actualizado de '{self.__masa_kg:2e}' a '{nueva_masa:2e}'")
        self.__masa_kg = nueva_masa
        self._conteo_modificaciones += 1
        ultimo_cambio = self._historial_eventos[-1].split(" ")[0]
        self._ultima_modificacions_masa = ultimo_cambio

    def consultar_ficha(self):
        print("\n--- Ficha Cuerpo Celeste ---\n"
              f"ID: {self.id_celeste}\n"
              f"Nombre actual: {self.__nombre}\n"
              f"Masa actual: {self.__masa_kg:2e}\n"
              f"Modificaciones totales: {self._conteo_modificaciones}\n"
              "\nUltimos registros:\n")
        for evento in self._historial_eventos:
            print(evento)
        print("** Fin registros **")

    
