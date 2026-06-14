class Takim:
    # Takimlarin istatistiklerini tuttugumuz ana sinif
    def __init__(self, ad, kurulus_yili):
        self.ad = ad
        self.kurulus_yili = kurulus_yili
        self.galibiyet = 0
        self.beraberlik = 0
        self.maglubiyet = 0
        self.oyuncular = []

    def mac_sonucu(self, atilan, yenilen):
        # maca gore takim galibiyet durumunu guncelle
        if atilan > yenilen:
            self.galibiyet += 1
        elif atilan == yenilen:
            self.beraberlik += 1
        else:
            self.maglubiyet += 1

    @property
    def puan(self):
        return (self.galibiyet * 3) + (self.beraberlik * 1)


class Oyuncu:
    def __init__(self, ad, mevki, takim_adi):
        self.ad = ad
        self.mevki = mevki
        self.takim_adi = takim_adi
        self._gol = 0
        self._asist = 0

    @property
    def gol(self):
        return self._gol
    
    @gol.setter
    def gol(self, deger):
        if deger < 0:
            raise ValueError("Gol sayisi negatif girilemez!")
        self._gol = deger

    @property
    def asist(self):
        return self._asist
    
    @asist.setter
    def asist(self, deger):
        if deger < 0:
            raise ValueError("Asist sayisi negatif girilemez!")
        self._asist = deger


class Mac:
    toplam_mac_sayisi = 0

    def __init__(self, ev_sahibi, deplasman, ev_skor, dep_skor, tarih, yeni_kayit=True):
        self.ev_sahibi = ev_sahibi
        self.deplasman = deplasman
        self.ev_skor = ev_skor
        self.dep_skor = dep_skor
        self.tarih = tarih
        
        # sadece yeni girilen maclarda sayaci artir, json yuklerken artirma
        if yeni_kayit:
            Mac.toplam_mac_sayisi += 1