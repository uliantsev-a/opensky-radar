"""
locator_opensky - Returning the result by the API OpenSky,
                  but with filtering the reach of the radius.
"""

from math import radians, cos, sin, asin, sqrt
import requests

__author__ = 'Ulyantsev Aleksandr (it.bumerang@gmail.com)'
__license__ = 'MIT'
__version__ = '1.0'

__all__ = ["get_nearest_ships"]

# default data resource URL
__DEF_URL__ = "https://opensky-network.org/api/states/all"


def get_nearest_ships(nearest=450, start_point=None):
    """
    Getting the nearest objects
    @param (int) nearest: objects to filtering
    @param (list) start_point: coefficient
    @return (list): result
    """
    if start_point is None:
        # 48.8566, 2.3516 - default coordinates of Paris
        start_point = [48.8566, 2.3516]
    elif not (isinstance(start_point, list) and
              len(start_point) != 2 and
              isinstance(start_point[0], float) and
              isinstance(start_point[1], float)):
        raise Exception("Wrong coordinates are given")
    if not isinstance(nearest, int):
        raise Exception("Exception due to not true "
                        " the nearest radius")

    r = requests.get(__DEF_URL__)
    nearest_ships = __filter_of_nearests__(r.json()['states'],
                                           nearest, start_point, )
    return nearest_ships


def __filter_of_nearests__(list, nearest, start_point):
    """
    Filtering by the coefficient closest to the starting point
    @param (list) list: objects to filtering
    @param (int) nearest: coefficient
    @param (list) start_point: point of start
    @return: filtering result
    """
    _res_list = []
    for item in list:
        distance = __calculate_distance__(start_point[0], start_point[1],
                                          item[6], item[5])
        if distance is not None and nearest >= distance:
            _res_list.append(__serialize_item_object__(item))
    return _res_list


def __serialize_item_object__(list_item):
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


def __calculate_distance__(lat1, lon1, lat2, lon2):
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


if __name__ == "__main__":
    locator_list = get_nearest_ships()
    for item in locator_list:
        print("Callsign: {callsign}. "
              "Coord: lon {longitude}, lan {latitude}".format(**item))
    print("Len nearest objects: {}".format(len(locator_list)))
