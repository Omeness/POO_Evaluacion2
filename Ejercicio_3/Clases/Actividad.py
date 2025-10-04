from datetime import datetime

class Actividad:
    # Almacenamos los id para verificar que no se repitan
    _id_unico = set()

    def __init__(self, id_actividad, nombre:str, duracion_min:int):

        # Verificaciones (id unico, valor existente o positivo)
        if id_actividad in type(self)._id_unico: 
            raise Exception(f"El ID '{id_actividad}' ya existe")
        if not nombre: raise Exception("El nombre no puede estar vacio")
        if duracion_min < 1: raise Exception("La duracion debe ser mayor o igual a uno")
        type(self)._id_unico.add(id_actividad)
        
        self.__id_actividad = id_actividad
        self.__nombre = nombre
        self.__duracion_min = duracion_min
        self.__historial_eventos = []

    def _registrar_historial(self, campo_modificado, valor_anterior, valor_nuevo):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__historial_eventos.append(
            f"[{fecha}]"
            f"Campo modificado: {campo_modificado}"
            f"|Valor anterior: {valor_anterior} |Valor nuevo: {valor_nuevo}"
            )

    @property
    def id_actividad(self):
        return self.__id_actividad
    
    @property
    def ver_historial(self):
        for evento in self.__historial_eventos:
            print(evento)
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise Exception("El nombre no puede estar vacio")
        self._registrar_historial("Nombre",self.__nombre, nuevo_nombre)
        self.__nombre = nuevo_nombre
        print(f"Nombre actualizado a {nuevo_nombre}.")
    
    @property
    def duracion_min(self):
        return self.__duracion_min
    
    @duracion_min.setter
    def actualizar_duracion(self, nueva_duracion):
        if nueva_duracion < 1:
            raise Exception("La duracion debe ser mayor o igual a uno")
        self._registrar_historial("Duracion", self.__duracion_min, nueva_duracion)
        self.__duracion_min = nueva_duracion
        print(f"Duracion actualizada a {nueva_duracion} min.")