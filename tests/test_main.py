import pytest

from src.main import calculate_cgpa, main


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


def test_zero_cgpa():
    assert calculate_cgpa([0, 0, 0]) == 0.0


def test_negative_grade_points():
    with pytest.raises(ValueError):
        calculate_cgpa([8, -1, 9])


def test_non_numeric_grade_points():
    with pytest.raises(ValueError):
        calculate_cgpa([8, "bad", 9])


def test_main_rejects_empty_grade_input(monkeypatch, capsys):
    responses = iter(["Alice", ""])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    main()

    captured = capsys.readouterr()
    assert "Error: Grade points cannot be empty." in captured.out
