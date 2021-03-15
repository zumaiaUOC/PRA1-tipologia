"""
Un archivo robots.txt indica a los rastreadores de los buscadores qué páginas o archivos de tu sitio pueden solicitar y
cuáles no. Principalmente, se utiliza para evitar que las solicitudes que recibe tu sitio lo sobrecarguen; no es un
mecanismo para impedir que una página web aparezca en Google. Si lo que buscas es esto último, debes usar directivas
noindex o proteger esas páginas con contraseña.
"""

from utils import robots_to_df
import os

cwd = os.getcwd()
print(cwd)

with open("../data/tiendas.txt", encoding="utf-8") as file:
    tiendas = [l.rstrip("\n") for l in file]

i = 0
for j in range(5):
    i = i+1
    globals()["tienda"+str(j)] = tiendas[j]
    print("\n"+"tienda"+str(j)+"\n")
    print(robots_to_df(globals()["tienda"+str(j)]))


