import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Veri Yükleme
veri = pd.read_excel("C:/Users/murat/Desktop/Arçelik.xlsx")

# 2. Veri Ön İşleme
print("Eksik Değerler:\n", veri.isnull().sum())
print("\nVeri Tipleri:\n", veri.dtypes)

# 3. Bağımlı ve Bağımsız Değişkenler
bagimli_degisken = 'Net Kâr'
bagimsiz_degiskenler = ['Net Satışlar', 'Brüt Kâr', 'Faaliyet Kârı', 'Toplam Varlık', 'Özsermaye', 'Kısa V. Borç', 'Uzun V. Borç']
X = veri[bagimsiz_degiskenler]
y = veri[bagimli_degisken]

# 4. Eğitim ve Test Ayrımı
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Eğitimi
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Tahmin
y_pred = model.predict(X_test)

# 7. Model Performansı
r_kare = r2_score(y_test, y_pred)
print(f'\nR-kare (Belirleme Katsayısı): {r_kare:.2f}')
print('\nKatsayılar:')
for i, katsayi in enumerate(model.coef_):
    print(f'{bagimsiz_degiskenler[i]}: {katsayi:.2f}')
print(f'Sabit (Intercept): {model.intercept_:.2f}')

# 8. Tahmin Grafiği
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot(y_test, y_test, color='red', linewidth=2)
plt.xlabel('Gerçek Net Kâr')
plt.ylabel('Tahmin Edilen Net Kâr')
plt.title('Gerçek vs Tahmin Net Kâr')
plt.grid(True)
plt.tight_layout()
plt.savefig('grafikler/tahmin_vs_gercek.png')
plt.show()

# 9. Korelasyon Matrisi
korelasyon_matrisi = veri[bagimsiz_degiskenler + [bagimli_degisken]].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(korelasyon_matrisi, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korelasyon Matrisi')
plt.xticks(fontsize=8)
plt.yticks(fontsize=7, rotation=0)
plt.tight_layout()
plt.savefig('grafikler/korelasyon_matrisi.png')
plt.show()

# 10. Oran Analizi Hesaplama
veri['Toplam Borç'] = veri['Kısa V. Borç'] + veri['Uzun V. Borç']
veri['Brüt Kâr Marjı'] = veri['Brüt Kâr'] / veri['Net Satışlar']
veri['Net Kâr Marjı'] = veri['Net Kâr'] / veri['Net Satışlar']
veri['Aktif Devir Hızı'] = veri['Net Satışlar'] / veri['Toplam Varlık']
veri['Özsermaye Kârlılığı'] = veri['Net Kâr'] / veri['Özsermaye']
veri['Cari Oran'] = veri['Toplam Varlık'] / veri['Kısa V. Borç']
veri['Borç/Özsermaye Oranı'] = veri['Toplam Borç'] / veri['Özsermaye']

# 11. Oran Analizi Yazdırma
print("\nOran Analizi Sonuçları:\n")
for yil in veri['Yıl']:
    print(f"{yil} Yılı Oranları:")
    print(f"  Brüt Kâr Marjı: {veri[veri['Yıl'] == yil]['Brüt Kâr Marjı'].values[0]:.2f}")
    print(f"  Net Kâr Marjı: {veri[veri['Yıl'] == yil]['Net Kâr Marjı'].values[0]:.2f}")
    print(f"  Aktif Devir Hızı: {veri[veri['Yıl'] == yil]['Aktif Devir Hızı'].values[0]:.2f}")
    print(f"  Özsermaye Kârlılığı: {veri[veri['Yıl'] == yil]['Özsermaye Kârlılığı'].values[0]:.2f}")
    print(f"  Cari Oran: {veri[veri['Yıl'] == yil]['Cari Oran'].values[0]:.2f}")
    print(f"  Borç/Özsermaye Oranı: {veri[veri['Yıl'] == yil]['Borç/Özsermaye Oranı'].values[0]:.2f}")
    print("-" * 30)

# 12. Oranların Zaman Grafiği
plt.figure(figsize=(12, 8))
oranlar = ["Brüt Kâr Marjı", "Net Kâr Marjı", "Aktif Devir Hızı", "Özsermaye Kârlılığı", "Cari Oran", "Borç/Özsermaye Oranı"]
for oran in oranlar:
    plt.plot(veri["Yıl"], veri[oran], marker="o", label=oran)

plt.title("Finansal Oranların Yıllara Göre Değişimi", fontsize=14)
plt.xlabel("Yıl", fontsize=12)
plt.ylabel("Oran Değeri", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafikler/oran_degisimi.png")
plt.show()
