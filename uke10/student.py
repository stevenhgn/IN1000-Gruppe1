class Student:
    def __init__(self, navn):
        self._navn = navn
        self._fagListe = []

    def leggTilFag(self, fag):
        self._fagListe.append(fag)

    def hentAntallFag(self):
        return len(self._fagListe)

    def hentStudentNavn(self):
        return self._navn

    def skrivFagPaaStudent(self):
        print("Navn:", self._navn)

        for fag in self._fagListe:
            print(fag.hentFagNavn())

    def tarFag(self, navn):
        return navn in self._fagListe

        '''
        if navn in self._fagListe:
            return True
        else:
            return False'''
