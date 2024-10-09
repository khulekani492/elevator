#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022

import unittest
from units import convert

class TestUnits(unittest.TestCase):
    def test_three_units(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
            ("shneep", "glorp"): 60, # 60 shneeps = 1 glorp
        }

        # 2 gleeps = 40 shneeps
        self.assertEqual(convert(ratios, "gleep", "shneep", 2), 40)

    def test_impossible(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
            ("glarg", "toriver"): 70, # 70 glargs = 1 toriver
        }

        # It's impossible to convert gleeps to torivers
        self.assertIsNone(convert(ratios, "gleep", "toriver", 1))

    def test_trivial(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
        }

        # 6 gleeps = 2 glorps
        self.assertEqual(convert(ratios, "gleep", "glorp", 6), 2)

    def test_trivial_backwards(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
        }

        # 2 glorps = 6 gleeps
        self.assertEqual(convert(ratios, "glorp", "gleep", 2), 6)

if __name__ == '__main__':
    unittest.main()


def convert(ratios, from_unit, to_unit, value):
    if from_unit == to_unit:
        return value

    if (from_unit, to_unit) in ratios:
        return value / ratios[(from_unit, to_unit)]

    return None


def convert(ratios, from_unit, to_unit, value):



    if from_unit == to_unit:
        return value

    if (from_unit, to_unit) in ratios:
        return  int(value / ratios[(from_unit, to_unit)])
 
    if (to_unit, from_unit) in ratios:
        return int(value * ratios[(to_unit, from_unit)])
    

    for (unit1, unit2), ratio in ratios.items():
        if from_unit in unit1:  # Try converting from `from_unit` to `unit2`
            common_value = value / ratio
            result = convert(ratios, unit2, to_unit, common_value)
            return result
        elif from_unit in unit2:  # Try converting from `from_unit` to `unit1`
            common_value = value * ratio
            result = convert(ratios, unit1, to_unit, common_value)
            return result
 


    return None 


ratios = {
    ("gleep", "glorp"): 3,    # 3 gleeps = 1 glorp
    ("gleep", "shneep"): 60,  # 3 gleeps  =  60 shneep
    ("shneep", "glara") : 5,  # 60 shneep = 5 glara
    ("glara", "rewodo") : 2,  # 5 glara = 2 rewodo
}

print(convert(ratios, "rewodo", "shneep", 5))  # Should give the correct result
# ratios = {
#             ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
#             ("shneep", "glorp"): 60, # 60 shneeps = 1 glorp
#         }
# print(convert(ratios, "gleep", "shneep", 2))

