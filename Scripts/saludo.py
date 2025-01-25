#Cree un programa que una vez ejecutado en la console se le envíe como opcion el saludo "Hola".
#El programa debe responder:
#* Con 1/2 de probabilidad la respuesta "Hola, ¿cómo estás?"
#* Con probabilidad 1/4 la respuesta "Hola, me llamo Computina"
#* Con probabilidad 1/4 la respuesta "Háblale a la mano"
#* Si no se pone este texto opcional debería responder "Primero, saluda!!"
import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--saludo", type=str, default="")
args = parser.parse_args()

saludo = args.saludo
if saludo == "Hola":
    num = random.randint(0,100)
    if num <=50:
        print("Hola, cómo estas")
    elif num <= 75:
        print('Hola, me llamo Computina')
    else:
        print("Háblale a la mano")
else:
    print("Primero, saluda!!")
