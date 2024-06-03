
def suma():
    num1=int(input("Introduce el numero1 -> "))
    num2=int(input("Introduce el numero2 -> "))
    resultado=num1+num2
    print(f"El resultado de {num1}+{num2} es {resultado}")

def resta():
    num1=int(input("Introduce el numero1-> "))
    num2=int(input("Introduce el numero2-> "))
    resultado=num1-num2
    print(f"El resultado de {num1}-{num2} es {resultado}")

def multiplicacion():
    num1=int(input("Introduce el numero1-> "))
    num2=int(input("Introduce el numero2-> "))
    resultado=num1*num2
    print(f"El resultado de {num1}*{num2} es {resultado}")

def division():
    num1=int(input("Introduce el numero1-> "))
    while True:
        num2=int(input("Introduce el numero2-> "))
        if num2==0:
            print("Lo siento no puedes dividir entre 0")
        else:
            break
    resultado=num1/num2
    print(f"El resultado de {num1}/{num2} es {resultado}")

print("Bienvenido a esta calculadora hecha en Python!")
while True:
    opcion=int(input("""Por favor elige el numero que corresponde la operacion desea realizar:
                1.Suma / 2.Resta / 3.Multiplicación / 4.División\n"""))

    match opcion:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            multiplicacion()
        case 4:
            division()
        case _:
            print("La opcion selecionada es invalida")

    resp=input("Para continuar presione enter, para salir escriba s y luego presione enter\n").upper()
    if resp=="S":
        print("Nos vemos pronto!")
        break