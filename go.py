#!/bin/python
import RuntimeSetup

class GoIshi:
  """ The Go-Ishi are the stones placed upon the Go-Ban.


  All of the game stats concerning the two players are stored
  within pre-structured dictionaries named GoIshi.Black and
  GoIshi.White, respectively.


  Stats, or data-points collected on the players include:
  
    -symbol:        Unicode symbol representing the players token.
                    Either ⚫ or ⚪.

    -player:        Nomenclature denoting _who_ is which.
                    Could be the algorithm being tested,
                    the username of a real player, etc.

    -prisoners:     How many of the opponents stones have been
                    captured.

    -points:        Number of empty intersections surrounded by
                    the player.

    -groups:        List of collective 'units' of stones sharing
                    liberties.
      -stones:      Number of stones in the group.
      -members:     Co-Ordinates of the stones within the group.
      -liberties:   Number of liberties collectively shared by
                    the group.

    -living:        How many of those groups contain at least one
                    eye.

    -individual:    Number of groups that contain two or more eyes.
  """
  def __init__(self, player_one=" ", player_two=" "):

    self.player_one = player_one
    self.player_two = player_two

    self.Black = {
      "symbol": "\u26AB",
      "player":player_one,
      "prisoners": 0,
      "points": 0,
      "groups": [],
      "living": 0,
      "individual": 0,
    }

    self.White = {
      "symbol": "\u26AA",
      "player": player_two,
      "prisoners": 0,
      "points": 0,
      "groups": [],
      "living": 0,
      "individual": 0,
    }

    if __name__ ==" __main__": self.__testing__()


  def __testing__(self):

    assert self.Black,\
               "Should be GoIshi.Black."

    assert self.Black['symbol'] == "⚫",\
                                "Should be a black circle emoji."

    assert self.Black['player'] == self.player_one,\
                                "Should be GoIshi.player_one."

    assert self.Black['prisoners'] == 0,\
                                   "Should be 0."

    assert self.Black['points'] == 0,\
                                "Should be 0."

    assert type(self.Black['groups']) == list,\
                                      "Should be list."

    assert self.Black['living'] == 0,\
                                "Should be 0."

    assert self.Black['individual'] == 0,\
                                    "Should be 0."

    assert self.White,\
               "Should be GoIshi.White"

    assert self.White['symbol'] == "⚪",\
                                "Should be a white circle emoji."

    assert self.White['player'] == self.player_two,\
                                "Should be GoIshi.player_two."

    assert self.White['prisoners'] == 0,\
                                   "Should be 0."

    assert self.White['points'] == 0,\
                                "Should be 0."

    assert type(self.White['groups']) == list,\
                                      "Should be list."

    assert self.White['living'] == 0,\
                                "Should be 0."

    assert self.White['individual'] == 0,\
                                    "Should be 0."




# The board itself.
class GoBan:
  """ The Go-Ban is the board upon which the Go-Ishi are placed.

  Unlike Chess, Black goes first, then White.  Also unlike Chess,
  turns are counted by the individual moves as opposed to
  move-response pairs;  i.e, Blacks first move is considered to be
  turn one, while Whites first move is turn two.

  To set up the board we initialize a dictionary of 'positions'
  numbered 1.1 through 19.19, for a total of 361 uniquely
  identified key:value pairs by calling
  GoBan.Initialize_Empty_Board() from GoBan.__init__().

  Play is simulated by writing either GoIshi.Black['symbol'] or
  GoIshi.White['symbol'] to any of these positions not currently
  occupied by a symbol.  When a positions (X+-1).(Y+-1) become
  occupied by an opposing players symbols, the X.Y position in
  question is overwritten by the None type and returns to a state
  of playability. """
  def __init__(self):

    # Set up the game pieces.
    self.GoIshi = GoIshi()
    self.Black = self.GoIshi.Black['symbol']
    self.White = self.GoIshi.White['symbol']

    # Count the number of turns.
    # This will continue to increment by one as moves are taken.
    self.Turn = 0

    # Since Black moves first, even numbered turns indicate it is
    # Blacks move.
    if self.Turn % 2 == 0: self.Move = self.Black
    else: self.Move = self.White

    # Create the board; populate it with 361 positions.
    self.Board = {}; self.Initialize_Empty_Board()

    if __name__ ==" __main__": self.__testing__()


  def __testing__(self):
      assert self.Board,\
                 "Should be GoBan.Board"

      # 19x19 = 361
      assert len(self.Board) == 361,\
                             "Should be 361."

      # No moves have been taken yet.
      assert self.Turn == 0,\
                       "Should be 0."

      # It is currently Black's turn.
      assert self.Move == self.Black,\
                       "Should be Black."


  def Initialize_Empty_Board(self):
    """ Populate GoBan.Board with 361 keys from 1.1 to 19.19,
    each with a value of None. """
    for X in range(1,20):
      for Y in range(1,20):
        self.Board[f"{X}.{Y}"] = None


  def Place_Stone(self, position):
    """ Fill in a position within the board with either
    a Black or a White GoIshi.
                       --Increment the turn by one. """
    self.Board[position] = self.Move

    if self.Move == self.Black: self.Move = self.White
    else: self.Move = self.Black
    
    self.Turn += 1


  def Remove_Stone(self, position):
    """ Return a Black or White value back to None.
    Also tally up the prisoners in the opposing
    players count. """

    # If the position holds a Black stone...
    if self.Board[position] == self.Black:
      self.GoIshi.White["prisoners"] += 1

    # If the position holds a White stone...
    elif self.Board[position] == self.White:
      self.GoIshi.Black["prisoners"] += 1

    # Why was this function called on an empty position?
    else: pass

    self.Board[position] = None





class GoSeki():

  def __init__(self):
    self.GoIshi = GoIshi()
    self.GoBan = GoBan()


  def Count_Dame(self, position):
    """ Count all the neighbors of a given point. """
  
    position = position.split(".")

    X = int(position[0])
    Y = int(position[1])

    dame = []
    cardinals = [
                  f"{X}.{Y+1}",# North
                  f"{X}.{Y-1}",# South
                  f"{X+1}.{Y}",# East
                  f"{X-1}.{Y}",# West
                                       ]

    for direction in cardinals:
      point = direction.split(".")
      X = int(point[0])
      Y = int(point[1])

      if X or Y <= 0: pass
      elif X or Y > 19: pass
      else: dame.append(direction)      

    return dame


  """ Currently being worked on...
  def Enumerate_Stone_Liberties(self, position):
    coordinates = position.split(".")
  """





class TestingSuite:
  def __init__(self):

    self.Go = GoBan()

    for position in self.Go.Board:
      print(position)



