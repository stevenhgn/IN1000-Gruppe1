from person import Person

from student import Student

daniel = Student("Daniel")
alexander = Student("Alexander")
nikolas = Student("Nikolas")

studentListe = [daniel,alexander,nikolas]

for i in studentListe:
    i.skrivNavn()
