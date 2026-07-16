import random

#declare variables
#card possibilities include multiple 10s to mimic face card values
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


#totals number in given hand
def getTotal(list):
    total = 0
    for i in range(0, len(list)):
        total += list[i]
    return total 

#prints out hand and total for player    
def printHand(list):
    print('Your hand:')
    print(list)
    print('Your total: ')
    print(getTotal(list))
    print('\n')

#prints out hand and total for dealer 
def printDealer(dealer):
    print('Dealer\'s hand:')
    print(dealer)
    print('Dealer\'s total: ')
    print(getTotal(dealer))
    print('\n')

#adds new card to hand and prints out for player
def addCard(list):
    newCard = cards[random.randint(0,13)]
    list.append(newCard)
    print('\n')
    print('New card:')
    print(newCard)

#for user input bet
def toInt(str):
    num = 0
    if str == '1':
        num = 1
    elif str == '2':
        num = 2
    elif str == '3':
        num = 3    
    elif str == '4':
        num = 4
    elif str == '5':
        num = 5
    elif str == '6':
        num = 6
    elif str == '7':
        num = 7
    elif str == '8':
        num = 8
    elif str == '9':
        num = 9
    elif str == '10':
        num = 10
    return num

        
def game(bet):
    
    #initial hand dealt        
    num1 = cards[random.randint(0,13)]
    num2 = cards[random.randint(0,13)]
    hand = [num1, num2]
    #initial dealer hand dealt         
    dnum1 = cards[random.randint(0,13)]
    dnum2 = cards[random.randint(0,13)]             
    dealer = [dnum1, dnum2]

    #show player their hand and dealer's top card only   
    print('Dealer\'s hand')
    print(dealer[0])
    print('\n')
    printHand(hand)

    play = True
    win = True
    firstTime = True
    #spend variable used to subtract from chips at end if player wants more cards
    spend = 0
    #player's turn
    while play == True:
        hit = ''
        #player decides if they want another card
        #loop to make sure input is valid
        while hit != 'y' and hit != 'n':

         #only spend chip on first time getting dealt a new card
          if firstTime == True:  
              hit = input("Would you like another card (y or n)? (costs 1 chip)")
          else:
              hit = input("Would you like another card (y or n)?")
        
        #player wants to be dealt another card
        if hit == 'y':
            #only spend chip on first time getting dealt a new card
            if firstTime == True:
                spend = 1
                firstTime = False
            addCard(hand)
            printHand(hand)
        #player is done
        elif hit == 'n':
            play = False
            print('\n')
            
        #check if player's hand exceeds 21 and automatically loses
        if getTotal(hand) > 21:
            play = False
            win = False


    #if player is under 21, continue
    if win == True:
        #print to show player the scores
        printHand(hand)
        printDealer(dealer)

        #dealer's turn
        while getTotal(dealer) <= 15:
            print('Dealer must draw')
            print(input('Press enter to continue'))
            print("Dealer draws")
            addCard(dealer)
            printDealer(dealer)
            
        print(input('Press enter to continue'))

        #calculate winner and number of chips won/lost
        if getTotal(dealer) > 21:
            print('Dealer went over 21')
            win = True
        elif getTotal(hand) > getTotal(dealer):
            print('Your total: ')
            print(getTotal(hand))
            print('Dealer\'s total: ')
            print(getTotal(dealer))
            print('\n')
            win = True
        else:
            print('Your total: ')
            print(getTotal(hand))
            print('Dealer\'s total: ')
            print(getTotal(dealer))
            print('\n')
            win = False

   
    #if player wins, return double bet (bet already subtracted from chips)
    if win == True:
        print('You win!')
        return(bet*2)
    #if player loses, return nothing or -1 if they...
    #chose to spend chip to be dealt more cards
    else:
        print('You lose :(')
        return(0 - spend)

    
        

        
def main():
    chips = 5
    playGame = True

    #intro
    print('Welcome to Blackjack')
    print('Total chips: ' + str(chips))
    print(input('Press enter to play'))

    #continue new round as long as player wants to and has enough chips
    while chips > 0 and playGame == True:

        #ask player for bet
        bet = toInt(input('How much would you like to bet? (max 10) '))
        #validate bet is within range and a valid number
        while bet > chips or bet == 0:
            if bet >= chips:
                bet = toInt(input('You don\'t have enough chips \nHow much would you like to bet?'))
            else:
                bet = toInt(input('Please enter valid number '))
        print('\n')
        #'spend' chips
        chips -= bet
        #play game and add/subtract any winnings/losings
        chips += game(bet)
        
        #ask if player wants to play again
        print('Total chips: ' + str(chips))
        again = ''
        while again != 'y' and again != 'n':
          again = input("Would you like to play again? (y or n)")
        if again == 'y':
            playGame = True
        elif again == 'n':
            playGame = False

    #if player choses to end game or out of chips
    print("\nGame over")
    print("Total chips:")
    print(chips)

    
main()
        

  
