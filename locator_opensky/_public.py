from locator_opensky import _core
import requests


def get_nearest_ships(nearest=450, start_point=None):
    """ Getting the nearest objects
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

    r = requests.get(_core.__DEF_URL__)
    nearest_ships = _core.filter_of_nearests(r.json()['states'], nearest, start_point, )
    return nearest_ships


def __main__():
    locator_list = get_nearest_ships()
    for item in locator_list:
        print("Callsign: {callsign}. "
              "Coord: lon {longitude}, lan {latitude}".format(**item))
    print("Len nearest objects: {}".format(len(locator_list)))
