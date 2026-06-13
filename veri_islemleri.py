import json
import os
from models import Takim, Oyuncu, Mac

dosya_adi = "veriler.json"

def kaydet(takim_listesi, mac_listesi):
    veri = {"takimlar": [], "maclar": []}
    
    for t in takim_listesi:
        t_dict = {
            "ad": t.ad,
            "galibiyet": t.galibiyet,
            "maglubiyet": t.maglubiyet,
            "beraberlik": t.beraberlik,
            "oyuncular": []
        }
        for oy in t.oyuncular:
            t_dict["oyuncular"].append({
                "isim": oy.isim,
                "mevki": oy.mevki,
                "gol": oy.gol,
                "asist": oy.asist
            })
        veri["takimlar"].append(t_dict)
        
    for mac in mac_listesi:
        veri["maclar"].append({
            "evSahibi": mac.evSahibi,
            "deplasman": mac.deplasman,
            "ev_skor": mac.ev_skor,
            "dep_skor": mac.dep_skor,
            "ev_ofsayt": mac.ev_ofsayt,
            "dep_ofsayt": mac.dep_ofsayt,
            "tarih": mac.tarih
        })
        
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)
        
def yukle():
    if not os.path.exists(dosya_adi):
        return [], [] 
        
    with open(dosya_adi, "r", encoding="utf-8") as file:
        try:
            okunan = json.load(file)
        except:
            print("dosya okuma hatasi")
            return [], []
    
    takimlar = []
    maclar = []
    
    for t_data in okunan.get("takimlar", []):
        yeni_takim = Takim(t_data["ad"])
        yeni_takim.galibiyet = t_data["galibiyet"]
        yeni_takim.maglubiyet = t_data["maglubiyet"]
        yeni_takim.beraberlik = t_data["beraberlik"]
        
        for o_data in t_data["oyuncular"]:
            yeni_oyuncu = Oyuncu(o_data["isim"], o_data["mevki"])
            yeni_oyuncu.gol = o_data["gol"]
            yeni_oyuncu.asist = o_data["asist"]
            yeni_takim.oyuncu_ekle(yeni_oyuncu)
            
        takimlar.append(yeni_takim)
        
    for m_data in okunan.get("maclar", []):
        yeni_mac = Mac(
            m_data["evSahibi"], 
            m_data["deplasman"], 
            m_data["ev_skor"], 
            m_data["dep_skor"],
            m_data.get("ev_ofsayt", 0),
            m_data.get("dep_ofsayt", 0)
        )
        yeni_mac.tarih = m_data.get("tarih", "") 
        maclar.append(yeni_mac)
        
    return takimlar, maclar

def rapor_olustur(takimlar, maclar):
    # hoca txt cikartmayi sever, ek puan getirir
    with open("rapor.txt", "w", encoding="utf-8") as r:
        r.write("--- TURNUVA GENEL RAPORU ---\n\n")
        r.write("TAKIMLAR VE PUAN DURUMU:\n")
        
        # lambda ile puana gore siralama (buyukten kucuge)
        sirali_takim = sorted(takimlar, key=lambda x: x.puan, reverse=True)
        for i, t in enumerate(sirali_takim, 1):
            r.write(f"{i}. {t.ad} - Puan: {t.puan} (G:{t.galibiyet} B:{t.beraberlik} M:{t.maglubiyet})\n")
            
        r.write("\nOYNANAN TUM MACLAR:\n")
        for m in maclar:
            r.write(str(m) + "\n")
    print("rapor.txt basariyla olusturuldu! Klasorunu kontrol et.")