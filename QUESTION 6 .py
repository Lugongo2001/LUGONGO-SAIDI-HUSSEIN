# Question 6: Farm Inventory Management
farm_inventory = {'Tractor': 2, 'Plough': 5, 'Seeds': 100}
def get_item_quantity(inventory, item_name):
    return inventory.get(item_name, "Item not found")
print(f"Quantity of Ploughs: {get_item_quantity(farm_inventory, 'Plough')}")
print(f"Quantity of Harvester: {get_item_quantity(farm_inventory, 'Harvester')}")
