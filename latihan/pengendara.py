from karakter import Karakter

class Pengendara(Karakter):
    def __init__(self, nama: str, kekuatan: int):
        super().__init__(nama, kekuatan)

    def menyerang(self) -> str:
        return f"{self.get_nama()} menabrak gengan kekuatan: {self.get_kekuatan()}"
        