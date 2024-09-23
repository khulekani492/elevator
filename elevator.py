#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022



levels = ['floor10','floor8','floor7','floor6','floor5','floor4','floor3','floor2','floor1',]


def _elavator(floor,num):
    for i in floor:
        if int(i[5]) == num:
             print(i,"(*_*)",f"{user_name}")
             print("_" * 6)
        else:
             print(i)
             print("_"* 6)
             

# create a d
#print(c)''#return n

user_name = input("Name: ")
num = int(input("Enter floor number: ")) 
_elavator(levels,num)




# create a deck 

Card = []
numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]
cards = {'Red ':numbers,'Yellow ':numbers,'blue ':numbers,'green ':numbers}






special_cards = []
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      c = "+2" + i
      special_cards.append(c)
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      b = "REV_" + i
      special_cards.append(b)
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
    b = "SKIP^" + i
    special_cards.append(b)


  
   
    #return n


for k,v in cards.items():
        for i in v:
            a = [k , str(i)]
            Card.append(a)



import random
rng = random.Random()
# create a deck 
Card = []
numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]
cards = {'RED':numbers,'YELLOW':numbers,'BLUE':numbers,'GREEN':numbers}

special_cards = []
for i in ['RED','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      c = [i,"+2"]
      special_cards.append(c)
for i in ['RED','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      b = [i ,"REV_"]
      special_cards.append(b)
for i in ['RED','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
    b = [i,"SKIP^"  ]
    special_cards.append(b)

for i in range(1,5):
      wild_card = ['wild',str(i)]
      special_cards.append(wild_card) 


for i in range(1,5):
      wild_card = ['wildraw','4']
      special_cards.append(wild_card)

for k,v in cards.items():
        for i in v:
            a = [k , str(i)]
            Card.append(a)
Card.extend(special_cards) 


#shuffle_the_card 
rng.shuffle(Card)

# Games main logic 

Computer_hand = Card[0:7] #After shuffling the deck I take the first 7 nested list and assign it to the computer hand

players_hand = Card[7:14] #After shuffling the deck I take the new first 7 nested list and assign it to the players_hand
del Card[0:15] # removing the cards from the Deck that have  been assigned to the players

#Computer = [random.choice(Computer_hand)]
#Back_to_nest = [Computer] # when the random function takes a random next_list it no longer nested it must nested [[]] in order to compare it value

#print(Discarded_pile[0] == ['wild','1'] or Discarded_pile[0] == ['wild','2'] or Discarded_pile[0] == ['wild','3'] or Discarded_pile[0] == ['wild','4'] )


# Separating the wild draw back from the deck to specify inside a function to remove it from discarded pile if it the first one turned

wild = [[]]
for i in range(1,5):
      wild_card = 'wilddraw','4'
      wild.append(wild_card)


Discarded_pile = Card[0]



#first_card = random.choice(Card)



def special_card_Removal():
    #if Discarded_pile[0] ==['wild','1'] or Discarded_pile[0] == ['wild','2'] or Discarded_pile[0] == ['wild','3'] or Discarded_pile[0] == ['wild','4'] :
          #Discarded_pile.remove(Discarded_pile[0])
          global Discarded_pile
          for i in range(len((wild))):
                if wild[i] == Discarded_pile:
                      return wild[i]
                return [wild[1]]      
              
          
          
#print(special_card_Removal())


'''
if Discarded_pile != special_card_Removal() : 
     print( Discarded_pile)
else:
     print(random.choice(Card))   

#Nest_the_discpile = [Discarded_pile]'''


#print('Choose ',players_hand)
#print(Computer,"Computer choice ")                 
#rint(Computer_hand,"Cards of the computer")

def player_card(user_input):
    #global Discarded_pile
   
    for i in range(len(players_hand)):
          if i == user_input:
               choosen_card = players_hand[i]
              # Discarded_pile.append(choosen_card)
              # del players_hand[i] 
               
               if Discarded_pile[0][0] == choosen_card[0][0] or Discarded_pile[0][1] == choosen_card[0][1] or Discarded_pile[0][0] == choosen_card[0][1]:
                   Discarded_pile.append(choosen_card)
                   del players_hand[i]
                   return Discarded_pile
               else:
                    print('Card is not in the list')

'''
def Computer_card():
    global Discarded_pile
    for i in range(len(Computer_hand)):
        current = Computer_hand[i]
       
        
        if Discarded_pile[0][0] == current[0][0] or Discarded_pile[0][1] == current[0][1] or Discarded_pile[0][0] == current[0][1]:
              Discarded_pile.append(current)
              del Computer_hand[i]
              
              
              print(Computer_hand,'current')
              print(Discarded_pile)
               
              return current  #return current'''
              
index = 0

while index < len(Card):

      start = 2
      if Discarded_pile != special_card_Removal() : 
         print( Discarded_pile)
      else:
          print(random.choice(Card))  
      print("Players cards ",players_hand)     
      user_input = int(input("Enter a number: "))
      
      player = player_card(user_input)
      print(player)
     
      
      print(Computer_hand, 'Computer hand')
      
     #print(Discarded_pile[2][1],' First')
      
      for i in range(len(Computer_hand)):
        current = [Computer_hand[i]]
        #print(current)
       # print(current[0][1] , ' POSITION')
        if player[start][0] == current[0][0] or player[start][1] == current[0][1] or player[start][0] == current[0][1]:
                  
                  player.append(current)
                  
             # Discarded_pile.append(current)
                  #print(player,' OG TALK')
                  break 
        start += 1



