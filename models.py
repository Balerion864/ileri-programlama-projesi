from datetime import datetime

class Oyuncu:
    def __init__(self, isim, mevki):
        self.isim = isim
        self.mevki = mevki
        self._gol = 0
        self._asist = 0

    @property
    def gol(self):
        return self._gol

    @gol.setter
    def gol(self, miktar):
        if miktar < 0:
            # hoca raise ile yakalamamizi istemisti
            raise ValueError("hata: gol sayisi sifirin altina dusemez!")
        self._gol = miktar

    @property
    def asist(self):
        return self._asist

    @asist.setter
    def asist(self, miktar):
        if miktar <0 :
            raise ValueError("hata: asist eksili olamaz")
        self._asist = miktar

    def __str__(self):
        return f"{self.isim} ({self.mevki}) - Gol: {self.gol}, Asist: {self.asist}"


class Mac:
    toplam_mac = 0 # class degiskeni burda

    def __init__(self, evSahibi, deplasman, ev_skor, dep_skor, ev_ofsayt=0, dep_ofsayt=0):
        self.evSahibi = evSahibi  
        self.deplasman= deplasman
        self.ev_skor =ev_skor
        self.dep_skor= dep_skor
        self.ev_ofsayt = ev_ofsayt
        self.dep_ofsayt = dep_ofsayt
        
        # bonus 2 icin zaman damgasi
        self.tarih = datetime.now().strftime('%Y-%m-%d %H:%M')
        Mac.toplam_mac += 1 

    def __str__(self):
        return f"[{self.tarih}] {self.evSahibi} {self.ev_skor} - {self.dep_skor} {self.deplasman} | Ofsayt: ({self.ev_ofsayt}-{self.dep_ofsayt})"


class Takim:
    def __init__(self, ad):
        self.ad = ad
        self.galibiyet = 0
        self.maglubiyet = 0
        self.beraberlik= 0
        self.oyuncular = [] 

    # Puan Durumu icin otomatik hesaplama 
    @property
    def puan(self):
        return (self.galibiyet * 3) + (self.beraberlik * 1)

    def oyuncu_ekle(self, oyuncu):
        self.oyuncular.append(oyuncu)

    def mac_sonucu(self, atilan, yenilen):
        if atilan > yenilen:
            self.galibiyet +=1
        elif atilan < yenilen:
            self.maglubiyet += 1
        else:
            self.beraberlik +=1

    def istatistik_goster(self):
        print(f"\n--- {self.ad} TAKIM İSTATİSTİKLERİ ---")
        print(f"Puan: {self.puan} | galibiyet: {self.galibiyet} | beraberlik: {self.beraberlik} | maglubiyet: {self.maglubiyet}")
        print("oyuncu listesi:")
        if len(self.oyuncular) == 0:
            print("kayitli oyuncu yokk")
        else:
            for o in self.oyuncular:
                print("-> " + str(o))
        print("---------------------------------------\n")