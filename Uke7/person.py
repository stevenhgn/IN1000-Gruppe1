class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def settNavn(self, navn):
        self._navn = navn

    def skrivNavn(self):
        print("Jeg heter", self._navn)

    def hentAlder(self):
        print(self._alder)
