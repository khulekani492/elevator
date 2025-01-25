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
def grouping_into_bins (n):
    a = [2,3,4,5,6,7,8,9,10,11,12]
    divide_by_eleven = 11 / n
    co = int(divide_by_eleven)
    start = 0 
    end = co
    sub_list = [] 
    for i in range(1,n+1):
        print(a)
        if i == n:
            sub_list.append(a)
        else:
           bx = a[start:end]

           sub_list.append(bx)
           del a[:co] 
    return sub_list 
turn_into_STRINGS = grouping_into_bins(4)
def histo_bins(turn):
    histogram_bins = []
    for sublist in turn:
       take =  str(sublist[0]) + '-' + str(sublist[-1])
       histogram_bins.append(take) 

    return histogram_bins 
print(histo_bins(turn_into_STRINGS))
