
# Importaciones necsarias
from error import DimensionError
from foto import Foto

# Mensaje de error predeterminado
msj_error = "Se debe ingresar un valor numérico entero"

# Dimensiones y ruta iniciales
ancho = 250
alto = 180
ruta = "Mi ruta"

# Instancia inicial del objeto Foto
foto = Foto(ancho, alto, ruta)

# Se imprimen en pantalla
print(f'''
    Dimensiones de la imagen:
    -------------------------
      - ancho: {foto.ancho}
      - alto: {foto.alto}
      - ruta: {foto.ruta}
''')

# Ciclo infinito para ingresar y validar al ancho
while True:

    # Se intenta capturar el nuevo ancho de la imagen
    try:
        nuevo_ancho = (input("Ingrese el nuevo ANCHO de la imagen: \n"))
        foto.ancho = int(nuevo_ancho) # Setea el nuevo valor
    
    # Excepción en caso de que se ingresen valores no enteros
    except ValueError as e:

        # Instancia del error con el mensaje predeterminado como único parámetro
        e = DimensionError(f"{msj_error} \n")
        print(e) # Imprime el mensaje en pantalla

    # Excepción en caso de que no pase las validación del método setter
    except DimensionError as e:
        print(e) # Imprime el mensaje personalizado en pantalla
        continue

    else:
        break # Rompe el ciclo

# Ciclo infinito para ingresar y validar al alto
while True:

    # Se intenta capturar el nuevo alto de la imagen
    try:
        nuevo_alto = (input("Ingrese el nuevo ALTO de la imagen: \n"))
        foto.alto = int(nuevo_alto) # Setea el nuevo valor
    
    # Excepción en caso de que se ingresen valores no enteros
    except ValueError as e:

        # Instancia del error con el mensaje predeterminado como único parámetro
        e = DimensionError(f"{msj_error} \n")
        print(e) # Imprime el mensaje en pantalla

    # Excepción en caso de que no pase las validación del método setter
    except DimensionError as e:
        print(e) # Imprime el mensaje personalizado en pantalla
        continue

    else:
        break # Rompe el ciclo


# Imprime en pantalla los atributos actualizados del objeto
print(f'''
    Dimensiones modificadas con éxito!!
      
    Nuevas dimensiones de la imagen:
    -------------------------------- 
      - nuevo ancho: {foto.ancho}
      - nuevo alto: {foto.alto}
      - ruta: {foto.ruta}
''')
