#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022





# create a deck 

from random import *
import random
from random import Random

rng = random.Random()

Card = []
numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]
cards = {'Red ':numbers,'Yellow ':numbers,'blue ':numbers,'green ':numbers}

# special_cards = []
# for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
#       c = "+2" + i
#       special_cards.append(c)
# for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
#       b = "REV_" + i
#       special_cards.append(b)
# for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
#     b = "SKIP^" + i
#     special_cards.append(b)

# for k,v in cards.items():
#         for i in v:
#             a = [k , str(i)]
#             Card.append(a)




 #create a deck 
#Card = []
# numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]
# cards = {'RED':numbers,'YELLOW':numbers,'BLUE':numbers,'GREEN':numbers}

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

print(len(Card))
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
     
     while bottom_card == ['wilddraw','4'] :
           shuffle = random.choice(before_shuffle)
           bottom_card = shuffle
     return bottom_card
     
     

def starting():
     
#      print('bottom..card',bottom())
#      if bottom() == ['RED','+2'] or bottom() == ['GREEN','+2'] or bottom() == ['YELLOW','+2'] or bottom() == ['BLUE','+2']:
#         Computer_hand.append(Card[:2])
#         print("bottom ",bottom_card, " 2** cards added to computer")
#      bot = bottom()
#      print(bot)

     print("\nPlayerhand ", players_hand) 
     take_or_play = input("\nPlease enter 'P' to play or 't' to'take' to draw a card from the Deck: ")

     if take_or_play.lower() != 'p' and take_or_play.lower() != 't':
            #print("ERROR\n Please enter 'play'  or 'take' to draw from the deck ")
            return starting()
     
           
     
     if take_or_play.lower() == 'p':
        user_input = int(input("\nPlease Enter a number(press '8' to restart): \n"))  
        print(player_card(user_input))
        b = player_card(user_input) 
        return ' new ', b
     elif take_or_play.lower() == 't':
           players_hand.append(random.choice(Card)) 
           print("\nCard have been added \n", players_hand) 
     print(Computer_card())
      
#      return player_card(user_input)

def restart():
     print("\n Player1 play again ...")
     starting()

def invalid_card():

      print("\nInvalid entry\n...Enter a valid card or take from the deck ")
      starting()

def player_card(user_input):
     global bottom_card
     #global bottom_card 
     bottom_card = bottom()          
     for i in range(len(players_hand)):
            
           if i == user_input:
                  choosen_card = players_hand[i]
                  if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[1] or choosen_card == ['wilddraw','4'] or choosen_card == ['wild','4']:
                       
                       bottom_card = choosen_card #switching the indexed position so bottom card get updated
                       del players_hand[i]     
                 
                       if bottom_card == ['RED','REV_'] or bottom_card == ['BLUE','REV_'] or bottom_card == ['YELLOW','REV_'] or bottom_card == ['GREEN','REV_']:
                              del players_hand[i]
                  
                              return restart()
                       if bottom_card == ['RED',"SKIP^" ] or bottom_card == ['BLUE','SKIP^'] or bottom_card == ['YELLOW','SKIP^' ] or bottom_card == ['GREEN','SKIP^' ]:
                              del players_hand[i]
                              
                              return restart()
                       if bottom_card == ['RED','+2'] or bottom_card == ['GREEN','+2'] or bottom_card == ['YELLOW','+2'] or bottom_card == ['BLUE','+2']:
                             bottom_card = choosen_card
                             del players_hand[i]
                             
                        #check if there is no alternative card that exists in the player's hand
                             Computer_hand.append(Card[:2])
                             return "bottom ",bottom_card, " 2 cards added to computer"
                       if bottom_card == ["wild","4"]:
                             del players_hand[i]
                             bottom_card = choosen_card
                             user =  input("You played a wild4 ,Choose a color['YELLOW','BLUE','GREEN','RED']:  ")
                             for i in  [ ["YELLOW"],["BLUE"],["GREEN","RED"]]:
                                  if i == user:
                                      bottom_card = i
                                      return "bottom card ", [bottom_card]

                        
                       return bottom_card
                     
                 
                        
                  elif choosen_card == ['wildraw','4']:
                         for card in players_hand:
                               if bottom_card[0] == card[0] or bottom_card[1] == card[1]:
                                     players_hand.append(Card[:4])
                                     return '4 cards added to play\n',players_hand
                                     

                         
                         bottom_card = choosen_card
                         del players_hand[i]
                        #check if no alternative card exist in the play hand
                         Computer_hand.append(Card[:4])
                         return "bottom ",bottom_card, "\n4 cards added to computer" 
                  
                  # elif bottom_card[0] != choosen_card:
                  #       return invalid_card()
              
           elif user_input > 8:
                 return invalid_card()
           elif user_input == 8:
                 return restart()
      #      print(Computer_hand)
      #      print(Computer_card())     



def Computer_card():
    global bottom_card
    for i in range(len(Computer_hand)):
        choosen_card = Computer_hand[i]
        
        if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[[1] or choosen_card == ['wilddraw','4'] or choosen_card == ['wild','4']:
                       
                       bottom_card = choosen_card #switching the indexed position so bottom card get updated
                       
                  #      if bottom_card == ['RED','REV_'] or bottom_card == ['BLUE','REV_'] or bottom_card == ['YELLOW','REV_'] or bottom_card == ['GREEN','REV_']:
                  #             del Computer_hand[i]
                              
                  #             return Computer_card()
                  #      if bottom_card == ['RED',"SKIP^" ] or bottom_card == ['BLUE','SKIP^'] or bottom_card == ['YELLOW','SKIP^' ] or bottom_card == ['GREEN','SKIP^' ]:
                  #             del Computer_hand[i]
                              
                  #             return Computer_card()
                  #      if bottom_card == ['RED','+2'] or bottom_card == ['GREEN','+2'] or bottom_card == ['YELLOW','+2'] or bottom_card == ['BLUE','+2']:
                  #            bottom_card = choosen_card
                  #            del Computer_hand[i]
                  #            players_hand.append(Card[:4])
                  #            return "bottom ",bottom_card, "\n4 cards added to Player" 
                       
                             
                  #      if bottom_card == ["wild","4"]:
                  #            del Computer_hand[i]
                  #            bottom_card = choosen_card
                  #            #user =  input("You played a wild4 ,Choose a color['YELLOW','BLUE','GREEN','RED']:  ")
                  #            colors = [ ["YELLOW"],["BLUE"],["GREEN","RED"]]
                  #            com_chosen_color = random.choice(colors)
                  #             #     if i == user:
                  #            bottom_card = com_chosen_color
                  #            return "bottom card ", [bottom_card]
                  #      if bottom_card == ['wildraw','4']:
                  #              del Computer_hand[i]
                  #              bottom_card = choosen_card
                  #       #check if no alternative card exist in the play hand
                  #              players_hand.append(Card[:4])
                  #              return "bottom ",bottom_card, "\n4 cards added to Player" 
                       

                       del Computer_hand[i]      
                       return 'bottom 55 card ',bottom_card
    else:
      return "hhhh"
        
      #   elif bottom_card != choosen_card:
      #        Computer_hand.append(Card[:2])
      #        return 'COMPYTER took a card'
#     else:
#           return "ddddd"
          
        
print(Computer_card())
    

# starting()
index =  0
while index < len(Card):
 
 print('\nBottom card\n____________________________\n',bottom())
 starting()
 #print(bottom(), "after")
 print('\nCOMPUTER TURN\n............................ ')
 print('\n COMPUTER cards\n------',Computer_hand)
 print(Computer_card())

 index += 1
# #       bottom_card = bottom()
#       print('bottom..card',bottom())
#       if bottom() == ['RED','+2'] or bottom() == ['GREEN','+2'] or bottom() == ['YELLOW','+2'] or bottom() == ['BLUE','+2']:
#         Computer_hand.append(Card[:2])
#         print("bottom ",bottom_card, " 2** cards added to computer")
#       starting()
      
      
#       print("COmputer turn", Computer_hand)
#       print(Computer_card())
     
