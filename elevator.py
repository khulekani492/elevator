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


            
        
        ix += 1
        

    # return count 

  #from python_spell.checker import SpellChecker

# fw = open('email.txt','w')
# fw.write('Subject: Your account  has been hacked !\n')
# fw.write('please send us your password so we can fix it .\n')
# fw.write('please send us your password so we can fix it .\n')


# fw.close()



with open("email.txt", 'r', errors='ignore') as f:

    contents = f.read()
    f.close()

# Reading from file
len_file = 0
CoList = contents.split("\n")
 
for i in CoList:
    if i:
        len_file += 1




spam = [ 'won' , 'million',  'winner', 'send','credit','card',  'details', 'claim' , 'prize','account'   'compromised', 'personal','secure','Congratulations',
                    'Investment','revenue', 'Click', 'link','more','confirm','Unsubscribe','Reply','Claim', 'winning', 'amount ','payment', 'Restricted','now','urgent ',
                    'invoice','bank account','problem','fix', 'download', 'secure ',' great deal', ' handsome ', 'gorgeous', 'email verification ', 'special', 'password','hacked','@','#','$',"%", "^","&","*","(",")","-",
                    " ",">","<","?","|","  ","??","hello", " ! !", "http:/",'sexy', 'free', 'spin',' spinning', 'true love',]



# def spam_email(emial):
#     inside = 0
#     count_spam = 0
#     misspelled = []

   
#     for line in range(len_file):
         
#          body_line = emial.split('\n')[line]
#          split = body_line.split() 
#          if body_line[0] == body_line.isupper():
#              count_spam -= 1
#          how_many = []
#          for keyword in spam_subjectline:
           
#             if keyword.lower() in split:
#                 how_many.append(keyword)
#                 count_spam += 2
             
            
#             if  len(split) >  5:
#                 count_spam += 2
        
       
#          if count_spam > 1:
#            return 'spam'
#          else:
#            return 'notspam'   
         
         
     
# print(spam_email(contents))

# spam_subjectline ={'won': 2 , 'million':3,  :2, 'send':3,'credit':2,'card':3, 'details':3, 'claim':2 ,'account':3, 'compromised':2, 'personal':3,'secure':2,'Congratulations':3,
#                     'Investment':4,'revenue':3, 'Click':3, 'link':2,'more':4,'confirm':3,'Reply':1,'Claim':3, 'winning':2, 'amount':3,'payment':2, 'Restricted':2,'now':3,'urgent ':4,
#                     'invoice':2,'bank':3 ,'account':2,'problem':3,'fix':2, 'download':3, 'secure ':2,' great deal':3, 'handsome':4, 'gorgeous':2, 'email verification':3, 'special': 2, 'password': 3,'hacked':5,'!!': 4,
#                     '@@': 2,'#':3,'$':4 ,"%": 1, "^": 2,"&": 3,"****": 2,
#                     ">":2,"<":3,"?":1,"|":3,"??":2,"hello":4, "!!":2, "http:/": 2,'sexy':3, 'free':4, 'spin':4,' spinning':3,'true love':3,}

# scam = ['hacked','win','claim','click','prize','Unsubscribe'] #


# import string library function 
import string 
import re
	
# Storing the sets of punctuation in variable result 
result = string.punctuation 
	


def check(email):
    spam_count = 0
    ham_count = 0
    content = email
    split_content = re.split(r'(\s+)',content)
    for index in range(len(split_content)):
        for pun in result:
          if split_content[index] == pun: 
            before = split_content[index - 1]
            if before == ' ':
                spam_count +=  1
            
        for i in result:
           if i in  split_content[index]:
              into_list = list(split_content[index])
              if len(into_list) > 2:
                 print(split_content[index])
                 ham_count += 1

  
    print(spam_count)
    print(ham_count)

non_spam = ['Market','Junior','Universit-y','Commissio-n','Microsoft','sure','Manager','Corporat-ion','Holder','Sep','Letter','Details','Staff','Trainee',
            'Mar','Project','Naukri','General','National','2017','Unsubscribe','Mountain','Deputy','Life','Last','Application','Graduate','Degree',
            'Reading','Date','Image','View','.Net','Office','2016','Research','United','Advt','Here','PST','Subscribed','Technician','Create','Technology'
            ,'Assistant','India','Powered','Development','Core','Updated','Engineer','Options','ASP.NET','DATES','Votes','Votes','States','Singh',
            'AM','Google','Torronto','State','IMPORTANT','Various','Bank','Form','Horoscope','Ghansham','Invites','Senior','Build','Multiple','Facebook',
            'Officer','Code','August','News','Forwarded','Police','Ago','Institute','Client','Wipeout','Yesterday','Technical','Data','Blogs','Open',
            'Entry','Official','Details','Executive','Tips','Stop','Group','Pradesh','Ontario','Operator','wrote ','Library ','Continue','Gmail'
            ]
def check(emial):
    current_count = 0
    two = 0
    # for line in range(len_file):
    #     body_line = emial.split('\n')[line]
        # words_list = body_line.split()
        # search_for_semicolon = emial.find(':')
        # subject_line = emial[search_for_semicolon:].split('\n')[0]
        # first_letter_is_capital = subject_line[1].isupper()
        # if first_letter_is_capital is True:
        #     two +=  1

                  
        # if '  ' in body_line:
        #     current_count += 1
        # # else:
        # #      two += 1

        # if "  !" in body_line or " !" in body_line:
        #         current_count +=  25 #25
        # if "  !" not in body_line or " !" not in body_line:
        #          two += 1.9
        # if"  ." in body_line or " ." in body_line:
        #          current_count += 6
        # if "  ." not in body_line or " ." not in body_line:
        #          two += 1
        # if"  ?" in body_line or " ?" in body_line:
        #          current_count += 7.5
        # if "  ?" not in body_line or " ?" not in body_line:
        #          two += 1
        
     
        # for word in words_list:
        #       if word in scam:
        #             current_count = 25 #60
        #             scam.remove(word)
     
    # if current_count > two:
    #      return 'spam'
    # else:
    #      return 'notspam'



def is_password_secure(password):
    pass_ = password
    length = False
    if len(pass_) < 8:
            #length = True
            return False


    Capital = ''
    upper = False
    for word in password:
          if word == word.upper():
                Capital +=  word 

    if len(Capital) == 0:
            return False
               #upper = True 
   
    low = ''
    lower = False
    for word in password:
          if word == word.lower():
                low +=  word 
    if len(low) == 0:
            return False
                #lower = True 
    
    

    digit = False
    numbers = []
    for num in password:
          if num.isdigit():
                numbers.append(num)
               # digit = True 
    if len(numbers) == 0:
                return False
     

    special_ones = list('@!#$%^&*()_+=-}{|/<>')
    chosen = False
    spaces = []
    for i in password:
          if i in special_ones:
                spaces.append(i)
                #chosen = True
    if len(spaces) == 0:
           return False
   
                
    return True             

        

