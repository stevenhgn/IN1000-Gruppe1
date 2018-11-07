from gave import Gave
from barn import Barn

class Julekalender:

    def __init__(self, barnListe, filnavn):
        self._aapnere = [] # liste over alle barn som skal aapne gave
        self._kalender = []
        self._nesteApner = 0
        self._dag = 0

        for navn in barnListe:
            self._aapnere.append(Barn(navn))
        self.lesGavefil(filnavn)

    def lesGavefil(self, filnavn):
        for gave in open(filnavn):
            gaveInfo = gave.split(", ")
            navn = gaveInfo[0]
            pris = float(gaveInfo[1])
            self._kalender.append(Gave(navn, pris))


    def nyDag(self):
        if self._dag >= len(self._kalender):
            print("Jul er over!")
            return

        if self._nesteApner == len(self._aapnere):
            self._nesteApner = 0

        barnSomskalAapne = self._aapnere[self._nesteApner]
        gave = self._kalender[self._dag]
        barnSomskalAapne.aapneGave(gave)

        self._dag +=1
        self._nesteApner +=1

    def gaveOversikt(self):
        for apner in self._aapnere:
            apner.skrivBarn()
