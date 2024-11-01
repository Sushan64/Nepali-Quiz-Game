#all file are self made which I provided
from questions import questions as q
from options import options as op
from answer import answer as ans

i = 0 #this is using in loop
score = 0
guess = []
for question in q:

  print(question)
  for o in range(0, len(op[i])):
    if o == (len(op[i]) -1): #this is for not displaying comma in the last.
      print(op[i][o])
    else:
      print(op[i][o], end=', ')
  user_choose = input("Enter (A, B, C, D): ").upper()
  
  guess.append(user_choose) 
  print(f"{user_choose}, {ans[i]}")
  if user_choose == ans[i]:
    print('—————————————')
    print('COORECT!')
    score += 1 #increasing the score of the user
  else:
    print('—————————————')
    print('INCORRECT!')
    print(f"Correct answer is {ans[i]}")
  print('—————————————')
  
  i += 1

print("Your guess: ", end="")
for g in range(0, len(guess)):
  if g == (len(guess) -1):
    print(guess[g])
  else:
    print(guess[g], end=", ")

print("Correct Answers: ", end="")
for a in range(0, len(ans)): #again this is also same, not to display comma in the last e.g. if we don't use this code output will be like A,B,C,D, but after this output will be like A,B,C,D
  if a == (len(ans) -1):
    print(ans[a])
  else:
    print(ans[a], end=", ")
print(f"Your score is {score}/{len(q)}")
