from medium_product import MediumProduct
from Large_Product import LargeProduct
from small_product import smallProduct

small = smallProduct(5000, "Popcorn")
prin(small.calculate_delivery())

medium = MediumProduct(6000, "Popcron")
prin(medium.calculate_delivery())

large = LargeProduct(7000, "Popcron")
prin(large.calculate_delivery())