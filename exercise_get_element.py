# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    if indice > len(lista) - 1 or indice < -(len(lista)):
        return None
    else:
        return lista[indice]

# nums = [1, 2, 3, 4]
# index = int(input("Enter an index: "))
# nums_element = get_element(nums, index)
# print(nums_element)
