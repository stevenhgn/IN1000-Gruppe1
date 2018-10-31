from student import Student
from fag import Fag

class Studentsystem:
    def __init__(self):
        self._studentListe = []
        self._fagListe = []

# Oppgave 1
    def lesFraFil(self, filnavn):
        fil = open(filnavn)

        # *MAT1001
        for linje in fil:
            if linje[0] == "*":
                fag = Fag(linje[1:-1])
                self._fagListe.append(fag)
            else:
                student = finnStudent(linje[:-1])

                if student == None:
                    student = Student(linje[:-1])
                    self._studentListe.append(student)


                fag.leggTilStudent(student)
                student.leggTilFag(fag)


    def finnStudent(self, navn):
        student = None
        for stud in self._studentListe:
            if stud.hentStudentNavn() == navn:
                student = stud

        return student


    def finnFag(self, emnekode):
        fag = None

        for f in self._fagListe:
            if f.hentFagNavn() == emnekode:
                fag = f

        return fag



# Oppgave 2
    def skrivStudent(self):
        navn = input("Oppgi navnet til person du vil hente oversikt til\n")

        student = finnStudent(navn)

        if student == None:
            print(navn + " finnes ikke i systemet")
        else:
            student.skrivFagPaaStudent()


    def skrivFag(self):
        kode = input("Oppgi emne til faget du vil hente oversikt til\n")

        fag = finnFag(kode)

        if fag == None:
            print(kode + " finnes ikke i systemet")

    def hentStudentMedFlestFag(self):
        studentMedFlest = None
        antallFlest = 0

        for stud in self._studentListe:
            if stud.hentAntallFag() > antallFlest:
                antallFlest = stud.hentAntallFag()
                studentMedFlest = stud

        print("Student med flest fag: " + studentMedFlest.hentStudentNavn()
                + " med antall: " +  antallFlest)


    def hentFagMedFlestStudenter(self):
        fag = None
        antallFlest = 0

        for f in self._fagListe:
            if (f.hentAntallStudent() > antallFlest):
                fag = f
                antallFlest = f.hentAntallStudent()

        print("Fag med flest studenter: " + fag.hentFagNavn()
                + " med antall: " +  antallFlest)


# Oppgave 3
    def settInnStudent(self, navn):

        student = finnStudent(navn)

        if (student == None):
            self._studentListe.append(student)
            print(navn + " lagt til")

        else:
            print(navn + " finnes allerede.")


    def settInnFag(self, navn):
        fag = finnFag(navn)

        if (fag == None):
            self._fagListe.append(fag)
            print(navn + " lagt til")
        else:
            print(navn + " finnes allerede.")



# Oppgave 4
    def leggTilStudentIFag(self):
        navn = input("Hva heter studenten du vil legge til i faget.\n")

        student = finnStudent(navn)

        if student == None:
            print(navn + " finnes ikke i systemet, du må legge studenten inn i systemet først.")
            return

        kode = inpurt("Hva heter emnet du vil legget til " + navn + "i\n")

        fag = finnFag(kode)

        if fag == None:
            print(kode + " finnes ikke i systemet, du må legge faget inn i systemet først.")
            return


        if student.tarFag(fag):
            print(navn + " tar allerede faget.")

        else:
            student.leggTilFag(fag)
            fag.leggTilStudent(student)
            print(navn + " er lagt til i " + kode)



    def ordrelokke(self):
        inntast = ""
        while inntast != "q":
            self.skrivMeny()
            inntast = input("Skriv inn ditt valg: ")

            if inntast == "1":
                self.leggTilStudent()
            elif inntast == "2":
                self.leggTilFag()
            elif inntast == "3":
                self.leggTilStudentIFag()
            elif inntast == "4":
                self.skrivFag()
            elif inntast == "5":
                self.skrivStudent()
            elif inntast == "6":
                self.finnFagMedFlestStudenter()
            elif inntast == "7":
                self.finnStudentMedFlestFag()
            #elif inntast == "8":
                #self.fjernStudentFraFag()
            #elif inntast == "9":
                #self.skrivAlt()
            elif inntast != "q":
                print("Ugylig input.\n")

        print("Avslutter programmet")

    def skrivMeny(self):
        print("--Meny--")
        print("1 - Legg til ny student")
        print("2 - Legg til nytt fag")
        print("3 - Legg til student i fag")
        print("4 - Skriv ut studenter ved fag")
        print("5 - Skriv ut alle fag til student")
        print("6 - Finn fag som blir tatt av flest")
        print("7 - Finn student som tar flest fag")
        #print("8 - Fjern student fra fag")
        #print("9 - Fullstendig oversikt")
        print("q - Avslutt")

    #HVIS TID: 9 - fullstendig oversikt
    def skrivAlt(self):
        for fag in self._alleFag:
            fag.skrivStudenterVedFag()

    #HVIS TID:
    #11-7
    def fjernStudentFraFag(self):
        navn = input("Hva heter studenten du vil fjerne fra faget?")
        stud = self.finnStudent(navn)
        if stud == None:
            print(navn + " finnes ikke.")
            return

        fagNavn = input("Fra hvilket fag vil du fjerne " + navn +"?")
        fag = self.finnFag(fagNavn)
        if fag == None:
            print(fagNavn + " finnes ikke.")
            return

        #sjekker om studenten tar faget, hvis den ikke tar det gjoer vi ikke noe.
        if not stud.tarFag(fag):
            print(navn + " tar ikke " + fagNavn)
        else:
            #hvis studenten finnes, faget finnes, og studenten faktisk tar faget, saa kan vi fjerne den!
            stud.fjernFag(fag)
            fag.fjernStudent(stud)

            print(navn + " fjernet fra " + fagNavn)
