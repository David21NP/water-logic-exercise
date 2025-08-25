import pytest

from main import all_tests, calc_water_3

@pytest.mark.parametrize(
    ["arr", "result"],
    all_tests,
)
def test_calc_3(arr, result):
    calc = calc_water_3(arr)
    print()
    print("Para el vector:", arr)
    print("Hay", calc, "conteos de agua.")
    print("Deberia contar", result, "conteos de agua.")

    assert calc == result
