def min_monedas(monedas, cantidad):
    # Ordenamos las monedas en orden descendente
    monedas.sort(reverse=True)
    
    # Lista para guardar cuántas monedas de cada denominación usaremos
    mon_contador = []
    
    # Recorrer cada denominación
    for moneda in monedas:
        # Determinamos cuántas monedas de esta denominación se pueden usar
        contador = cantidad // moneda
        mon_contador.append((moneda, contador))
        # Reducimos el monto del cambio restante
        cantidad -= contador * moneda
    
    # Si aún queda cambio por dar que no puede ser cubierto por las denominaciones, no es posible
    if cantidad != 0:
        return "No es posible dar el cambio exacto con estas monedas."
    
    return mon_contador

# Ejemplo de uso:
monedas = [1, 2, 5, 10]  # Denominaciones de las monedas
cantidad = 69  # Cantidad de cambio a devolver

resultado = min_monedas(monedas, cantidad)
print("Monedas utilizadas para dar el cambio:")
for moneda, contador in resultado:
    print(f"Moneda de {moneda}: {contador} monedas")