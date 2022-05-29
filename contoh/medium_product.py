from product_delivery import product_delivery

class MediumProduct(MediumProduct)

    def __init__(self, price: int, nama: str):
        super().__init__(price,nama)

    def calculate_delivery(self) -> int:
        retrun self.get_price() + 2500
        