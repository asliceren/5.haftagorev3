* Bu ödevde `renklifoto.jpg` görüntüsünü hem OpenCV'nin hazır `cv2.cvtColor` fonksiyonuyla hem de standart formülle kendi yazdığım fonksiyonla gri seviyeye dönüştürdüm.
* Düz aritmetik ortalama yerine insan gözünün renklere olan duyarlılığını doğru yansıtan `Gri = 0.299*R + 0.587*G + 0.114*B` ağırlıklı toplam formülünü kullandım.
* İki yöntem arasındaki mutlak fark görüntüsünü aldığımda ekran tamamen siyah çıktı; görüntü işlemede siyah renk 0 demek olduğu için pikseller arasında görünür hiçbir fark oluşmadı.
* Terminale yazdırdığım toplam mutlak hata ve piksel başına düşen ortalama hata değerleri neredeyse 0 çıktı.
* Aradaki önemsiz küsurat farkı sadece Python'daki ondalıklı sayı yuvarlaması ile OpenCV'nin tamsayı optimizasyonu arasındaki donanımsal farktan kaynaklandı.
* Elde edilen sonuçlar, kendi yazdığım manuel dönüşüm fonksiyonunun OpenCV ile birebir aynı ve doğru çalıştığını gösterdi.
