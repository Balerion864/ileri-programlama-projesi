from models import Takim, Oyuncu, Mac
from veri_islemleri import verileri_kaydet, verileri_yukle, txt_raporu_olustur
from datetime import datetime

def takimi_bul_ve_getir(takimlar, takim_adi):
    for t in takimlar:
        if t.ad.lower() == takim_adi.lower():
            return t
    yeni_takim = Takim(takim_adi, 2024)
    takimlar.append(yeni_takim)
    return yeni_takim

def ana_menu():
    takimlar, maclar = verileri_yukle()
    
    # listedeki mac sayisini sinif degiskenine esitleyelim
    Mac.toplam_mac_sayisi = len(maclar)
    
    while True:
        print("\n=== TURNUVA VE ISTATISTIK SISTEMI ===")
        print("1 - Mac Sonucu Gir")
        print("2 - Oyuncu Ekle")
        print("3 - Kralliklari Goster")
        print("4 - Puan Durumu")
        print("5 - TXT Raporu Al")
        print("6 - Kaydet ve Cikis")
        
        secim = input("Seciminiz (1-6): ")
        
        if secim == '1':
            try:
                ev_ad = input("Ev Sahibi: ")
                dep_ad = input("Deplasman: ")
                ev_skor = int(input("Ev Sahibi Skor: "))
                dep_skor = int(input("Deplasman Skor: "))
                
                if ev_skor < 0 or dep_skor < 0:
                    print("Hata: Skor eksili bir deger olamaz!")
                    continue
                
                ev_takim = takimi_bul_ve_getir(takimlar, ev_ad)
                dep_takim = takimi_bul_ve_getir(takimlar, dep_ad)
                
                ev_takim.mac_sonucu(ev_skor, dep_skor)
                dep_takim.mac_sonucu(dep_skor, ev_skor)
                
                bugun = datetime.now().strftime("%Y-%m-%d")
                yeni_mac = Mac(ev_ad, dep_ad, ev_skor, dep_skor, bugun)
                maclar.append(yeni_mac)
                print("Mac kaydedildi.")
                
            except ValueError:
                print("Lutfen skor kisminda sadece sayi kullanin.")
                
        elif secim == '2':
            t_ad = input("Takim Adi: ")
            takim = takimi_bul_ve_getir(takimlar, t_ad)
            
            o_ad = input("Oyuncu Adi: ")
            o_mevki = input("Mevki: ")
            
            try:
                yeni_oyuncu = Oyuncu(o_ad, o_mevki, takim.ad)
                gol_sayisi = int(input("Gol Sayisi: "))
                asist_sayisi = int(input("Asist Sayisi: "))
                
                yeni_oyuncu.gol = gol_sayisi
                yeni_oyuncu.asist = asist_sayisi
                
                takim.oyuncular.append(yeni_oyuncu)
                print("Oyuncu sisteme eklendi.")
                
            except ValueError as e:
                print(f"Hatali giris: {e}")
                
        elif secim == '3':
            tum_oyuncular = []
            for t in takimlar:
                for o in t.oyuncular:
                    tum_oyuncular.append(o)
                    
            if not tum_oyuncular:
                print("Sistemde kayitli oyuncu yok.")
                continue
                
            print("\n--- GOL KRALLIGI ---")
            gol_kralligi = sorted(tum_oyuncular, key=lambda x: x.gol, reverse=True)
            for o in gol_kralligi[:5]:
                print(f"{o.ad} ({o.takim_adi}) - {o.gol} Gol")
                
            print("\n--- ASIST KRALLIGI ---")
            asist_kralligi = sorted(tum_oyuncular, key=lambda x: x.asist, reverse=True)
            for o in asist_kralligi[:5]:
                print(f"{o.ad} ({o.takim_adi}) - {o.asist} Asist")
                
        elif secim == '4':
            print("\n--- PUAN DURUMU ---")
            sirali_takimlar = sorted(takimlar, key=lambda x: x.puan, reverse=True)
            print(f"{'Takim':<15} | {'O':<3} | {'G':<3} | {'B':<3} | {'M':<3} | {'P':<3}")
            print("-" * 45)
            for t in sirali_takimlar:
                oynanan_mac = t.galibiyet + t.beraberlik + t.maglubiyet
                print(f"{t.ad:<15} | {oynanan_mac:<3} | {t.galibiyet:<3} | {t.beraberlik:<3} | {t.maglubiyet:<3} | {t.puan:<3}")
                
        elif secim == '5':
            txt_raporu_olustur(takimlar)
            print("Veriler rapor.txt olarak masaustune cikarildi.")
            
        elif secim == '6':
            verileri_kaydet(takimlar, maclar)
            print(f"Toplam {Mac.toplam_mac_sayisi} mac kaydedildi. Program kapaniyor.")
            break
            
        else:
            print("Lutfen 1 ile 6 arasinda bir secim yapin.")

if __name__ == '__main__':
    ana_menu()