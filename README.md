
 Renkli Resmi Griye Çevirme ve Hata Analizi
   Bu ödevde `renklifoto.jpg` fotoğrafını iki farklı şekilde griye dönüştürdüm:
  1. OpenCV'nin hazır `cv2.cvtColor` fonksiyonuyla
  2. Standart formülle (`Gri = 0.299*R + 0.587*G + 0.114*B`) kendi yazdığım fonksiyonla
  Düz ortalama almak yerine insan gözünün renklere olan duyarlılığını yansıtan bu formülü kullandım.

Sonuç ve Hata Değerlendirmesi:
*İki yöntem arasındaki mutlak farkı (`absdiff`) aldığımda çıkan ekran tamamen siyah oldu. Çünkü siyah renk 0 demektir; bu da pikseller arasında görünür hiçbir fark olmadığını gösteriyor.
* Terminaldeki toplam hata ve ortalama hata da neredeyse 0 çıktı. Aradaki önemsiz küsurat farkı sadece Python'daki ondalıklı yuvarlama ile OpenCV'nin tamsayı optimizasyonundan kaynaklanıyor.
* Sonuç olarak kendi yazdığım fonksiyon, OpenCV'nin hazır fonksiyonuyla birebir aynı ve doğru şekilde çalıştı.
