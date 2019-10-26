import unittest
from app import module
from tests import factory


class TestModule(unittest.TestCase):

    def test_calculate_insurance_default(self):
        result_expected = factory.create_client_insurance_default()
        result = module.calculate_insurance(factory.create_client_info_default())
        self.assertEqual(result_expected, result)

    def test_calculate_auto_ineligible(self):
        result = module.calculate_auto(factory.create_client_info_ineligible(), 0)
        self.assertEqual("ineligible", result)

    def test_calculate_auto_economic(self):
        result = module.calculate_auto(factory.create_client_info_economic(), -1)
        self.assertEqual("economic", result[0]["value"])

    def test_calculate_auto_regular(self):
        result = module.calculate_auto(factory.create_client_info_default(), 0)
        self.assertEqual("regular", result[0]["value"])

    def test_calculate_auto_responsible(self):
        result = module.calculate_auto(factory.create_client_info_responsible(), 3)
        self.assertEqual("responsible", result[0]["value"])

    def test_calculate_disability_ineligible(self):
        result = module.calculate_disability(factory.create_client_info_ineligible(), 0)
        self.assertEqual("ineligible", result)

    def test_calculate_disability_economic(self):
        result = module.calculate_disability(factory.create_client_info_economic(), -1)
        self.assertEqual("economic", result)

    def test_calculate_disability_regular(self):
        result = module.calculate_disability(factory.create_client_info_regular(), 1)
        self.assertEqual("regular", result)

    def test_calculate_disability_responsible(self):
        result = module.calculate_disability(factory.create_client_info_responsible(), 3)
        self.assertEqual("responsible", result)

    def test_calculate_home_ineligible(self):
        result = module.calculate_home(factory.create_client_info_ineligible(), 0)
        self.assertEqual("ineligible", result)

    def test_calculate_home_economic(self):
        result = module.calculate_home(factory.create_client_info_economic(), -1)
        self.assertEqual("economic", result[0]["value"])

    def test_calculate_home_regular(self):
        result = module.calculate_home(factory.create_client_info_regular(), 1)
        self.assertEqual("regular", result[0]["value"])

    def test_calculate_home_responsible(self):
        result = module.calculate_home(factory.create_client_info_responsible(), 3)
        self.assertEqual("responsible", result[0]["value"])

    def test_calculate_life_economic(self):
        result = module.calculate_life(factory.create_client_info_economic(), -1)
        self.assertEqual("economic", result)

    def test_calculate_life_ineligible(self):
        result = module.calculate_life(factory.create_client_info_ineligible(), 0)
        self.assertEqual("ineligible", result)

    def test_calculate_life_regular(self):
        result = module.calculate_life(factory.create_client_info_regular(), 1)
        self.assertEqual("regular", result)

    def test_calculate_life_responsible(self):
        result = module.calculate_life(factory.create_client_info_responsible(), 3)
        self.assertEqual("responsible", result)

    def test_calculate_umbrella_ineligible(self):
        result = module.calculate_umbrella(factory.create_client_insurance_ineligible())
        self.assertEqual("ineligible", result)

    def test_calculate_umbrella_regular(self):
        result = module.calculate_umbrella(factory.create_client_insurance_default())
        self.assertEqual("regular", result)


if __name__ == '__main__':
    unittest.main()
