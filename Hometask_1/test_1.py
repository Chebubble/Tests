from Hometask_1.main1 import sort_russia, unic_num, max_value, geo_logs, ids, stats
from unittest import TestCase

class TestHW_1(TestCase):

    def test_return_list(self):
        res = sort_russia(geo_logs)
        self.assertIsInstance(res, list)

    def test_numbers_unic(self):
        res = unic_num(ids)
        self.assertEqual(res, list(set(res)))

    def test_yandex_in(self):
        res = max_value(stats)
        self.assertIn('yandex', res)