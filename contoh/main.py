from medium_product import MediumProduct
from large_product import LargeProduct
from small_product import SmallProduct

small = SmallProduct(5000, "Popcorn")
print(small.calculate_delivery())

medium = MediumProduct(6000, "Popcron")
print(medium.calculate_delivery())

large = LargeProduct(7000, "Popcron")
print(large.calculate_delivery())