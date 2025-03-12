
class Marketplace:
    def __init__(self, seller, buyer, products):
        self.seller = seller
        self.buyer = buyer
        self.products = products

    def func_for_seller(self):
        return f'prodovets {self.seller} prodaet: {self.products}'

    def func_for_buyer(self):
        return  f' pokupatel {self.buyer} Pokupaet: {self.products}'