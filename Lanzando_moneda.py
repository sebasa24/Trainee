import random
def lanzar_moneda():
    return random.choice (["cara", "sello"])


print ("Hemos empezado el juego de la moneda.")

name = (input  ("Ingrese P1: "))

name2 = (input ("Ingrese P2: "))




def cara_sello():
    
 cara_o_sello = input(f"{name}, ¿cara o sello?: ").strip().lower()
 if cara_o_sello== "cara":
    print (f"{name2}, tu tienes sello")
    return cara_o_sello
 elif cara_o_sello=="sello":
    print (f"{name2}, tu tienes cara")
    return cara_o_sello
 else:
    print("porfavor escribe cara o sello")
    cara_sello()
eleccion_p1 = cara_sello()

print ("Lanzando moneda..")

resultado = lanzar_moneda()
print (f"¡la moneda cayo en {resultado}!")



if eleccion_p1 == resultado:
    print(f"FELICIDADES {name}, GANASTE")
else:
    print(f"FELICIDADES {name2}, GANASTE")

    
