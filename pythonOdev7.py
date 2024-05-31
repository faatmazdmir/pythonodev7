"""
sozluk={"Kategori":["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
"Ürün":["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
"Fiyat":[300,180,450,50,700,400,150,80,850,900]}

Yukarıdaki sözlük DataFrame’e dönüştürülür.

Yukarıdaki DataFrame için;
2.indexte bulunan kategori bulunur.(Sadece kategori bilgisi)
2.indexte bulunan ürün bulunur.(Sadece ürün bilgisi)
4.indexten 9.indexe kadar olan veriler bulunur.(Kategori,ürün,fiyat bilgisi beraber)
1.indexten 6.indexe kadar olan ürünler bulunur.(Sadece ürün bilgisi)

Yukarıdaki DataFrame için;
Giyim kategorisinde bulunan ürünler gösterilir.
Ayakkabı kategorisinde bulunan ürünler gösterilir.
Aksesuar kategorisinde bulunan ürünler gösterilir.

Yukarıdaki DataFrame için;
Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir.
Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir.
Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir.
"""
import pandas as pd

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
         "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
         "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

df = pd.DataFrame(sozluk)

kategori_2_index = df.loc[2, "Kategori"]
urun_2_index = df.loc[2, "Ürün"]
veriler_4_9_index = df.loc[4:9]
urun_1_6_index = df.loc[1:6, "Ürün"]

giyim = df[df["Kategori"] == "Giyim"]
ayakkabi = df[df["Kategori"] == "Ayakkabı"]
aksesuar = df[df["Kategori"] == "Aksesuar"]

giyim_fiyat = df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)]
ayakkabi_fiyat = df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] < 600)]
aksesuar_fiyat = df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)]

print("2.indexte bulunan kategori:", kategori_2_index)
print("2.indexte bulunan ürün:", urun_2_index)
print("4.indexten 9.indexe kadar olan veriler:\n", veriler_4_9_index)
print("1.indexten 6.indexe kadar olan ürünler:\n", urun_1_6_index)
print("Giyim kategorisinde bulunan ürünler:\n", giyim)
print("Ayakkabı kategorisinde bulunan ürünler:\n", ayakkabi)
print("Aksesuar kategorisinde bulunan ürünler:\n", aksesuar)
print("Giyim kategorisinde fiyatı 300'den fazla olan ürünler:\n", giyim_fiyat)
print("Ayakkabı kategorisinde fiyatı 600'den az olan ürünler:\n", ayakkabi_fiyat)
print("Aksesuar kategorisinde fiyatı 100'den fazla olan ürünler:\n", aksesuar_fiyat)