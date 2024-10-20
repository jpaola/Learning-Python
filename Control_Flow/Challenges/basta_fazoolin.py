"""
You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart.
The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.
"""


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"Franchise located at {self.address}"

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            try:
                bill += self.items[purchased_item]
            except KeyError:
                print(f"Item {purchased_item} not found in menu.")
        return bill


# MENU Items
brunch_menu_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_menu_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_menu_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_menu_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_menu_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# MENU Options
brunch_menu = Menu("Brunch", brunch_menu_items, 1100, 1600)
early_bird_menu = Menu("Early Bird", early_bird_menu_items, 1500, 1800)
dinner_menu = Menu("Dinner", dinner_menu_items, 1700, 2300)
kids_menu = Menu("Kids", kids_menu_items, 1100, 2100)
arepas_menu = Menu("Take a’ Arepa", arepas_menu_items, 1000, 2000)

print(kids_menu)  # Kids menu available from 1100 to 2100
print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))  # 13.5
print(early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))  # 21.5

# FRANCHISES
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

print(flagship_store)  # Franchise located at 1232 West End Road
print(new_installment)  # Franchise located at 12 East Mulberry Street
print(flagship_store.available_menus(1200))  # [Brunch menu available from 1100 to 1600, Kids menu available from
# 1100 to 2100]
print(flagship_store.available_menus(1700))  # [Early Bird menu available from 1500 to 1800, Dinner menu available
# from 1700 to 2300, Kids menu available from 1100 to 2100]

# BUSINESS
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a' Arepa", [arepas_place])

print(arepa.franchises[0].menus[0])  # Take a’ Arepa menu available from 1000 to 2000
