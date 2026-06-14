from models import Takim, Oyuncu, Mac
from veri_islemleri import verileri_kaydet, verileri_yukle, txt_raporu_olustur
from datetime import datetime

def takimi_bul_veya_olustur(takimlar, takim_adi):
    for t in takimlar:
        if t.ad.lower() == takim_adi.lower():
            return t
    yeni_takim = Takim(takim_adi, 2024)
    takimlar.append(yeni_takim)
    return yeni_takim

def ana_menu():
    takimlar, maclar = verileri_yukle()
    
    while True:
        print("\n=== FUTBOL TURNUVA VE İSTATİSTİK YÖNETİM SİSTEMİ ===")
        print("1 - Maç Sonucu Ekle")
        print("2 - Oyuncu Ekle ve İstatistik Güncelle")
        print("3 - Gol ve Asist Krallığı")
        print("4 - Puan Durumu Göster")
        print("5 - Tüm Verileri TXT Olarak Çıktı Al")
        print("6 - Kaydet ve Çık")
        
        secim = input("Seçiminiz (1-6): ")
        
        if secim == '1':
            try:
                ev_ad = input("Ev Sahibi Takım Adı: ")
                dep_ad = input("Deplasman Takım Adı: ")
                ev_skor = int(input("Ev Sahibi Skor: "))
                dep_skor = int(input("Deplasman Skor: "))
                
                ev_takim = takimi_bul_veya_olustur(takimlar, ev_ad)
                dep_takim = takimi_bul_veya_olustur(takimlar, dep_ad)
                
                ev_takim.mac_sonucu(ev_skor, dep_skor)
                dep_takim.mac_sonucu(dep_skor, ev_skor)
                
                bugun = datetime.now().strftime("%Y-%m-%d")
                yeni_mac = Mac(ev_ad, dep_ad, ev_skor, dep_skor, bugun)
                maclar.append(yeni_mac)
                print("Maç başarıyla kaydedildi!")
                
            except ValueError:
                print("Hata: Skorlar sadece sayı olmalıdır!")
                
        elif secim == '2':
            t_ad = input("Oyuncunun Takımı: ")
            takim = takimi_bul_veya_olustur(takimlar, t_ad)
            
            o_ad = input("Oyuncu Adı: ")
            o_mevki = input("Mevki: ")
            
            try:
                # Oyuncuyu oluştururken artık takım adını da (t.ad) parametre olarak veriyoruz
                yeni_oyuncu = Oyuncu(o_ad, o_mevki, takim.ad)
                gol_sayisi = int(input("Gol Sayısı: "))
                asist_sayisi = int(input("Asist Sayısı: "))
                
                yeni_oyuncu.gol = gol_sayisi
                yeni_oyuncu.asist = asist_sayisi
                
                takim.oyuncular.append(yeni_oyuncu)
                print("Oyuncu ve istatistikleri başarıyla eklendi!")
                
            except ValueError as e:
                print(f"Hata: Geçersiz değer girdiniz. Detay: {e}")
                
        elif secim == '3':
            tum_oyuncular = []
            for t in takimlar:
                for o in t.oyuncular:
                    tum_oyuncular.append(o)
                    
            if not tum_oyuncular:
                print("Henüz sisteme oyuncu eklenmemiş.")
                continue
                
            print("\n--- GOL KRALLIĞI ---")
            gol_kralligi = sorted(tum_oyuncular, key=lambda x: x.gol, reverse=True)
            for o in gol_kralligi[:5]: # İlk 5'i göster
                print(f"{o.ad} ({o.takim_adi}) - {o.gol} Gol")
                
            print("\n--- ASİST KRALLIĞI ---")
            asist_kralligi = sorted(tum_oyuncular, key=lambda x: x.asist, reverse=True)
            for o in asist_kralligi[:5]: # İlk 5'i göster
                print(f"{o.ad} ({o.takim_adi}) - {o.asist} Asist")
                
        elif secim == '4':
            print("\n--- PUAN DURUMU ---")
            sirali_takimlar = sorted(takimlar, key=lambda x: x.puan, reverse=True)
            print(f"{'Takım':<15} | {'Oynanan':<7} | {'G':<3} | {'B':<3} | {'M':<3} | {'Puan':<4}")
            print("-" * 50)
            for t in sirali_takimlar:
                oynanan_mac = t.galibiyet + t.beraberlik + t.maglubiyet
                print(f"{t.ad:<15} | {oynanan_mac:<7} | {t.galibiyet:<3} | {t.beraberlik:<3} | {t.maglubiyet:<3} | {t.puan:<4}")
                
        elif secim == '5':
            txt_raporu_olustur(takimlar)
            print("Veriler 'rapor.txt' dosyasına başarıyla aktarıldı!")
            
        elif secim == '6':
            verileri_kaydet(takimlar, maclar)
            print(f"Sistem kapatılıyor... Toplam oynanan maç: {Mac.toplam_mac_sayisi}")
            break
            
        else:
            print("Geçersiz seçim, lütfen 1-6 arası bir rakam giriniz.")

if __name__ == '__main__':
    ana_menu()