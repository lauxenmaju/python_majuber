#ordenação total 
class Restaurantes:
    def __init__(self,nome,alimento,nota):
        self.nome = nome
        self.alimento = alimento
        self.nota = nota
    def __repr__(self):
        return repr((self.nome,self.alimento,self.nota))

restaurante_obj = [
    Restaurantes('Burger King', 'Whopper', 5),
    Restaurantes('Mc Donalds', 'Big Mac', 6),
    Restaurantes('Subway', 'Supremo Carne', 4),
    Restaurantes('Dominos', 'Portuguesa', 7),
    Restaurantes('KFC', 'Frango', 8)
]


restaurantes_ordenados = sorted(restaurante_obj, key=lambda r: r.nota, reverse=True)

for restaurante in restaurantes_ordenados:
    print(restaurante)