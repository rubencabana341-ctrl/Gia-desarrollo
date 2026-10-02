import math

def es_primo(numero: int) -> bool:
    """Determina si un número entero es primo."""
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite = int(math.isqrt(numero))
    for i in range(3, limite + 1, 2):
        if numero % i == 0:
            return False
    return True