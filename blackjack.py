import random



def card_draw(min_value=1, max_value=11):
      return random.randint(min_value, max_value)

newRole = card_draw()
playerDraw = random.randint(1, 11)
aiDraw = random.randint(1, 11)


userInput = input(f'you draw {playerDraw} , type "yes" or "no"').strip().lower():
if userInput == "yes":
    print('you drew' +playerDraw)
    playerTotal = playerDraw + newRole
    if playerTotal > 21:
        print('you have ' +playerTotal+ ', bust')
    elif playerTotal < 21:
        print('you have ' +playerTotal+ ', do you want to draw again? "yes" or "no"')
        contPlay = input()
        if contPlay == "yes":
        playerTotal + newRole
elif userInput == "no":
     aiDraw + newRole
        if aiDraw > 21:
         print(f'AI has {aiDraw} and you have {playerTotal} you win')
          
