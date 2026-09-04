import pytest

from helpers import (
    validate_amount,
    validate_non_empty_text,
    validate_date
)


def test_valid_amount():
    assert validate_amount("250") == 250.0


def test_invalid_amount():
    with pytest.raises(ValueError):
        validate_amount("abc")


def test_empty_category():
    with pytest.raises(ValueError):
        validate_non_empty_text("")


def test_valid_date():
    assert validate_date("2026-09-04") == "2026-09-04"


def test_invalid_date():
    with pytest.raises(ValueError):
        validate_date("2026-50-99")