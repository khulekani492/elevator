#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022

cash = {'R200':20000,'R100' : 10000,'R50': 5000, 'R20': 2000,'R10':1000,'R5':500,'R2':200, 'R1' :100 , '50c': 50,'20c':20,
        '10c':10,'5c':5 }

amount_paid = 7000          #200
amount_due =  5600
change = amount_paid - amount_due

while True:

    for k, v in cash.items():
        if change >= v :
            change = change - v
            print(k)
            break

    if change == 0:
        break

def change(amount_paid,amount_due):
       cash = {'R200':20000,'R100' : 10000,'R50': 5000, 'R20': 2000,'R10':1000,'R5':500,'R2':200, 'R1' :100 , '50c': 50,'20c':20,
        '10c':10,'5c':5 }
       change = amount_paid - amount_due

       denominations = []
       while True:
            for k, v in cash.items():
                if change >= v :
                    change = change - v
                    denominations.append(k)
                    break
            if change == 0:
              break 
    
       final_change = set(denominations)

       # converting denomationations list to a dictionary, keys being the denomations and coins 
       # the values are the number of times that denomationtions or coin appears
       #in the list append in the while loop
       #final_change = set(denominations)

       denominations_dict = {}
       for denomination in final_change:
            denominations_dict[denomination] = denominations.count(denomination)
       return denominations_dict


