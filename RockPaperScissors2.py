import random as r

player_moves = ["Rock", "Paper", "Scissors"]
bot_moves = ["Rock", "Paper", "Scissors"]
player_move = input("Please choose a move: ").capitalize()
bot_move = r.choice(bot_moves)
if player_moves.__contains__(str(player_move)):
      player = player_move
      bot = bot_move
      print("I choose..." + bot_move + "!")
      assignment = {"Rock": "Player",
                   "Paper": "Player",
                   "Scissors": "Player"}


      def assignments_p():
          if player == "Rock":
             return assignment.update({"Rock": "Player"})
          elif player == "Paper":
              return assignment.update({"Paper": "Player"})
          elif player == "Scissors":
             return assignment.update({"Scissors": "Player"})
          else:
              pass

      def assignments_b():
              if bot == "Rock":
                 return assignment.update({"Rock": "Bot"})
              elif bot == "Paper":
                 return assignment.update({"Paper": "Bot"})
              elif bot == "Scissors":
                  return assignment.update({"Scissors": "Bot"})
              else:
                  pass
      if player == bot:
       print("Its a draw!: " + player + "|" + bot)
      else:


        assignments_p()
        assignments_b()
        if assignment["Rock"] == "Player" or assignment["Rock"] == "Bot" and assignment["Paper"] == "Player" or assignment["Paper"] == "Bot":
          print("The " + str(assignment["Paper"]) + " won the game!: " + player + "|" + bot)
        elif assignment["Rock"] == "Player" or assignment["Rock"] == "Bot" and assignment["Scissors"] == "Player" or assignment["Scissors"] == "Bot":
          print("The " + str(assignment["Rock"]) + " won the game!: " + player + "|" + bot)
        elif assignment["Paper"] == "Player" or assignment["Paper"] == "Bot" and assignment["Rock"] == "Player" or assignment["Rock"] == "Bot":
          print("The " + str(assignment["Paper"]) + " won the game!: " + player + "|" + bot)
        elif assignment["Paper"] == "Player" or assignment["Paper"] == "Bot" and assignment["Scissors"] == "Player" or assignment["Scissors"] == "Bot":
           print("The " + str(assignment["Paper"]) + " won the game!: " + player + "|" + bot)
        else:
            pass
else:
    pass



