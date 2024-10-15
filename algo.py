import ast

# Tu lista original
lista = ["(1, 'IVA TASA GENERAL 21%', 21.0)"]

# Extraer el string y convertirlo en una tupla
tupla = ast.literal_eval(lista[0])

print(f" {tupla}  {type(tupla)}")  # Salida: (