import pytest
from fractions import Fraction
from openprocurement.auction.esco.utils import calculate_npv


@pytest.mark.parametrize('test_input,expected', [
    ((0.22, 751.500, 676.350, 10), 698.444), ((0.22, 751.500, 676.350, 10, 95), 678.691),
    ((0.22, 300.600, 270.540, 6), 483.978),  ((0.22, 300.600, 270.540, 6, 125), 460.946),
    ((0.22, 225.450, 202.905, 4), 499.595),
    ((0.22, 75.150, 67.635, 2), 234.309),
], ids=['bid1', 'bid1(incomplete period)',
        'bid2', 'bid2(incomplete period)',
        'bid3',
        'bid4',
        ])
def test_npv_calculation(test_input, expected):
    assert round(float(calculate_npv(*test_input)), 3) == expected
