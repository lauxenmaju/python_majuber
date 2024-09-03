
lista = ['Burger King', 'Mc Donalds', 'Subway', 'Dominos', 'KFC']
lista2 = ['Whopper', 'Big Mac', 'Supremo Carne', 'Portuguesa', 'Frango empanado']


def ordenacao_natural(lista):
    return sorted(lista)


def ordenacao_customizada(lista, criterio):
    return sorted(lista, key=criterio)


def primeira_letra(s):
    return s[0] if s else ''


ordenado_naturalmente_lista = ordenacao_natural(lista)
print("Ordenação Natural dos Restaurantes:", ordenado_naturalmente_lista)


ordenado_naturalmente_lista2 = ordenacao_natural(lista2)
print("Ordenação Natural dos Pratos:", ordenado_naturalmente_lista2)


ordenado_por_primeira_letra_lista = ordenacao_customizada(lista, primeira_letra)
print("Primeira Letra dos Restaurantes:", ordenado_por_primeira_letra_lista)


ordenado_por_primeira_letra_lista2 = ordenacao_customizada(lista2, primeira_letra)
print("Primeira Letra dos Pratos:", ordenado_por_primeira_letra_lista2)
