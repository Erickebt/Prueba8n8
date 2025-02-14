def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def main():
    print("Seleccione operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Ingrese opción (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))

            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
            
            siguiente = input("¿Desea realizar otra operación? (s/n): ")
            if siguiente.lower() != 's':
                break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()