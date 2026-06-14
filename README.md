# BUÜ İleri Programlama Dönem Projesi
## Futbol Turnuva ve İstatistik Yönetim Sistemi

Bu proje, Python programlama dili kullanılarak Nesne Yönelimli Programlama (OOP) prensiplerine uygun şekilde geliştirilmiş bir futbol turnuva ve istatistik yönetim sistemidir 

### 🚀 Proje Özellikleri ve Uygulanan Kurallar
* **Modüler Yapı:** Proje; `models.py`, `veri_islemleri.py` ve `main.py` olmak üzere 3 farklı modüle bölünmüştür.
* **Veri Kapsülleme (Encapsulation):** Oyuncu gol ve asist sayıları `@property` ve `.setter` yapısı kullanılarak korunmuş, negatif değer girişleri engellenmiştir.
* **Hata Yönetimi (Try-Except):** Kullanıcı hatalı veri girdiğinde (eksili skor veya harf girişi vb.) sistem `raise ValueError` fırlatarak çökmeleri önler.
* **Sınıf Değişkeni (Class Variable):** Sistemdeki toplam maç kaydı, `Mac` sınıfına ait ortak bir sayaç ile anlık olarak takip edilir.
* **Veri Kalıcılığı (JSON):** Girilen tüm veriler program kapatılırken `veriler.json` dosyasına kaydedilir ve açılışta otomatik yüklenir.
* **Gelişmiş Puan Durumu ve Krallıklar:** Takımların puanları otomatik hesaplanır; sistem en çok gol/asist yapan oyuncuları dinamik olarak sıralar.
* **Rapor Çıktısı (Dosya İşlemleri):** Menü üzerinden turnuvanın genel durumu tek tıkla `rapor.txt` dosyasına yazdırılabilir.

### 📁 Proje Yapısı
* `models.py` -> Sınıf tanımlamaları (Takim, Oyuncu, Mac) ve kapsülleme yapıları.
* `veri_islemleri.py` -> JSON okuma/yazma ve TXT rapor oluşturma fonksiyonları.
* `main.py` -> Ana menü döngüsü ve try-except kontrolleri.
* `akis_semasi.png` -> Sistemin çalışma mantığını gösteren draw.io akış şeması.

### 🛠️ Kurulum ve Çalıştırma
Proje klasöründe terminali açarak aşağıdaki komutla uygulamayı başlatabilirsiniz:
```bash
python main.py
