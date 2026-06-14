class Takim:
    """Bir futbol takımının istatistiklerini ve oyuncularını yöneten sınıf."""
    def __init__(self, ad, kurulus_yili):
        self.ad = ad
        self.kurulus_yili = kurulus_yili
        self.galibiyet = 0
        self.beraberlik = 0
        self.maglubiyet = 0
        self.oyuncular = []

    def mac_sonucu(self, atilan, yenilen):
        """Maç sonucuna göre galibiyet, beraberlik veya mağlubiyet sayaçlarını günceller."""
        if atilan > yenilen:
            self.galibiyet += 1
        elif atilan == yenilen:
            self.beraberlik += 1
        else:
            self.maglubiyet += 1

    @property
    def puan(self):
        """Takımın toplam puanını hesaplar (Galibiyet: 3, Beraberlik: 1)."""
        return (self.galibiyet * 3) + (self.beraberlik * 1)


class Oyuncu:
    """Bir futbolcunun gol ve asist istatistiklerini güvenli bir şekilde tutan sınıf."""
    def __init__(self, ad, mevki, takim_adi):
        self.ad = ad
        self.mevki = mevki
        self.takim_adi = takim_adi  # Krallık listesi için takım adını burada tutuyoruz
        self._gol = 0
        self._asist = 0

    @property
    def gol(self):
        return self._gol
    
    @gol.setter
    def gol(self, deger):
        if deger < 0:
            raise ValueError("Gol sayısı negatif olamaz!")
        self._gol = deger

    @property
    def asist(self):
        return self._asist
    
    @asist.setter
    def asist(self, deger):
        if deger < 0:
            raise ValueError("Asist sayısı negatif olamaz!")
        self._asist = deger


class Mac:
    """Oynanan maçların bilgilerini tutan ve toplam maç sayısını sayan sınıf."""
    toplam_mac_sayisi = 0  # Sınıf değişkeni

    def __init__(self, ev_sahibi, deplasman, ev_skor, dep_skor, tarih):
        self.ev_sahibi = ev_sahibi
        self.deplasman = deplasman
        self.ev_skor = ev_skor
        self.dep_skor = dep_skor
        self.tarih = tarih
        Mac.toplam_mac_sayisi += 1