import json
from models import Takim, Oyuncu, Mac

def verileri_kaydet(takimlar, maclar, dosya_adi="veriler.json"):
    data = {"takimlar": [], "maclar": []}
    
    for t in takimlar:
        takim_dict = {
            "ad": t.ad,
            "kurulus_yili": t.kurulus_yili,
            "galibiyet": t.galibiyet,
            "beraberlik": t.beraberlik,
            "maglubiyet": t.maglubiyet,
            "oyuncular": []
        }
        for o in t.oyuncular:
            takim_dict["oyuncular"].append({
                "ad": o.ad,
                "mevki": o.mevki,
                "takim_adi": o.takim_adi,
                "gol": o.gol,
                "asist": o.asist
            })
        data["takimlar"].append(takim_dict)
        
    for m in maclar:
        data["maclar"].append({
            "ev_sahibi": m.ev_sahibi,
            "deplasman": m.deplasman,
            "ev_skor": m.ev_skor,
            "dep_skor": m.dep_skor,
            "tarih": m.tarih
        })
        
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def verileri_yukle(dosya_adi="veriler.json"):
    takimlar = []
    maclar = []
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            for t_data in data.get("takimlar", []):
                t = Takim(t_data["ad"], t_data["kurulus_yili"])
                t.galibiyet = t_data["galibiyet"]
                t.beraberlik = t_data["beraberlik"]
                t.maglubiyet = t_data["maglubiyet"]
                
                for o_data in t_data.get("oyuncular", []):
                    o = Oyuncu(o_data["ad"], o_data["mevki"], o_data["takim_adi"])
                    o.gol = o_data["gol"]
                    o.asist = o_data["asist"]
                    t.oyuncular.append(o)
                takimlar.append(t)
                
            for m_data in data.get("maclar", []):
                # eski veriyi yuklerken sayaci bozmamasi icin yeni_kayit=False dedik
                m = Mac(m_data["ev_sahibi"], m_data["deplasman"], m_data["ev_skor"], m_data["dep_skor"], m_data["tarih"], yeni_kayit=False)
                maclar.append(m)
                
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Veriler okunurken bir hata olustu: {e}")
        
    return takimlar, maclar


def txt_raporu_olustur(takimlar, dosya_adi="rapor.txt"):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write("--- TURNUVA RAPORU ---\n\n")
        
        sirali_takimlar = sorted(takimlar, key=lambda x: x.puan, reverse=True)
        f.write("PUAN DURUMU:\n")
        f.write("Takim Adi | G | B | M | Puan\n")
        f.write("-" * 35 + "\n")
        for t in sirali_takimlar:
            f.write(f"{t.ad:10} | {t.galibiyet} | {t.beraberlik} | {t.maglubiyet} | {t.puan}\n")
            
        f.write("\n===================================\n\n")
        f.write("OYUNCU ISTATISTIKLERI:\n")
        for t in takimlar:
            f.write(f"\n[{t.ad}]\n")
            for o in t.oyuncular:
                f.write(f"- {o.ad} ({o.mevki}) - Gol: {o.gol}, Asist: {o.asist}\n")