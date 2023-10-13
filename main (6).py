'''Implement a class  called player that represents a cricket player. the player class should have a method
called play() which prints"The player is playing cricket.
Drive two classes,Batsman and Bowler, from the player 
class.Override the play() method in each derrived class to print "The batsman is batting", respectively. Write a program to create objects of both the Batsman and Bowler
classes and call the play() method for each object.'''


# Defline the base class player
class player:
  def player(self):
      print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(player):
  def play(self):
      print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is boling.")

# Create objects of Batsman and Bowler cllasses
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
