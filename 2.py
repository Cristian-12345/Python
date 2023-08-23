palabra = input("Ingrese una palabra: ")

verificacion_palabra = "SI ES un palindromo."

for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-(i + 1)]:
        verificacion_palabra = "NO ES un palindromo."
        break

print(verificacion_palabra)