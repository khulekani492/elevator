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
    
fw = open('example_file.txt','w')
fw.write('Subject: Your account has been hacked !\n')
fw.write('please send us your password so we can fix it .\n')
fw.close()

with open('example_file.txt', 'r', errors='ignore') as f:

    contents = f.read()
   #print(contents)
    f.close()





def spam_email(emial):
    count = 0
    search_for_semicolon = emial.find(':')
    subject_line = emial[search_for_semicolon:].split('\n')[0]
    
    # print(subject_line[1] == ' ')
    first_letter_is_capital = subject_line[1].isupper()
    if first_letter_is_capital is True:
        count +=  1

    first_letter_is_capital = subject_line[2].isupper()
    if first_letter_is_capital is True:
        count +=  1 

    symbols = list('!,:?.')
    position = []
    ix = 0
    msg = ''
    while ix < len(subject_line):
        positioned = subject_line[ix]
        if positioned == ' ':
            next_index = ix + 1

            next_position = subject_line[next_index]
            if next_position in symbols:
                return  
        
            
               
            
        
        ix += 1
        

    # return count 

          
        
print(spam_email(contents))    
#             ("shneep", "glorp"): 60, # 60 shneeps = 1 glorp
#         }
# print(convert(ratios, "gleep", "shneep", 2))

