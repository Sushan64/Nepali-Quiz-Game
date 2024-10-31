questions = ("In which district is the ‘Fungfung’ waterfall?",
             "How many heritage properties are listed in the World Heritage List?",
             "Who was the first to use the word ‘Jai Nepal’?",
             "How many national pride projects are there in Nepal right now?",
             "What percentage of the total land area of Nepal is cultivated on land?",
             "Which is Nepal’s first highway?",
             "What is the name of road: Kathmandu – Pokhara?",
             "What is called the blank sheet on the front and back of the book?",
             "Who is the ‘Zero’ Inventor?",
             "From which district did tea cultivation originate in Nepal?")


options = (("A. Manaag", "B. Mustang", "C. Bhankuta", "D. Nuwakot"),
          ("A. 9", "B. 10", "C. 11", "D. 12"),
          ("A. Puspa Kamal Dahal", "B. BP Koirala", "C. Shukraraj Shastri", "D. Prithivi Narayana Shah"),
          ("A. 21", "B. 22", "C. 23", "D. 24"),
          ("A. 17.95%", "B. 17.96%", "C. 17.97%", "D. 17.87%"),
          ("A. Araniko Highway", "B. Tribhuvan Highway", "C. Prithiwi Highway", "D. Mahendra Highway"),
          ("A. BP Highway", "B. Prithwi Highway", "C. Araniko Highway", "D. Mahendra Highway"),
          ("A. Fly Leaf", "B. No Paper", "C. Blank Cover", "D. Clean Leaf"),
          ("A. Newton", "B. Balmeeki", "C. Arya Bhatt", "D. Albert Einstein"),
          ("A. Jhapa", "B. Sholukhumbu", "C. Bhankuta", "D. ilam"))


answer = ("D",
         "B",
         "C",
         "C",
         "C",
         "B",
         "B",
         "A",
         "C",
         "D")

i = 0
score = 0
guess = []
for question in questions:

  print(question)
  for o in range(0, len(options[i])):
    if o == (len(options[i]) -1):
      print(options[i][o])
    else:
      print(options[i][o], end=', ')
  user_choose = input("Enter (A, B, C, D): ").upper()
  
  guess.append(user_choose) # add the user choice in the list guess[]
  
  if user_choose == answer[i]:
    print('—————————————')
    print('COORECT!')
    score += 1
  else:
    print('—————————————')
    print('INCORRECT!')
    print(f"Correct answer is {answer[i]}")
  print('—————————————')
  
  i += 1

print("Your guess: ", end="")
for g in range(0, len(guess)):
  if g == (len(guess) -1):
    print(guess[g])
  else:
    print(guess[g], end=", ")

print("Correct Answers: ", end="")
for a in range(0, len(answer)):
  if a == (len(answer) -1):
    print(answer[a])
  else:
    print(answer[a], end=", ")
print(f"Your score is {score}/{len(questions)}")
