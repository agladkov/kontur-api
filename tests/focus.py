import os
import unittest

from kontur import FocusClient


class TestKonturFocus(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv('FOCUS_API_KEY', None)
        if api_key is None:
            raise Exception('Set FOCUS_API_KEY env varible')
        self.client = FocusClient(api_key)

    def test_req(self):
        inn = '6663003127'
        org_list = self.client.req(inn=inn)
        self.assertIsInstance(org_list, list, org_list)
        self.assertEqual(1, len(org_list), org_list)
        org = org_list[0]
        self.assertIsInstance(org, dict, org)
        self.assertIn('inn', org, org)
        self.assertEqual(inn, org['inn'], org)
        self.assertIn('ogrn', org, org)
        ogrn = org['ogrn']
        self.assertIn('UL', org, org)
        ul = org['UL']
        self.assertIn('legalName', ul, ul)
        self.assertIn('short', ul['legalName'], ul)
        self.assertGreater(len(ul['heads']), 0, ul)
