
from math import radians, cos, sin, asin, sqrt

# default data resource URL
__DEF_URL__ = "https://opensky-network.org/api/states/all"


def filter_of_nearests(list, nearest, start_point):
    """
    Filtering by the coefficient closest to the starting point
    @param (list) list: objects to filtering
    @param (int) nearest: coefficient
    @param (list) start_point: point of start
    @return: filtering result
    """
    _res_list = []
    for item in list:
        distance = calculate_distance(start_point[0], start_point[1], item[6], item[5])
        if distance is not None and nearest >= distance:
            _res_list.append(serialize_item_object(item))
    return _res_list


def serialize_item_object(list_item):
    """
    # Preparing one answer from the value pool
    @param (list) list_item: value pool
    @return (dict): json object
    """
    if not isinstance(list_item, list) and len(list_item) < 6:
        raise Exception("Bad pool for serialize")
    return {
        'callsign': str(list_item[1]).strip(),
        'longitude': list_item[5],
        'latitude': list_item[6]
    }


def calculate_distance(lat1, lon1, lat2, lon2):
        """
        Calculates the distance in kilometers between two points
        given the circumference of the Earth.
        https://en.wikipedia.org/wiki/Haversine_formula
        @param (float) lat1: latitude first point
        @param (float) lon1: longitude first point
        @param (float) lat2: latitude second point
        @param (float) lon2: longitude second point
        @return: filtering result
        """
        if None in [lat1, lon1, lat2, lon2]:
            return None

        # Equatorial radius of the Earth
        EQU_RADIUS = 6367

        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = EQU_RADIUS * c
        return round(km, 4)
