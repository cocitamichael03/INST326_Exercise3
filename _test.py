import math
from bulk_pricing import get_cost

def test_bulk_pricing_happy_path():
    assert math.isclose(get_cost(5), 3.75)
    assert math.isclose(43.2, get_cost(60))
    assert math.isclose(get_cost(500), 350)
    assert math.isclose(get_cost(1500), 1005)

def test_bulk_pricing_edge_cases():
    assert math.isclose(get_cost(49), 36.75)
    assert math.isclose(get_cost(50), 36)
    assert math.isclose(get_cost(999), 699.3)
    assert math.isclose(get_cost(1000), 670)