import os
from models import Takim, Mac, Oyuncu
import veri_islemleri

takimlar = []
maclar = []

def takim_bul_veya_olustur(ad):
    for t in takimlar:
        if t.ad.lower() == ad.lower():
            return t
            
    yeni_t = Takim(ad)
    takimlar.append(yeni_t)
    return yeni_t

def ekrani_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def ana_menu():
    global takimlar, maclar
    
    takimlar, maclar = veri_islemleri.yukle()
    
    while True:
        print("\n===========================================")
        print("=== BUÜ İleri Programlama Projesi ===")
        print("=== Hazırlayan: Ömer Faruk ===")
        print(f"-> Sistemdeki Toplam Maç Kaydı: {Mac.toplam_mac}") 
        print("===========================================")
        print("1 - Yeni Maç Ekle (Skor ve Ofsayt)")
        print("2 - Oyuncu Ekle / Bireysel İstatistik Gir")
        print("3 - Puan Durumu ve Gol/Asist Kralligi (YENI)")
        print("4 - Takım İstatistiklerini Görüntüle")
        print("5 - TXT Formatinda Rapor Al (YENI)")
        print("6 - Çıkış ve Kaydet")
        
        secim = input("Ne yapmak istersiniz? (1-6): ")
        
        if secim == '1':
            ev_ad = input("Ev Sahibi Takım: ")
            dep_ad = input("Deplasman Takımı: ")
            
            try:
                ev_skor = int(input(f"{ev_ad} atilan gol: "))
                dep_skor = int(input(f"{dep_ad} atilan gol: "))
                
                ev_ofsayt = int(input(f"{ev_ad} ofsayt sayisi: "))
                dep_ofsayt = int(input(f"{dep_ad} ofsayt sayisi: "))
                
                if ev_skor < 0 or dep_skor < 0 or ev_ofsayt < 0 or dep_ofsayt < 0:
                    raise ValueError("skor veya ofsayt eksi deger alamaz!") 
                    
                yeni_mac = Mac(ev_ad, dep_ad, ev_skor, dep_skor, ev_ofsayt, dep_ofsayt)
                maclar.append(yeni_mac)
                
                ev_takim = takim_bul_veya_olustur(ev_ad)
                dep_takim = takim_bul_veya_olustur(dep_ad)
                
                ev_takim.mac_sonucu(ev_skor, dep_skor)
                dep_takim.mac_sonucu(dep_skor, ev_skor) 
                
                print("mac ve istatistikler basariyla eklendi!")
                
            except ValueError as e:
                print(f"Hata: Lütfen geçerli bir sayi girin! ({e})")
                
        elif secim == '2':
            t_ad = input("Hangi takima oyuncu eklenecek?: ")
            takim = takim_bul_veya_olustur(t_ad)
            
            o_isim = input("Oyuncu ismi: ")
            o_mevki = input("Mevki (Orn: Forvet): ")
            
            try:
                o_gol = int(input(f"{o_isim} kac gol atti?: "))
                o_asist = int(input(f"{o_isim} kac asist yapti?: "))
                
                yeni_oyuncu = Oyuncu(o_isim, o_mevki)
                yeni_oyuncu.gol = o_gol     
                yeni_oyuncu.asist = o_asist 
                
                takim.oyuncu_ekle(yeni_oyuncu)
                print(f"{o_isim} isimli oyuncu sisteme eklendi!")
                
            except ValueError as e:
                print(f"Hata: Gol veya asist sadece rakam olmalidir! ({e})")
                
        elif secim == '3':
            ekrani_temizle()
            print("--- PUAN DURUMU ---")
            
            sirali_takimlar = sorted(takimlar, key=lambda x: x.puan, reverse=True)
            for sira, t in enumerate(sirali_takimlar, 1):
                print(f"{sira}. {t.ad} - Puan: {t.puan} (G:{t.galibiyet} B:{t.beraberlik} M:{t.maglubiyet})")
            
            tum_oyuncular = []
            for t in takimlar:
                for o in t.oyuncular:
                    tum_oyuncular.append(o)
                    
            print("\n--- GOL KRALLIGI ---")
            sirali_gol = sorted(tum_oyuncular, key=lambda x: x.gol, reverse=True)
            for i, o in enumerate(sirali_gol[:3], 1): # sadece ilk 3 u alir
                if o.gol > 0:
                    print(f"{i}. {o.isim} ({t.ad}) - {o.gol} Gol")
                    
            print("\n--- ASIST KRALLIGI ---")
            sirali_asist = sorted(tum_oyuncular, key=lambda x: x.asist, reverse=True)
            for i, o in enumerate(sirali_asist[:3], 1):
                if o.asist > 0:
                    print(f"{i}. {o.isim} ({t.ad}) - {o.asist} Asist")
                    
        elif secim == '4':
            ekrani_temizle()
            if len(takimlar) == 0:
                print("Sistemde henuz takim yok.")
            else:
                for t in takimlar:
                    t.istatistik_goster()
                print("\nSon Oynanan Maclar:")
                for m in maclar:
                    print(m)
                    
        elif secim == '5':
            veri_islemleri.rapor_olustur(takimlar, maclar)
            
        elif secim == '6':
            veri_islemleri.kaydet(takimlar, maclar)
            print("Veriler JSON dosyasina kaydedildi. Cikis yapiliyor. Iyi gunler!")
            break
            
        else:
            print("Gecersiz secim, lutfen 1 ile 6 arasi bi sey girin.")

if __name__ == '__main__':
    ana_menu()