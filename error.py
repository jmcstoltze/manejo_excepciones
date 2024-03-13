
class DimensionError(Exception):
    
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None) -> None:
        
        super().__init__(mensaje)
        
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    # Método que retorna string con mensaje personalizado
    def __str__(self):

        # Si solo se ha ingresado el mensaje al crear la excepción
        if self.dimension is None and self.maximo is None:
            
            # retornar el método de la clase padre
            return super().__str__()
        
        # En caso contrario, crear y retornar un mensaje personalizado
        else:
            
            # Se define el mensaje de retorno que viene dado por la excepción
            mensaje_retorno = f'{self.mensaje}\n'

            # Se agrega la dimensión a la cadena del mensaje
            if self.dimension != None:
                mensaje_retorno += f'Valor ingresado: {self.dimension}\n'

            # Se agrega el valor máximo (o mínimo) se agrega a la cadena del mensaje
            if self.maximo != None:
                mensaje_retorno += f'Límite: {self.maximo}\n'

            # Devuelve el mensaje editado
            return mensaje_retorno


if __name__ == "__main__":

    # Cuando recibe un solo argumento
    error1 = DimensionError("ERROR: \n")
    print(error1)

    # Cuando recibe los tres argumentos
    error2 = DimensionError("Mensaje de error", 300, 50)
    print(error2)