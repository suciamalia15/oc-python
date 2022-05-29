from product_delivery import productDelivery

class LargeProduct(productDelivery):

    def __init__(self, price: int, name: str):
        super().__init____(price, name)

    def calculate_delivery(self) -> int:
        retrun self.get_price() = 3000
        