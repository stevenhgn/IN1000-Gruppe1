class Bygning:
    def __init__(self, adresse, huseier, antLeietaker, maxLeietaker):
        self._adresse = adresse
        self._huseier = huseier
        self._antLeietaker = antLeietaker
        self._kostnad = 500
        self._maxLeietaker = maxLeietaker

    def flyttInn(self, ant):
        if (self._antLeietaker + ant > maxLeietaker):
            print("Det er ikke mulig, ikke nok plass")
        else:
            self._antLeietaker += ant

    def flyttUt(self, ant):
        if (self._antLeietaker - ant < 0):
            print("Kan ikke flytte ut", ant, "men kan flytte resterende")
            self._antLeietaker = 0
        else:
            self._antLeietaker -= ant

    def leieKostnad(self):
        print(self._kostnad)

    def ny_huseier(self, nyhuseier):
        self._huseier = nyhuseier

    def hentLeiertaker(self):
        print("Antall leiertaker ", self._antLeietaker)
