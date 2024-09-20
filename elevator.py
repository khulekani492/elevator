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
      c = ["+2",i]
      special_cards.append(c)
for i in ['RED','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      b = ["REV_" ,i]
      special_cards.append(b)
for i in ['RED','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
    b = ["SKIP^" , i]
    special_cards.append(b)

for i in range(1,5):
      wild_card = ['wild',str(i)]
      special_cards.append(wild_card)


for i in range(1,5):
      wild_card = ['wildraw',str(i)]
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
#print('com hand', Computer_hand)
players_hand = Card[7:14] #After shuffling the deck I take the new first 7 nested list and assign it to the players_hand
del Card[0:15] # removing the cards from the Deck that have  been assigned to the players





Computer = [random.choice(Computer_hand)]
#Back_to_nest = [Computer] # when the random function takes a random next_list it no longer nested it must nested [[]] in order to compare it value
Discarded_pile = [Card[0]] 
#Nest_the_discpile = [Discarded_pile]
user_input = int(input("Enter a number: "))
print(b)

print(Discarded_pile, ' Card on the table')
print('Choose ',players_hand)
                  

for i in range(len(players_hand)):
      if i == user_input:
            choosen_card = players_hand[i]
            b = choosen_card
print("Card choosen buy player", choosen_card)
