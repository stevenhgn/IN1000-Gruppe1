from gave import Gave

class Barn:
    def __init__(self, navn):
        self._navn = navn
        self._gaveListe = []
        self._totalpris = 0


    def hentNavn(self):
        return self._navn

    def totalPris(self):
        return self._totalpris

    def aapneGave(self, gave):
        self._gaveListe.append(gave)
        self._totalpris += gave.hentPris()

    def skrivBarn(self):
        print(self._navn)
        for gave in self._gaveListe:
            print(gave)
        print("Total verdi: " + str(self._totalpris))
