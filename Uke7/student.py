class Student:
    def __init__(self, navn):
        self._navn = navn

    def skrivNavn(self):
        print("Jeg heter", self._navn)
