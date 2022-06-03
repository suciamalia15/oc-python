from penembak import Penembak
from pemukul import Pemukul
from pengendara import Pengendara

penembak1 = Penembak("Aljar", 80)
pemukul1 = Pemukul("Suci", 50)
pengendara1 = Pengendara("Lala", 30)

print(penembak1.menyerang(), pemukul1.menyerang(),
      pengendara1.menyerang(), sep="\n")


