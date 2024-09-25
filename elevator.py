#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022








# create a deck 

from random import *
import random

rng = random.Random()

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
      wild_card = ['wild','4']
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

Computer_hand = Card[:7] #After shuffling the deck I take the first 7 nested list and assign it to the computer hand
del Card[7]
players_hand = Card[8:15] #After shuffling the deck I take the new first 7 nested list and assign it to the players_hand
del Card[:15] # removing the cards from the Deck that have  been assigned to the players


before_shuffle = Card

Discarded_pile = [Card[0]]
    
bottom_card = Discarded_pile[0]


# Discarded assign bottom card
del Card[0]
#delete from the deck   
base = "Bottom Card..."
#print(base, bottom_card)

def bottom():
     global bottom_card
     
     
     while bottom_card == ['wilddraw','4']:
            rng.shuffle(before_shuffle)
            bottom_card = before_shuffle[0]
     return bottom_card





def starting():
     
     print('bottom..card',bottom())

     print("\nPlayerhand ", players_hand) 
     take_or_play = input("\nPlease enter Play to play or 'take' to draw a card from the Deck: ")

     if take_or_play != 'play' and take_or_play != 'take':
            return restart()
     
           
     
     if take_or_play.lower() == 'play':
        user_input = int(input("\nPlease Enter a number(press '8' to restart): "))  
        print(player_card(user_input)) 
     elif take_or_play.lower() == 'take':
           players_hand.append(random.choice(Card)) 
           print("\nCard have been added ", players_hand) 
     

def restart():
    print("\nPlay again ...")
    starting()



def player_card(user_input):
     global bottom_card           
     for i in range(len(players_hand)):
            
           if i == user_input:
                  choosen_card = players_hand[i]
                  if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[1] or bottom_card == ['wilddraw','4'] or bottom_card == ['wild','4']:
                       
                       bottom_card = choosen_card #switching the indexed position so bottom card get updated
                       del players_hand[i]
                       if bottom_card == ['RED','REV_']or bottom_card == ['BLUE','REV_'] or bottom_card == ['YELLOW','REV_'] or bottom_card == ['GREEN','REV_']:
                              del players_hand[i]
                              return restart()
                       if bottom_card == ['RED',"SKIP^" ] or bottom_card == ['BLUE','SKIP'] or bottom_card == ['YELLOW','SKIP^' ] or bottom_card == ['GREEN','SKIP^' ]:
                              del players_hand[i]
                              return restart()
                       if bottom_card == ['RED','+2'] or bottom_card == ['GREEN','+2'] or bottom_card == ['YELLOW','+2'] or bottom_card == ['BLUE','+2']:
                             
                             bottom_card = choosen_card
                             del players_hand[i]
                        #check if no alternative card exist in the play hand
                             Computer_hand.append(Card[:2])
                             return "bottom ",bottom_card, " 2 cards added to computer" 
                             
                       return bottom_card
                  
                        
                  elif choosen_card == ['wildraw','4']:
                        del players_hand[i]
                        bottom_card = choosen_card
                        #check if no alternative card exist in the play hand
                        Computer_hand.append(Card[:4])
                        return "bottom ",bottom_card, " 4 cards added to computer" 
                  elif choosen_card == ["wild",'4']:
                        del players_hand[i]
                        bottom_card = choosen_card
                        user =  input("You played a wild4 ,Choose a color:  ")
                        for i in ["YELLOW","BLUE","GREEN","RED"]:
                              if i == user:
                                  bottom_card = i
                                  return "bottom card ", bottom_card
               
                  elif choosen_card == ['RED','REV_'] or choosen_card == ['BLUE','REV_'] or choosen_card == ['YELLOW','REV_'] or choosen_card == ['GREEN','REV_']:

                         return "HEY HEY run"
                  # elif choosen_card == ['RED',"SKIP^" ] or choosen_card == ['BLUE','SKIP'] or choosen_card == ['YELLOW','SKIP^' ] or choosen_card == ['GREEN','SKIP^' ]:
                  #       return " So we skip"
                            
                  # for invalid move
                  
                  # elif bottom_card[0] != choosen_card[0] or bottom_card[1] != choosen_card[1] or bottom_card[0] != ['wilddraw','4'] or bottom_card[0] != ['wild','4']:
                  #       return 'jjj'
           elif user_input > 8:
                 return "Invalid number your card of choice must be between (0-6)"
           elif user_input == 8:
                 return restart()
                                           

'''
                  elif choosen_card == ['wild','4']:
                    del players_hand[i]
                    select_next_clr = input("Select a color [YELLOW ,BLUE, Green,blue] choose one ")
                    upper_case = select_next_clr.upper()
                    bottom_card = upper_case
                    return bottom_card
               
                  elif choosen_card == ['wilddraw','4']:
                    for i in range(len(players_hand)):
                        current = players_hand[i]
                        #checking if the user has no alternative cards to play besides wildraw.4
                        if bottom_card[0] != current[0] or bottom_card[1] != current[1]: 
                            Computer_hand.append(Card[:4])
                            return'Computer hand append by 4 cards ',Computer_hand
                        else:
                             players_hand.append(Card[:4])
                             return' Player hand append by 4 cards ',players_hand
                    
               
   
                  else:
                      
                    return "_", bottom_card
          
                 '''
starting()

def Computer_card():
    global bottom_card
    for i in range(len(Computer_hand)):
        choosen_card = Computer_hand[i]

        if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[1] or bottom_card[0] == ['wilddraw','4'] or bottom_card[0] == ['wild','4']:
                   del Computer_hand[i]
                   bottom_card = choosen_card #switching the indexed position so bottom card get updated
                   return bottom_card
                   
        elif choosen_card == ['wild','4']:
                    del players_hand[i]
                    select_next_clr = ["Yellow","BLUE","GREEN","RED"]
                    rand_choice = random.choice(select_next_clr)
                    upper_case = rand_choice.upper()
                    bottom_card = upper_case
                    return bottom_card  
        else:
             Computer_hand.append(random.choice(Card))
       
             return "Computer_hand takes one card ", random.choice(Card)
'''        
def valid_answer(choosen_card):
      global bottom_card , user_input
      if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[1] or bottom_card[0] == ['wilddraw','4'] or bottom_card[0] == ['wild','4']:
           return True
      else:
           return False

def valid_input_play_take():
      
         take_or_play = input("Please enter Play to play or 'take' to draw a card from the Deck: ")
         return take_or_play
  
index = 0 
while index < len(Card):   
    if bottom_card == ['wilddraw','4']:
        rng.shuffle(before_shuffle)
        bottom_card = before_shuffle[0]
        print(base,bottom_card)
    else:
        print(base,bottom_card)

    print("Playerhand ",players_hand)
    #take_or_play = input("Please enter Play to play or 'take' to draw a card from the Deck:\n")

    if valid_input_play_take().lower() == 'play':
        user_input = int(input("Please Enter a number: "))  
        if valid_answer(player_card(user_input)) == True:
             print(player_card(user_input))
        else:
             print("Please enter a valid card  or take from the deck if the playble card is not availble")
             
            #  if valid_input_play_take().lower() == 'play':
            #       print("Choose a valid card (*^_^*) ", players_hand)
            #       user_input = int(input("Please Enter a number: "))
            #       if valid_answer(user_input) == True:
            #            print(player_card(user_input))
            #  elif valid_input_play_take().lower() == 'take':
            #       players_hand.append(Card[0])
            #       print("Player card added ", players_hand)
            #       break
             
    
    elif valid_input_play_take().lower() == 'take':
          players_hand.append(random.choice(Card))
          print("Player card append ", players_hand)
    
   
   # print(player_card(user_input))

    print("next turn....computer...")
    if len(players_hand) == 0:
         print("Player1 wins")
         break
    
    
    print("Computer turn ______\n")
    print('Computer chose ',Computer_card())
    print("Computerhand ", Computer_hand)

    
    print("next turn player")
    if Computer_hand == 0:
         print("Computer wins")
         break

    
index += 1
'''


