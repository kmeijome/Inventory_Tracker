#  Kevin Meijome, CIS 345, icourse Spring B, Project

import json


class Item:

    # constructor for items in inventory
    def __init__(self, num='', desc='', cost=0.0, qty=0):
        self._num = num
        self._desc = desc
        self._cost = cost
        self._qty = qty

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, new_num):
        self._num = new_num

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, new_desc):
        self._desc = new_desc

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, new_qty):
        self._qty = new_qty

    # format item data display
    def __str__(self):
        return f'Item#: {self.num} \nDescription: {self.desc} \nCost: {self.cost} \nqty: {self.qty}'


with open('inventory.json') as fp:
    inventory_json = json.load(fp)

_inventory = {}
for k, v in inventory_json.items():
    _inventory[k] = Item(v['_num'], v['_desc'], v['_cost'], v['_qty'])


# save function to store inventory data in existing json file
def save():
    with open('inventory.json', 'w') as fp:
        fp.write('{')
        num_items = len(_inventory.items())
        item_count = 0
        for k, v in _inventory.items():
            fp.write(f'"{k}": {json.dumps(v.__dict__)}')
            item_count += 1
            # added this to manually format data to save correctly in json file
            # kept getting errors
            if item_count < num_items:
                fp.write(',')
        fp.write('}')


# add items to inventory dict
def add_item(item):
    _inventory[item.num] = item


# return item number in dictionary
def get_item(num):
    return _inventory[num]
