# Basta Fazoolin'_Objective_Flask
# You’ve started a position as the lead programmer for the family-style 
# Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been 
# doing fantastically and seen a lot of growth lately. You’ve been hired to 
# keep things organized. If you get stuck during this project or would like 
# to see an experienced developer work through it, click “Get Unstuck“ to 
# see a project walkthrough video.
# 1 Create a Menu class
class Menu:
    # 2 Give Menu a constructor ( функция мында конструкция 
    # деп аталып тұр) with the five parameters:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
        # 7 Give our Menu class a string representation method that will 
        # tell you the name of the menu. Also, indicate in this 
        # representation when the menu is available.
    def __repr__(self):
        return self.name + ' brunch menu available from ' + str(self.start_time) + ' - ' +  str(self.end_time)
#print(brunch)
# 9 Give Menu a method .calculate_bill() that has two parameters: 
# self, and purchased_items, a list of the names of purchased items.
# Have calculate_bill return the total price of a purchase consisting 
# of all the items in purchased_items.
    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill
# 3 Brunch
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 
  'burger': 11.00, 'home fries': 4.50, 
  'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 
  'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
# 10 Test out Menu.calculate_bill(). We have a breakfast order for 
# one order of pancakes, one order of home fries, and one coffee. 
# Pass that into brunch.calculate_bill() and print out the price.
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(brunch_menu.name)
# 4 Early Bird
early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early_Bird_Dinners', 
early_bird_items, 1500, 1800)
# 11 What about an early-bird purchase? Our last guests ordered the 
# salumeria plate and the vegan mushroom ravioli. Calculate the bill
# with .calculate_bill().
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#print(early_bird_menu.start_time)
# 5 Dinner
dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)
#print(dinner_menu.end_time)
# 6 Kids
kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, 1100, 2100)
print(kids_menu)