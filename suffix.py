from collections import Counter

# Leer archivo de texto y agregar símbolo $
def leer_archivo(file_path):
    try:
        with open(file_path, 'r') as file:
            contenido = file.read().strip()
        # Agregar el símbolo $ al final de la cadena
        return contenido + '$'
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return None

# Construir Suffix Array
def construir_suffix_array(texto):
    # Crear una lista de sufijos con sus posiciones originales
    sufijos = [(texto[i:], i) for i in range(len(texto))]
    # Ordenar lexicográficamente los sufijos
    sufijos_ordenados = sorted(sufijos)
    # Retornar solo las posiciones originales de los sufijos ordenados
    suffix_array = [sufijo[1] for sufijo in sufijos_ordenados]
    return suffix_array

def construir_bwt(texto, suffix_array): # Implementación del Burrows-Wheeler Transform
    bwt = ''
    n = len(texto)
    for i in suffix_array:
        if i == 0:  # Si i es 0, el carácter anterior es el último de la cadena
            bwt += texto[n-1]
        else:
            bwt += texto[i-1]
    return bwt

def construir_C(bwt): # Construir el arreglo C
    conteo = Counter(bwt)
    caracteres_ordenados = sorted(conteo.keys())
    
    C = {}
    total = 0
    for char in caracteres_ordenados:
        C[char] = total
        total += conteo[char]
    return C

def construir_Occur(bwt):
    occur = {}
    for char in set(bwt):
        occur[char] = [0] * (len(bwt) + 1)

    for i in range(1, len(bwt) + 1):
        char = bwt[i - 1]
        for c in occur:
            occur[c][i] = occur[c][i - 1]
        occur[char][i] += 1
    
    return occur

def main():
    archivo = 'entrada.txt'
    
    cadena = leer_archivo(archivo)
    
    if cadena:
        print(f"Texto leído: {cadena}")
        
        suffix_array = construir_suffix_array(cadena)
        print(f"Suffix Array: {suffix_array}")
        
        bwt = construir_bwt(cadena, suffix_array)
        print(f"BWT: {bwt}")
        
        C = construir_C(bwt)
        print(f"Arreglo C: {C}")
        
        Occur = construir_Occur(bwt)
        print("Arreglo Occur:")
        for char, lista in Occur.items():
            print(f"{char}: {lista}")

if __name__ == "__main__":
    main()