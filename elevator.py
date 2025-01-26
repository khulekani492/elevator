
   import argparse
import random 
import math 
def parse_args():
    parser = argparse.ArgumentParser(description='Dice parameters taking in number of dice, weight ,\n')
    parser.add_argument('--dice', type=str, help='Number of dice ')
    parser.add_argument('--faces', type=int, help='Number of faces', default=6)
    parser.add_argument('--rolls', type=int, help='Number of rolls', default=1000)
    parser.add_argument('--weights', type=str,help='Die side that is mostly like to land', default=1)
    parser.add_argument('--bins', type=int,help='number of bins', default=1000)

    return parser.parse_args()



 #python multi_dice_simulator.py --dice 2 --faces 6 --rolls 1000 --weights 1,1,1,1,2,2 --bins 10
args = parse_args()

if args.bins > 11:
    raise ValueError
def my_file_parameters(die,faces,rolls,weight):
     print(f'Number of Dice: {die}')
     print(f'Number of Rolls: {rolls}')
     print(f'Dice Faces: {faces}') 
     print(f'Weights = {weight}') 

first_section  = my_file_parameters(args.dice,args.faces,args.rolls,args.weights)

def frequency(weight):
    global die1
    die1 = [2,3,4,5,6,7,8,9,10,11,12]
    outcomes = []
    #depending on the weights of the most likey die face to be rolled, the list is extended by adding that face number again 
    # e.g if the weight of 6 is 2 then list = [1,2,3,4,5,6,6]   
   
    weight = args.weights
    remove_commas = weight.replace(',','')
    numbers_die = []
    for i in range(len(remove_commas)):
        numbers_die.append(int(remove_commas[i]))
    
    die_face_most_likely = [] 

  
    for i in range(len(numbers_die)):
        if numbers_die[i] > 1:
            die_face_most_likely.append(i)
    
    number_to_double = []
    for i in die_face_most_likely:
      number_to_double.append(die1[i])   
    #extend the die list according to the weights 
    for i in  number_to_double:
        die1.append(i)
        
    for i in range(1,1000+1): 
        dice1 = random.choice(die1)
        outcomes.append(dice1) 
    
    frequency  = {}
    for n in die1:
            frequency[n] = outcomes.count(n)
            
    return frequency
        
results_table = frequency(first_section)
#print(results_table)
def table_for_frequency(outcome):
    print()
    print('Frequency Distribution:')
    print('Outcome Frequency:')
    print()
    for k,v in  outcome.items():
        print(f'{k}    {v}')
#
table_for_frequency(results_table)

def histogram(outcomes): 
    list_outcomes = []

    store_up_stars = []
    bins = 12 / args.bins

    first_key = next(iter(outcomes))
    for k,v in outcomes.items():
        first_step = v / outcomes[first_key] 
        second_step = first_step * first_key 
        store_up_stars.append(int(second_step) * '*')
        list_outcomes.append(str(k))
    histo = {}
    
    for i in range(11):
        histo[list_outcomes[i]] = store_up_stars[i] 
    return histo
dict_for_histo = histogram(results_table)

# #Summary Statisti

def grouping_into_bins (n):
    a = [2,3,4,5,6,7,8,9,10,11,12]
    divide_by_eleven = 11 / n
    co = int(divide_by_eleven)
    start = 0 
    end = co
    sub_list = [] 
    for i in range(1,n+1):
        
        if i == n:
            sub_list.append(a)
        else:
           bx = a[start:end]

           sub_list.append(bx)
           del a[:co] 
    return sub_list 
turn_into_STRINGS = grouping_into_bins(args.bins)

def histo_bins(turn):
    histogram_bins = []
    for sublist in turn:
       take =  str(sublist[0]) + '-' + str(sublist[-1])
       histogram_bins.append(take) 

    return histogram_bins 
#print(histo_bins(turn_into_STRINGS)) 
def display_histo(table1,table2,dic):
    f = table2 
    data_combined =  []
    for bin in range(f):
        pair_bins = table1[bin]
        strip_values = pair_bins.split('-')
        start,end = strip_values 
        values_combined = ''
        for combine in range(int(start),int(end)+1):
               values_combined += dic[str(combine)]
        data_combined.append(values_combined)
    dispaly = {} 
    
    for i in range(f):
        dispaly[table1[i]] = data_combined[i]
    print()
    print('Histogram:')
    for k,v in  dispaly.items():
        strip_values = k.split('-')
        start,end = strip_values
        if start == end:
            k = start
            print(f'{k}   {v}') 
        else:
           print(f'{k}    {v}')

display_histo(histo_bins(turn_into_STRINGS),args.bins,dict_for_histo)



#DIplay statitics 
def median(outcomes): 
   #outcomes.sort()
   #check if list is odd or even and return the median
   count = 0 
   values =  []
   for k, v in outcomes.items():
       count += v
       for n in range(1,v+1):
           values.append(k)
   
   if count % 2 == 0:
       index_first_half = count / 2
       first_half = index_first_half + 1
       first_step = values[int(index_first_half)] + values[int(first_half)]
       final_result = first_step / 2
       return final_result
   elif count % 3 == 0:
       index_=  count / 2
       roun_up = round(index_)
       return values[roun_up] 

        
#         # for i in range(2):
#         #     del outcomes[0]
#         #     del outcomes[-1]
     
#         output = outcomes[0] + outcomes[-1]/2
#         return output
#    else:
#     for i in range(3):
#             del outcomes[0]
#             del outcomes[-1]
#             return outcomes[0] 
median_value = median(results_table)
   
def mean(outcomes):
    # count = 0
    # for n in outcomes:
    #     count += n
    # return int(count) // 11 

    roll_count = 0
    fre_count = 0
    for k,v in outcomes.items():
        for n in range(1,v+1):
            fre_count += k 
            roll_count += 1 
    b = fre_count / roll_count
    return round(b) 
mean_value = mean(results_table)
def mode(outcomes):
    print(outcomes)
    values = outcomes.values()
    high = max(values)
    for k,v in outcomes.items():
        if high == v:
            return k

def varienc(outcome):
    sum = 0
    roll_count = 0
    for k,v in outcome.items():
        for n in range(1,v+1):
            sum +=  (k-mean_value) ** 2 
            roll_count += 1 

    return sum / (roll_count - 1) 
varienc_value  = varienc(results_table)

def standard_deviation(n):
    return math.sqrt(n)
def dispaly_stats():
    outcome = [2,3,4,5,6,7,8,9,10,11,12]
    print()
    print('Summary Statistics')

    print(f'Median: {median_value}')
    print(f'Mean: {mean(results_table)}')
    print(f'Mode: {mode(results_table)}')
    print(f'Variance: {varienc_value} ')
    print(f'Standard Deviation: {standard_deviation(varienc_value)} ') 

dispaly_stats()
