
def get_rose_point(i):
    rose_points = [
        'N',
        'NNE',
        'NE',
        'ENE',
        'E',
        'ESE',
        'SE',
        'SSE',
        'S',
        'SSW',
        'SW',
        'WSW',
        'W',
        'WNW',
        'NW',
        'NNW'
    ]
    return rose_points[i]


# Assumption : first sector is North and is id=0
def get_wind_rose(wind_deg):
    """

    :param wind_deg: 0 to 360 degrees
    :return: Wind rose as in N, NNW etc.
    """

    if wind_deg < 0:
        return None, None
    wind_deg = wind_deg % 360
    for i in range(0, 16):
        #print('i is ' + i.__str__())
        x_upper = 11.25 + (i * 22.5)
        x_lower = x_upper - 22.5
        if x_lower < 0.0:
            x_lower = x_lower + 360.0
        #print('x_lower is ' + x_lower.__str__())
        #print('x_upper is ' + x_upper.__str__())
        if i == 0 and (wind_deg >= x_lower or wind_deg < x_upper):
            rose_point = get_rose_point(i)
            return i, rose_point
        elif wind_deg >= x_lower and wind_deg < x_upper:
            rose_point = get_rose_point(i)
            return i, rose_point


# if __name__ == '__main__':
#     for wind_dir in range(0, 450):
#         rose_point = get_wind_rose(wind_dir)
#         print('wind_dir : ' + wind_dir.__str__() + ', rose_point : ' + rose_point.__str__())
