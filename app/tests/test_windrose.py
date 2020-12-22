# author : R.Crouch
# Test wind_rose functions

import pytest
import windrose


# ----------
@pytest.mark.parametrize(
    "wind_deg, expected_wind_rose_id, expected_wind_rose",
    [
        (-1, None, None),
        (0, 0, 'N'),
        (90, 4, 'E'),
        (180, 8, 'S'),
        (270, 12, 'W'),
        (360, 0, 'N'),
        (365, 0, 'N'),
        (45, 2, 'NE'),
        (135, 6, 'SE'),
        (225, 10, 'SW'),
        (315, 14, 'NW'),
    ]
)
def test_get_wind_rose(wind_deg, expected_wind_rose_id, expected_wind_rose):
    wind_rose_id, wind_rose = windrose.get_wind_rose(wind_deg)

    assert wind_rose_id == expected_wind_rose_id
    assert wind_rose == expected_wind_rose
