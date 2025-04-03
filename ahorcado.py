import random

def obtener_palabra():
    palabras = ["guitarra", "nebulosa", "relampago", "espejismo", "laberinto", "murmullo", "destello", "zancada", "armadura", "dioses", "carmesi", "epistedio"]
    return random.choice(palabras).lower()

def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = set()
    intentos_maximos = 6
    intentos = 0
    
    print("¡Bienvenido al juego del ahorcado!")
    print(mostrar_palabra(palabra, letras_adivinadas))
    
    while intentos < intentos_maximos:
        letra = input("Ingresa una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has intentado con esa letra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos += 1
            print(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
        
        palabra_mostrada = mostrar_palabra(palabra, letras_adivinadas)
        print(palabra_mostrada)
        
        if "_" not in palabra_mostrada:
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print(f"Has perdido. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_ahorcado()

