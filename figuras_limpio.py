import math

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    if radio <= 0:
        raise ValueError("El radio debe ser mayor a cero.")
    return math.pi * radio ** 2

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dadas su base y altura."""
    if base <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores a cero.")
    return base * altura

def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo dadas su base y altura."""
    if base <= 0 or altura <= 0:
        raise ValueError("Las dimensiones deben ser mayores a cero.")
    return (base * altura) / 2

if __name__ == "__main__":
    print(f"Área Círculo (r=5): {calcular_area_circulo(5):.2f}")
    print(f"Área Rectángulo (b=4, h=6): {calcular_area_rectangulo(4, 6):.2f}")
    print(f"Área Triángulo (b=4, h=6): {calcular_area_triangulo(4, 6):.2f}")