
# Se importa desde error.py
from error import DimensionError

# Definición de la clase Foto
class Foto():

    # Constantes para un valor máximo y mínimo
    MAX = 2500
    MIN = 1

    # Constructor de la clase foto
    def __init__(self, ancho: int, alto: int, ruta: str) -> None:

        # Atributos de la foto
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    # Método getter retorna ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, ancho) -> None:
        
        # Si el ancho no alcanza el valor mínimo
        if ancho < self.MIN:
        
            # Se levanta la excepción correspondiente 
            raise DimensionError(f"El alto es menor al valor mínimo {self.MIN}", ancho, self.MIN)
        
        # Si el ancho es mayor al valor establecido
        elif ancho > self.MAX:

            # Se levanta la excepción correspondiente
            raise DimensionError(f"El ancho excede el valor máximo {self.MAX}", ancho, self.MAX)    
        self.__ancho = ancho

    # Método getter retorna alto
    @property
    def alto(self) -> int:
        return self.__alto

    # Método setter para el alto
    @alto.setter
    def alto(self, alto) -> None:
        
        # Si el alto no alcanza el valor mínimo
        if alto < self.MIN:
        
            # Se levanta la excepción correspondiente 
            raise DimensionError(f"El alto es menor al valor mínimo {self.MIN}", alto, self.MIN)
        
        # Si el alto es mayor al valor establecido
        elif alto > self.MAX:
            
            # Se levanta la excepción correspondiente 
            raise DimensionError(f"El alto excede el valor máximo {self.MAX}", alto, self.MAX)
        
        self.__alto = alto


# Módulo de pruebas del archivo foto.py
if __name__ == "__main__":

    # Se intenta modificar un parámetro con valor no permitido
    try:
        f = Foto(None, None, None) # Instancia cualquiera de la imagen
        f.ancho = 3500
        
    except DimensionError as e:
        print(e) # Se espera que imprima el error
    
    # Se intenta modificar un parámetro con valor no permitido
    try:
        f.alto = 0
        
    except DimensionError as e:
        print(e) # Se espera que imprima el error
 
    # Se intenta modificar un parámetro con valor no permitido
    try:
        f.alto = 4000
        
    except DimensionError as e:
        print(e) # Se espera que imprima el error

    # Se intenta modificar un parámetro con valor no permitido
    try:
        f = Foto(250, 180, "mi ruta")
        f.alto = 0
        
    except DimensionError as e:
        print(e) # Se espera que imprima el error
