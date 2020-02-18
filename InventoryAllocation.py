import sys


class inventoryAllocation:

    def __init__(self, inventory, orders):
        self.inventory = inventory
        self.orders = orders
        self.prods = self.getList(self.inventory)

    def getList(self, dict):
        return list(dict.keys())

    def run(self, ord):
        self.input = [0, 0, 0, 0, 0]
        self.allocat = [0, 0, 0, 0, 0]
        self.backOrder = [0, 0, 0, 0, 0]
        self.out = str(ord['Header']) + ': '
        try:
            for i in ord['Lines']:
                self.allocateInventory(i)
        except:
            print("Oops!", sys.exc_info()[0], "occured.")

        print(self.out, self.input, self.allocat, self.backOrder)

    def allocateInventory(self, order):
        if order['Product'] in self.inventory:
            self.input = self.replaceList(self.input, order)
            if self.inventory[order['Product']] >= order['Quantity']:
                self.inventory[order['Product']] = self.inventory[order['Product']] - order['Quantity']
                self.allocat = self.replaceList(self.allocat, order)
            else:
                self.backOrder = self.replaceList(self.backOrder, order)
        # print(self.out, self.input, self.allocat, self.backOrder)
        else:
            print('Error:the ordered product ' + order['Product'] + ' is not supported.')

    def replaceList(self, list, order):
        for i in range(len(list)):
            if i == self.prods.index(order['Product']):
                list[i] = order['Quantity']
        return list

    def processOrders(self):
        for ord in self.orders:
            if all(value == 0 for value in inventory.values()):
                break
            else:
                ia.run(ord)


inventory = {'A': 2, 'B': 3, 'C': 1, 'D': 0, 'E': 0}
ord1 = {"Header": 1, "Lines": [{"Product": "A", "Quantity": 1}, {"Product": "C", "Quantity": 1}]}
ord2 = {"Header": 2, "Lines": [{"Product": "E", "Quantity": 5}]}
ord3 = {"Header": 3, "Lines": [{"Product": "D", "Quantity": 4}]}
ord4 = {"Header": 4, "Lines": [{"Product": "A", "Quantity": 1}, {"Product": "C", "Quantity": 1}]}
ord5 = {"Header": 5, "Lines": [{"Product": "B", "Quantity": 3}]}
ord6 = {"Header": 6,
        "Lines": [{"Product": "A", "Quantity": 3}, {"Product": "C", "Quantity": 1}, {"Product": "Z", "Quantity": 5}]}
orders = [ord1, ord2, ord3, ord4, ord5, ord6]

ia = inventoryAllocation(inventory, orders)
ia.processOrders()
