# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    index = len(lista) - 1 # el indice es el len de la lista -1, ya que arranca de 0
    if index >= 5:    
        del lista[0]
        del lista[3]
        del lista[3]
    elif index > 0 and index < 4:
        del lista[0]
    elif index <= 1:
        lista = []
    
    return lista
