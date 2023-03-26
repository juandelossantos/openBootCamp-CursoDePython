def es_bisiesto(anio):
    """
    Determina si un año es bisiesto o no.

    Parámetros:
    - anio: int, el año a evaluar.

    Retorna:
    - True si el año es bisiesto, False si no lo es.
    """
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True


if es_bisiesto(2022):
    print("es bisiesto")
else:
    print('no es bisiesto')
