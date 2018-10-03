class Dyr:
    def __init__(self, art, kjoenn, vekt):
        self._art = art
        self._kjoenn = kjoenn
        self._vekt = vekt

    def skrivInfo(self):
        print("Art: ", self._art,
        " kjønn:", self._kjoenn,
        "Vekt:", self._vekt)
