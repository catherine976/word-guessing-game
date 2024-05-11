import random

listOfWords = [
  "guava", "pineapple", "orange", "mango", "raspberry", "avocado", "strawberry", "kiwi", "grapes", "lemon", "banana", "papaya"
]
wordChosen = random.choice(listOfWords)
newList = list(wordChosen)
answer = ""
count = 6
for letter in range(len(wordChosen)):
  answer = answer + "_"
  ansList = list(answer)
while True:
  letter = input("Pick a letter >").strip().lower()
  if letter in wordChosen:
    newIndex = newList.index(letter)
    newList[newIndex] = 0
    ansList[newIndex] = letter
    answer = "".join(ansList)
    print("Correct!")
    print(answer)
  else:
    print("Nope, not in there")
    count -= 1
    if count == 0:
      print("You lost!")
      break
    else:
      print(f"You have {count} lives left.")
  if "_" not in answer:
    print(f"Congratulations! You won with {count} lives left.")
    break
