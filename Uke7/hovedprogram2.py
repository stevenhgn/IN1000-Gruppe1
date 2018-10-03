from bygning import Bygning


bygning = Bygning("Gata 1", "Hans Hansen", 6, 30)
bygning.hentLeiertaker()

bygning.flyttInn(2)
bygning.hentLeiertaker()
bygning.flyttUt(3)
bygning.hentLeiertaker()
bygning.leieKostnad()
