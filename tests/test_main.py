
import pytest

from src.main import calculate_cgpa


def test_calculate_cgpa():
    assert calculate_cgpa([8, 9, 7, 10]) == 8.5


def test_empty_grade_points():
    with pytest.raises(ValueError):
        calculate_cgpa([])


def test_invalid_grade_points():
    with pytest.raises(ValueError):
        calculate_cgpa([8, 11])


def test_decimal_grade_points():
    assert calculate_cgpa([8.5, 9.5]) == 9.0