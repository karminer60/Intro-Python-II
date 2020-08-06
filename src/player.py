# Write a class to hold player information, e.g. what room they are in
# currently.

class Basics:
    #cosntructor
  def __init__(self, room:
      self.room = room
      
class Player(Basics):
    def __init__(self, name, room):
        # `super` method allows us to access the parent class
        super().__init__(room)
        self.name = name
    
    def __str__(self):
        return f"Player: {self.name}, {self.room}"
