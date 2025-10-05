from datetime import datetime


class Publicacion:
    # Atributo de clase para almacenar IDs y verificar que sean unicas
    _id_unico = set()

    def __init__(self, id_publicacion, titulo:str, anio):

        # Validaciones (ID unico, valor existente, año valido)
        if id_publicacion in type(self)._id_unico: 
            raise Exception(f"El identificador '{id_publicacion}' ya existe")
        if not titulo.split(): raise Exception("El atributo no puede estar vacio")
        if anio < 1450: raise Exception("El año debe ser mayor o igual a 1450")
        type(self)._id_unico.add(id_publicacion)

        self.__id_publicacion = id_publicacion
        self.__titulo = titulo
        self.__anio = anio
        self.__historial_eventos = []
    
    def __registrar_evento(self, detalle):
        # Metodo para registrar eventos con fecha y hora en historial_eventos
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__historial_eventos.append(f"[{fecha}] [{detalle}]")

    @property
    def titulo(self):
        """
        Getter con setter para actualizar el titulo de la publicacion.
        Valida que sea un dato existente y deja registro en historial_eventos
        """
        return self.__titulo

    @titulo.setter
    def actualizar_titulo(self, nuevo_titulo):
        if not nuevo_titulo.split():
            raise Exception("El nombre no puede estar vacio")
        self.__registrar_evento(f"Se actualizó el titulo de '{self.__titulo}' a '{nuevo_titulo}'")
        self.__titulo = nuevo_titulo
        print(f"Se actualizó el titulo de '{self.__titulo}' a '{nuevo_titulo}'")
    
    @property
    def anio(self):
        """
        Getter con setter para actualizar el año de publicacion.
        Valida que sea un año valido y deja registro en historial_eventos
        """
        return self.__anio

    @anio.setter
    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio < 1450:
            raise Exception("El año debe ser mayor o igual a 1450")
        self.__registrar_evento(f"Se actualizó el año de '{self.__anio}' a '{nuevo_anio}'")
        self.__anio = nuevo_anio
        print(f"Se actualizó el año de '{self.__anio}' a '{nuevo_anio}'")

    # Metodo para visualizar los eventos registrados
    def historial_eventos(self):
        print("--- Historial Eventos ---\n")
        for evento in self.__historial_eventos:
            print(evento)
        print("** Fin **")