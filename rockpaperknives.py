import random
winningCombinations = {
        "rock": "knives",
        "paper": "rock",
        "knives": "paper"
}
mySet = {"rock", "paper", "knives"}
myList = list(mySet)
randomWord = random.choice(myList)
print('type "rock", "paper" or "knives"')
userInput = input()
if userInput == randomWord:
        print('you chose ' +userInput+ ' and AI chose ' +randomWord+ ' go again') 
elif winningCombinations[userInput] == randomWord:
        print('you chose ' +userInput+ ' and AI chose ' +randomWord+ ' you win')
else:
        print('you chose ' +userInput+ ' and AI chose ' +randomWord+ ' you lose')
