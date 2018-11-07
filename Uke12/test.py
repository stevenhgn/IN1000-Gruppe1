from julekalender import Julekalender

def main():
    kalender = Julekalender(["Steven", "Daniel", "Kristine", "Sara", "Odin"], "gavefil.txt")

    for i in range(24):
        kalender.nyDag()

    kalender.gaveOversikt()

main()
