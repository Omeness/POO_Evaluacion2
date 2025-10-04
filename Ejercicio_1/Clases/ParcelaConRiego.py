from datetime import datetime
from Ejercicio_1.Clases.Parcela import Parcela


class ParcelaConRiego(Parcela):
    def __init__(self, id_parcela, superficie_ha, cultivo_actual, litros_disponibles,
                 tasa_riego_l_ha, umbral_min_litros, estado="activa"):
        super().__init__(id_parcela, superficie_ha, cultivo_actual, estado)

        if litros_disponibles < 0: 
            raise Exception("Los litros disponibles no pueden ser un numero negativo")
        if tasa_riego_l_ha <= 0: raise Exception("La tasa de riego debe ser mayor a cero")
        if umbral_min_litros < 0: raise Exception("El umbral no puede ser un numero negativo")
        
        self.estado = estado
        if self.estado == "activa": 
            self.estado_riego = "habilitado"
        else:
            self.estado_riego = "inhabilitado"

        self.__litros_disponibles = litros_disponibles
        self.tasa_riego_l_ha = tasa_riego_l_ha
        self.umbral_min_litros = umbral_min_litros
        self.__eventos_riego = []
    
    def _registrar_riego(self, litros_solicitados, litros_aplicados, saldo_antes, saldo_despues, modo):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self.__eventos_riego.append(f"[{fecha}] "
                                    f"[Solicitado: {litros_solicitados}L - "
                                    f"Aplicado: {litros_aplicados}L] ["
                                    f"Saldo anterior: {saldo_antes}L -> "
                                    f"Saldo despues: {saldo_despues}L]  Modo: {modo}")
    
    @property
    def litros_disponibles(self):
        return self.__litros_disponibles

    @litros_disponibles.setter
    def cargar_agua(self, litros):
        if litros < 1:
            raise Exception(f"La cantidad de litros debe ser mayor a cero. Valor ingresado: '{litros}'")
        nivel_anterior = self.__litros_disponibles
        nivel_actual = self.__litros_disponibles + litros
        detalle = f"Se cargaron {litros}lts. Nivel anterior: {nivel_anterior}lts. Nivel actual: {nivel_actual}"
        self._registrar_evento("Carga agua", detalle)
        self.__litros_disponibles += litros
        print("Carga de agua exitosa")
    
    @property
    def eventos_riego(self):
        print("--- Historial riego ---")
        for evento in self.__eventos_riego:
            print(evento)
        print("**  Fin registros **")

    def configurar_tasa(self, l_ha):
        if l_ha < 1:
            raise Exception(f"La tasa de l/ha debe ser mayor a cero. Valor ingresado: '{l_ha}'")
        detalle = f"Tasa anterior: {self.tasa_riego_l_ha}. Nueva tasa: {l_ha}"
        self._registrar_evento("Configuracion tasa", detalle)
        self.tasa_riego_l_ha = l_ha
        print("Tasa configurada con exito")

    def configurar_umbral(self, litros):
        if litros < 0:
            raise Exception(f"El umbral no puede ser un numero negativo. Valor ingresado: '{litros}'")
        detalle = f"Umbral anterior: {self.umbral_min_litros} Nuevo umbral: {litros}"
        self._registrar_evento("Configuracion umbral", detalle) 
        self.umbral_min_litros = litros
        print("Umbral configurado con exito")
  
    def habilitar_riego(self):
        if self.estado == "inactiva":
            raise Exception("La parcela no esta activa")
        if self.estado_riego == "inhabilitado":
            self.estado_riego = "habilitado"
            self._registrar_evento("Habilitacion riego","")
            print("Riego habilitado con exito")
        else:
            print("Error: El riego ya esta habilitado")

    def inhabilitar_riego(self):
        if self.estado == "inactiva":
            raise Exception("La parcela no esta activa")
        if self.estado_riego == "habilitado":
            self.estado_riego = "inhabilitado"
            self._registrar_evento("Inhabilitacion riego","")
            print("Riego inhabilitado con exito")
        else:
            print("Error: El riego ya esta inhabilitado")

    def regar_automatico(self, modo):
        if self.estado == "inactiva":
            raise Exception("[Riego prohibido] La parcela no esta activa")
        if self.estado_riego == "inhabilitado":
            raise Exception("[Riego prohibido] El riego esta inhabilitado")
        if self.tasa_riego_l_ha < 1:
            raise Exception("[Riego prohibido] La tasa de riego es menor o igual a 0")
        demanda = self.superficie_ha * self.tasa_riego_l_ha
        saldo_anterior = self.__litros_disponibles
        if modo == "estricto":
            if self.__litros_disponibles - demanda >= self.umbral_min_litros:
                self.__litros_disponibles -= demanda
                self._registrar_riego(demanda, demanda, saldo_anterior, self.__litros_disponibles, modo)
                self._registrar_evento("Activacion riego", "Modo: estricto")
                print("Se ha regado en modo estricto")
            else:
                print("Error: No hay suficiente agua")
        elif modo == "parcial":
            riego_max = self.__litros_disponibles - self.umbral_min_litros
            if riego_max > 0:
                litros_aplicados = min(demanda, riego_max)
                saldo_despues = self.__litros_disponibles - litros_aplicados
                self._registrar_riego(demanda, litros_aplicados, saldo_anterior, saldo_despues, modo)
                self._registrar_evento("Activacion riego", "Modo: parcial")
                print("Se ha regado en modo parcial")
            else:
                print("Error: No hay suficiente agua")
        else:
            print("Error: El modo debe ser 'parcial' o 'estricto'")