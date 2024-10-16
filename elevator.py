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


from python_spell.checker import SpellChecker

fw = open('example_file.txt','w')
fw.write('Subject: your fjjk account has been hacked !\n')
fw.write('please send us your password so we can fix it .\n')
fw.close()



with open("example_file.txt", 'r', errors='ignore') as f:

    contents = f.read()
    
    #print(contents)
    f.close()
search_for_semicolon = contents.find(':')
subject_line = contents.split('\n')[0]
print(subject_line)
#la
 
# Reading from file
len_file = 0
CoList = contents.split("\n")
 
for i in CoList:
    if i:
        len_file += 1



spam_subjectline = ['account','compromised', 'personal','secure','Congratulations', 'won' , 'million',  'winner', 'send','credit','card',  'details', 'claim' , 'prize',
                    'Investment','revenue', 'Click', 'link','more','confirm','Unsubscribe','Reply','Claim', 'winning', 'amount ','payment', 'Restricted','now','urgent ',
                    'invoice','bank account','problem','fix', 'download', 'secure ',' great deal', ' handsome ', 'gorgeous', 'email verification ', 'special', 'password','hacked']


def spam_email(emial):
    count_ham = 0
    count_spam = 0
    search_for_semicolon = emial.find(':')

    # checking if the first letter in the subject line is a capital letter
    subject_line = emial[search_for_semicolon + 1].split('\n')[0]
    return subject_line
   
    remove_white_spaces = subject_line.replace(" ","")
    first_letter_is_capital = remove_white_spaces[0].isupper() 
    
    if first_letter_is_capital != False:
        count_ham += 1
    else:
        count_spam += 1

    
   
    #checking for typos inside the subject line
    checker = SpellChecker(subject_line, "english")
    check_text = checker.check()
    if first_letter_is_capital != False:
        count_ham += 1
    else:
        count_spam += 1
    number_of_typos = len(check_text['misspelled_words'])

    if number_of_typos >  0:
        count_spam += number_of_typos
        #return count_spam 

    #checking if the subject line has any spam key word
    for keyword in spam_subjectline:
        if keyword.lower() in subject_line:
            count_spam += 1
    # check for generic greetings in body
    lines = []
    for line in range(1,len_file):
        lines.append(emial.split('\n')[line])

    for lin in lines:
        remove_white_spacs = lin.replace(" ","")
        first_letter = remove_white_spacs[0].isupper() 
        if first_letter != False:
           count_ham += 1
        else:
           count_spam += 1

        checker_two = SpellChecker(subject_line, "english")
        check_text_two = checker_two.check()
        number_of_errors = len(check_text_two['misspelled_words'])
        
        if number_of_typos >  0:
           count_spam += number_of_errors

        
    return remove_white_spaces

    # return remove_white_spacs

    
print(spam_email(contents))


#         }
# print(convert(ratios, "gleep", "shneep", 2))

