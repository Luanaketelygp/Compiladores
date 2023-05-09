def identificar_padrao(cadeia, padrao):
    n = len(cadeia)
    m = len(padrao)
    indice_padrao = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if cadeia[i + j] != padrao[j]:
                match = False
                break
        if match:
            indice_padrao.append(i)
    return indice_padrao

cadeia = "abcabcabc"
padrao = "abc"

indices = identificar_padrao(cadeia, padrao)
print("Padrões encontrados:")
for indice in indices:
    print(indice)
