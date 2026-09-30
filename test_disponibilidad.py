import pytest
from disponibilidad import hay_disponibilidad

RESERVAS = [{"laboratorio": "L1", "estado": "confirmada", "inicio": 10, "fin": 12}]

def test_horario_libre():
    assert hay_disponibilidad("L1", 12, 14, RESERVAS)

def test_cruce_parcial():
    assert not hay_disponibilidad("L1", 11, 13, RESERVAS)

def test_cruce_total():
    assert not hay_disponibilidad("L1", 9, 13, RESERVAS)

def test_otro_laboratorio():
    assert hay_disponibilidad("L2", 10, 12, RESERVAS)

def test_reserva_cancelada_no_bloquea():
    canceladas = [{**RESERVAS[0], "estado": "cancelada"}]
    assert hay_disponibilidad("L1", 10, 12, canceladas)

def test_intervalo_invalido():
    with pytest.raises(ValueError):
        hay_disponibilidad("L1", 14, 12, RESERVAS)