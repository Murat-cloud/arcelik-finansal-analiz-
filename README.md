# Arçelik Finansal Veri Analizi ve Tahmin Modeli

Bu projede Arçelik firmasına ait yıllık finansal veriler kullanılarak çeşitli finansal oran analizleri yapılmış ve gelecekteki net dönem kârı tahmin edilmiştir.

## 🔍 Proje Özeti

- **Veri Kaynağı:** Arçelik'in yıllık bilanço verileri (Excel dosyası)
- **Amaç:** Finansal oranlar üzerinden regresyon modeliyle net dönem kârını tahmin etmek
- **Kullanılan Araçlar:** Python (pandas, matplotlib, seaborn, scikit-learn)

## 📊 Yapılan İşlemler

1. Veriler yüklendi ve gerekli ön işlemler yapıldı.
2. Finansal oranlar hesaplandı (Likidite, Karlılık, Borçluluk oranları vb.)
3. Korelasyon matrisi oluşturuldu.
4. Regresyon modeli kurularak geçmiş verilerle tahmin denemesi yapıldı.
5. Modelin başarımı değerlendirildi ve grafiklerle görselleştirildi.

## 📁 Dosya İçeriği

- `arcelik_analiz.py` → Python kod dosyası
- `Arçelik.xlsx` → Finansal verilerin bulunduğu Excel dosyası
- `grafikler/` → Oluşturulan grafik dosyaları (korelasyon, tahmin grafiği)
- `README.md` → Bu açıklamaları içeren dosya

## 🖼️ Örnek Grafikler

![Tahmin Grafiği](grafikler/tahmin_vs_gercek.png)

## 🤝 Katkı

Bu proje bireysel öğrenme amacıyla geliştirilmiştir. Pull request'lerle katkı sağlamak isteyenlere açıktır.

## ⚠️ Lisans ve Kullanım

Bu proje **eğitim ve portföy amacıyla** paylaşılmıştır.  

Kodların ya da verilerin ticari amaçlarla veya kaynak göstermeden kullanılması **yasaktır**.  

Daha fazla bilgi için `LICENSE` dosyasını inceleyiniz.
