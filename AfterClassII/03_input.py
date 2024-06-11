nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")

linea = f"{nombre},{apellido},{edad}"

with open("clientes.txt", "w") as f:
    f.write(linea+"\n")

print("Fin de programa")