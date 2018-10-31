class Fag:
    def __init__(self, navn):
        self._navn = navn
        self._studentListe = []


    def leggTilStudent(self, student):
        self._studentListe.append(student)

    def hentAntallStudent(self):
        return len(self._studentListe)

    def hentFagNavn(self):
        return self._navn

    def hentStudenterVedFag(self):
        print("Fag: ", self._navn)
        for student in self._studentListe:
            print(student.hentStudentNavn())


    #gitt for oppgave 7
    def fjernStudent(self, student):
        self._studentliste.remove(student)
