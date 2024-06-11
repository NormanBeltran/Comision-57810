try:
    edad = input("Ingrese su edad:")
    edad = int(edad)
except Exception as e:
    print(f"Hubo un error, lo ingresado no es un entero {e}")    
else:
    print(f"Ud tiene {edad} años")    