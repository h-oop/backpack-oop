#Backpack class

class Backpack:
    # Constructor
    def __init__(self, colour, size):
        self.colour = colour
        self.size = size
        self.items = []
        self.open = False
        print(f"")


    # Methods
    def open_bag(self):
        if self.open == False:
            print("bag opened")
            self.open = True
        else:
            print("err")

    def close_bag(self):
        if self.open == True:
            print("bag closed")
            self.open = False
        else:
            print("err")

    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print(f"{item} added to backpack")
        else:
            print("err")

    def takeout(self, item):
        if self.open == True:
            if item in self.items:
                self.items.remove(item)
                print(f"{item} removed from backpack")
            else:
                print("err")
        else:
            print("err")

#make
backpack1 = Backpack("blue", "small")
backpack2 = Backpack("red", "medium")
backpack3 = Backpack("green", "large")

#act
backpack1.open_bag()
backpack1.putin("lunch")
backpack1.putin("jacket")
backpack1.close_bag()
backpack1.open_bag()
backpack1.takeout("jacket")
backpack1.close_bag()
