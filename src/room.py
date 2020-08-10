# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'You are now in {self.name} and  {self.description}'
    
     def add_item_to_room(self,*args):
        for arg in args:
            self.items.append(arg)
        return f"item added"

    def remove_item_from_room(self,item_name):
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)
        return f"item removed"
    
    def check_item(self, item_name):
        for item in self.items:
            if item_name == item.name:
                return item
        return False