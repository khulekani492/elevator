#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022

# create a deck 

from random import *
import random
#from random import Random

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
     
     while bottom_card == ['wildraw','4'] :
           shuffle = random.choice(before_shuffle)
           bottom_card = shuffle
     return bottom_card
     
     

def starting():
     global bottom_card
     print('_______________-------CLASSIC UNO------_______________')
     print('Bottom..card',bottom())
          
     if bottom() == ["wild","4"]:
          user =  input("\n_______\n it wild4 ,Choose a color:  ")
          to_lst = [user]
          for clr in [["YELLOW"],["BLUE"],["GREEN"],["RED"]]:
               if clr == to_lst:
                  bottom_card = to_lst
                  return "nxt color to play ", bottom_card

                    #print("ayisuka mani")

     
     print("\nPlayerhand\n_ _ _ _ _ _ _ _ ", players_hand) 
     take_or_play = input("\n________________\nPlease enter Play to play or 'take' to draw a card from the Deck: ")

     if take_or_play != 'p' and take_or_play != 't':
            #print("ERROR\n Please enter 'play'  or 'take' to draw from the deck ")
            print("INVALID ENTRY!! input 'p' or 't' ")
            return starting()
     
           
     
     if take_or_play.lower() == 'p':
        user_input = int(input("\n__________||Please Enter a number(press '00' to restart): "))  
        print(player_card(user_input)) 
     elif take_or_play.lower() == 't':
           re = Card[0]
      
           players_hand.append(re) 
           del Card[0]
           
           print("\nCard have been added ", players_hand) 
     

def restart():
     print("\nplay again ...")
     starting()

def invalid_card():

      print("\nCard not match or you pressed a number above 8\n...Enter a valid card or take from the deck ")
      starting()

def player_card(user_input):
     global bottom_card 
     #bottom_card = bottom()          
     for i in range(len(players_hand)):
            
           if i == user_input:
                  choosen_card = players_hand[i]
                  if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[1] or choosen_card == ['wildraw','4'] or choosen_card == ['wild','4']:
                       
                       bottom_card = choosen_card #switching the indexed position so bottom card get updated
                       
                       if bottom_card == ['RED','REV_'] or bottom_card == ['BLUE','REV_'] or bottom_card == ['YELLOW','REV_'] or bottom_card == ['GREEN','REV_']:
                              del players_hand[i]
                             # print (players_hand)
                              return restart()
                       if bottom_card == ['RED',"SKIP^" ] or bottom_card == ['BLUE','SKIP^'] or bottom_card == ['YELLOW','SKIP^' ] or bottom_card == ['GREEN','SKIP^' ]:
                              del players_hand[i]
                             # print (players_hand)
                              return restart()
                       if bottom_card == ['RED','+2'] or bottom_card == ['GREEN','+2'] or bottom_card == ['YELLOW','+2'] or bottom_card == ['BLUE','+2']:
                             bottom_card = choosen_card
                             del players_hand[i]
                             #appending the computer cards with two cards
                             for i in range(2):
                                 extras = Card[i]
                                 Computer_hand.append(extras)
                                 del Card[i]
                            
                        
                             return "*******\n 2 cards added to computer",bottom_card
                       if choosen_card == ['wildraw','4']:
                             del players_hand[i]
                             #check if there is no alternative card that exists in the player's hand
                             for card in players_hand:
                                if bottom()[0] == card[0] or bottom()[1] == card[1]:
                                      for i in range(5):
                                            extras = Card[i]
                                            
                                            players_hand.append(extras)
                                            del Card[i]
                                            return 'You played a wildraw\nin your cards you have a card that can be played\n4 plus cards added to  PLAYER'#,players_hand
                                
                             #appending the computer card
                             for i in range(5):
                                     extras = random.choice(Card)
                                     Computer_hand.append(extras)
                           
                        
                             return "********\n4 cards added to computer"    
                                                            
                  
                       if bottom_card == ["wild","4"]:
                             del players_hand[i]
                             bottom_card = choosen_card
                             user =  input("You played a wild4 ,Choose a color ['YELLOW','RED','BLUE','GREEN'](0-3):  ")
                             to_lst = [user] # convert user input to a string 
                             
                             for clr in[["YELLOW"],["BLUE"],["GREEN"],["RED"]] :
                                  if clr == to_lst: 
                                      bottom_card = to_lst
                                      return "nxt color to play ", bottom_card

                       del players_hand[i]      
                       return bottom_card
                  
                  elif bottom_card != choosen_card:
                        return invalid_card()
              
      #      elif user_input > 8:
      #            return invalid_card()
           elif user_input == 00:
                 return restart()     


# this function return the element that appears the most
# This is to give the computer an advantage when playing a wild or wildraw4 card by picking the color it has the most


def Computer_card():
    global bottom_card
    print("**********************************************************")
    print("\n|||___COMPUTER TURN___|||\n Computer Cards",Computer_hand)
    for i in range(len(Computer_hand)):
        choosen_card = Computer_hand[i]

        if bottom_card[0] == choosen_card[0] or bottom_card[1] == choosen_card[1] or choosen_card == ['wildraw','4'] or choosen_card == ['wild','4']:
                       
                   
                   bottom_card = choosen_card #switching the indexed position so bottom card get updated
                   
                   if bottom_card == ['RED','REV_'] or bottom_card == ['BLUE','REV_'] or bottom_card == ['YELLOW','REV_'] or bottom_card == ['GREEN','REV_']:
                              del Computer_hand[i]
                             # print (players_hand)
                              return Computer_card()
                   if bottom_card == ['RED',"SKIP^" ] or bottom_card == ['BLUE','SKIP^'] or bottom_card == ['YELLOW','SKIP^' ] or bottom_card == ['GREEN','SKIP^' ]:
                              del Computer_hand[i]
                             # print (players_hand)
                              return Computer_card()
                   if bottom_card == ['RED','+2'] or bottom_card == ['GREEN','+2'] or bottom_card == ['YELLOW','+2'] or bottom_card == ['BLUE','+2']:
                             bottom_card = choosen_card
                             del Computer_hand[i]
                             #appending the computer cards with two cards
                             for i in range(2):
                                 extras = Card[i]
                                 players_hand.append(extras)
                                 del Card[i]
                            
                        
                             return "*******\n 2 cards added to player"
                   if choosen_card == ['wildraw','4']:
                             del Computer_hand[i]
                             for i in range(5):
                                 extras = Card[i]
                                 players_hand.append(extras)
                                 del Card[i]
                                 return "4 card added to player"
                   if bottom_card == ["wild","4"]:
                      del Computer_hand[i]
                      bottom_card = choosen_card
                      
                      colors = [["YELLOW"],["BLUE"],["GREEN"],["RED"]]
                      choosen = random.choice(colors)
                      bottom_card = choosen
                      return "nxt color to play ", bottom_card

                   
        
                   del Computer_hand[i]
      
                   return bottom_card 
    else:        
       re = Card[0]
       players_hand.append(re) 
       del Card[0]
       
       
       return "Conputer takes one card"

while True:
      starting()
      if len(players_hand) == 0:
            print("Player 1 win ")
            print(players_hand,"last cards")
            break
      print(Computer_card())
      if len(Computer_hand) == 0:
            print(players_hand,"last cards")
            print("Computer wins ")
            break
