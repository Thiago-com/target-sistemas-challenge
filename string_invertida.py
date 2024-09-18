def string_invertida(f):
    invertida = ''
    for i in range(len(f) - 1, -1, -1):
        invertida += f[i]
    return invertida

frase = input("Digite uma frase: ")

resultado = string_invertida(frase)
print(f'Frase invertida: {resultado}')