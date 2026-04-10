# Ejercicio 9: Verificar si una lista está vacía

def is_empty(lista):
    """
    Determina si una lista está vacía.

    Args:
        lista: Una lista de elementos

    Returns:
        True si la lista está vacía, False en caso contrario
    """
    quant = len(lista)
    if quant == 0:
        return True
    else:
        return False