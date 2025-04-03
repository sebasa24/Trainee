print ("""Calculadora simple""")
try: 
    
  numeros = int(input("Ingresa un numero entero: "))
  numeros2 = int(input("Ingresa otro numero entero: "))

  signos = input("Favor ingresa uno de estos signos (+ , -, *, /): ")

  if signos== "+":
        numero3= numeros+numeros2
        print (f"El total es {numero3}")
  elif signos== "-":
        numero3=numeros-numeros2
        print(f"La diferencia es {numero3}") 
  elif signos== "*":
        numero3=numeros*numeros2
        print(f"El producto es {numero3}")
  elif signos== "/":
      if numeros2== 0:
          print ("Error. No se puede dividir entre cero")
      else:
        numero3=numeros/numeros2
        print(f"El cociente es {numero3}")
  else:
        print("No seas bruto, Pon un signo que si es pedazo de idiota inepto")

except ValueError:
 print("Error: ingresa numeros validos")
