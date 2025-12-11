# ignore este codigo, no lo modifique
def doSomething(x):
    a = ['gato', 'perro', 'rana', 'oveja']
    b = [x] * len(a)
    c = [x+x+x] * len(a)
    return ''.join(map(lambda d,e,f: d[e:f], a, b, c))
# fin del codigo a ignorar



# encuentre los errores en el siguiente codigo
num = input("Ingrese un numero entero: ")

res = num // num

    text = doSomething(res)

print(texto