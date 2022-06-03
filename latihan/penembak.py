from karakter import Karakter

class penembak(Karakter):
    def __init__(self, nama: str,kekuatan: int):
        super().__init__(nama,kekuatan)
        
    def menyerang(self)-> str:
        return f"{self.get_nama()} menembak dengan kekuatan: {self.get_kekuatan()}"