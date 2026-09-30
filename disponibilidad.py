def hay_disponibilidad(laboratorio, inicio, fin, reservas):
    """True si el laboratorio está libre en el intervalo [inicio, fin)."""
    if fin <= inicio:
        raise ValueError("Intervalo inválido: fin debe ser posterior a inicio")
    for r in reservas:
        if r["laboratorio"] != laboratorio or r["estado"] != "confirmada":
            continue
        if inicio < r["fin"] and r["inicio"] < fin:
            return False
    return True