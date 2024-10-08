# Paso 1: Leer archivo de texto
def leer_archivo(file_path):
    try:
        with open(file_path, 'r') as file:
            contenido = file.read().strip()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return None

# Paso 2: Implementar el Suffix Array
def construir_suffix_array(texto):
    # Generar una lista de sufijos y sus índices
    sufijos = [(texto[i:], i) for i in range(len(texto))]
    
    # Ordenar los sufijos lexicográficamente
    sufijos_ordenados = sorted(sufijos)
    
    # Retornar los índices de los sufijos ordenados
    suffix_array = [sufijo[1] for sufijo in sufijos_ordenados]
    return suffix_array

# Paso 3: Función principal para ejecutar el programa
def main():
    # Nombre del archivo de texto (puedes cambiarlo por el archivo que desees)
    archivo = 'entrada.txt'
    
    # Leer el contenido del archivo
    cadena = leer_archivo(archivo)
    
    if cadena:
        # Construir el Suffix Array
        suffix_array = construir_suffix_array(cadena)
        
        # Mostrar el Suffix Array
        print("Suffix Array:", suffix_array)

if __name__ == "__main__":
    main()
