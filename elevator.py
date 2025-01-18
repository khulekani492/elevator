https://github.com/MrAlexander2000/Gents-Platform.git

def is_password_secure(password):
    pass_ = password
    if len(pass_) < 8:
            return False


    Capital = ''
    for word in password:
          if word == word.upper():
                Capital +=  word 

    if len(Capital) == 0:
            return False 
   
    low = ''
    for word in password:
          if word == word.lower():
                low +=  word 
    if len(low) == 0:
            return False
    
    numbers = []
    for num in password:
          if num.isdigit():
                numbers.append(num)
    if len(numbers) == 0:
                return False
     

    special_ones = list('@!#$%^&*()_+=-}{|/<>')
    spaces = []
    for i in password:
          if i in special_ones:
                spaces.append(i)
                
    if len(spaces) == 0:
           return False
   
                
    return True                    
