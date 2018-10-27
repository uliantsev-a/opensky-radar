from locator_opensky import core
import requests


def nearest_ships(nearest=450, start_point=None):
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

    r = requests.get(core.DEF_URL)
    return core.clipping_far_ships(r.json()['states'], nearest, start_point)


def __main__():
    count_ships = 0
    for item in nearest_ships():
        count_ships += 1
        print("Callsign: {callsign}. "
              "Coord: lon {longitude}, lan {latitude}".format(**item))
    print("Len nearest objects: {}".format(count_ships))
