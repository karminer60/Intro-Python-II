# Write a class to hold player information, e.g. what room they are in
# currently.
class Player : 
    def __init__ (self, name, room, inventory = []):
        self.name = name
        self.room = room
        self.inventory = inventory 

    def add_item(self, item):
        self.inventory.append(item)
     

    def remove_item(self, item_name):
        for item in self.inventory:
            if item_name == item.name:
                self.inventory.remove(item)

    def get_item_name(self, item_name):
        for item in self.inventory:
            if item_name == item.name:
                return item
            else:
                return False




