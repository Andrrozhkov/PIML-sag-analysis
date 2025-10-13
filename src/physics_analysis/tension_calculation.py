# src/physics_analysis/tension_calculation.py
def calculate_wire_tension(span_length, sag, linear_weight, g=9.81):
    """
    Расчет натяжения провода по формуле для нерастяжимой нити
    T ≈ (w * g * L²) / (8 * sag)
    """
    return (linear_weight * g * span_length**2) / (8 * sag)

# tests/test_tension_calculation.py
import pytest
from src.physics_analysis.tension_calculation import calculate_wire_tension

def test_calculate_wire_tension_standard_case():
    """Тест расчета натяжения для стандартного случая"""
    # Arrange
    span_length = 100.0  # м
    sag = 5.0           # м
    linear_weight = 1.2  # кг/м
    expected_tension = 2943.0  # Н (примерно)
    
    # Act
    actual_tension = calculate_wire_tension(span_length, sag, linear_weight)
    
    # Assert
    assert abs(actual_tension - expected_tension) < 1.0

def test_calculate_wire_tension_zero_sag_raises_error():
    """Тест, что нулевой провис вызывает ошибку"""
    # Arrange
    span_length = 100.0
    sag = 0.0  # Невозможное значение!
    linear_weight = 1.2
    
    # Act & Assert
    with pytest.raises(ValueError):
        calculate_wire_tension(span_length, sag, linear_weight)
