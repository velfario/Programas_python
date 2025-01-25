import argparse


def esprimo(n):
    if n <= 0:
        return print("el número no es válido")
    
    primo = True
    for i in range(2, n):
        if n%i == 0:
            primo = False
            num1 = int(i)
            num2 = int(n/i)
            break
    if primo:
        print('es primo')
    else:
        print("no es primo porque {0}*{1} = {2}".format(num1, num2, num1*num2))


# en esta sección estamos comunicandonos y haciendo que lo que metamos en consola se meta en la variable n
# esto se repite siempre con pequeñas modificaciones
parser = argparse.ArgumentParser()
parser.add_argument("n", type = int)
args = parser.parse_args()

n =  args.n
esprimo(n)