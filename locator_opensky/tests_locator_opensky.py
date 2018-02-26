import unittest
from  locator_opensky import __inside as locator_opensky
import requests


class TestLocatorOpenSky(unittest.TestCase):
    start_point = [48.856651, 2.351691]  # Paris
    # [[Berlin], [Orlean-Lyare]]
    list_right_pool = [[0, 'OAL224', 2, 3, 4, 13.406888, 52.517481],
                       [0, 'VIR3N   ', 2, 3, 4, 1.879132, 47.943628]]

    test_false_coord = [48.8566, None, 48.8566, '2.2551']

    between_about = 877  # Between Paris and Berlin Approximately 850 km
    nearest = 450  # maximum radius for locator

    def setUp(self):
        self.right_res = [locator_opensky.__serialize_item_object__(
            self.list_right_pool[1])]

    def test_get_nearest(self):
        res_filter = locator_opensky.__filter_of_nearests__(
            self.list_right_pool, self.nearest, self.start_point)
        # Test for filter right
        self.assertCountEqual(self.right_res, res_filter)

    def test_url_opensky(self):
        r = requests.get(locator_opensky.__DEF_URL__)
        # True response
        self.assertTrue(r.ok)
        # Content Checking
        self.assertTrue(len(r.json()) > 0)
        self.assertTrue('states' in r.json().keys())

    def test_calculate_distance(self):
        # Check that the count returns a number
        for pool in self.list_right_pool:
            distance = locator_opensky.__calculate_distance__(
                self.start_point[0], self.start_point[1], pool[6], pool[5])
            self.assertTrue(isinstance(distance, (int, float)))

        # Check if the coordinates are incorrect
        none_dist = (locator_opensky.
                     __calculate_distance__(*self.test_false_coord))
        self.assertEqual(none_dist, None)
        self.assertFalse(isinstance(none_dist, int))

        beet_dist = locator_opensky.__calculate_distance__(
            self.start_point[0], self.start_point[1],
            self.list_right_pool[0][6],
            self.list_right_pool[0][5])
        # test of value right calculate
        self.assertAlmostEqual(round(beet_dist), round(self.between_about))


if __name__ == '__main__':
    unittest.main()
