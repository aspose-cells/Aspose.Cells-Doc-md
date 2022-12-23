---
title: Tarih Ekseni
type: docs
weight: 200
url: /tr/net/date-axis/
---
## **Olası Kullanım Senaryoları**
Tarihleri kullanan çalışma sayfası verilerinden bir grafik oluşturduğunuzda ve tarihler grafikte yatay (kategori) eksen boyunca çizildiğinde, Aspose.cells kategori eksenini otomatik olarak bir tarih (zaman ölçeği) eksenine değiştirir.
Tarih ekseni, çalışma sayfasındaki tarihler sıralı sırada veya aynı temel birimlerde olmasa bile, tarihleri belirli aralıklarla veya gün, ay veya yıl sayısı gibi temel birimlerde kronolojik sırada görüntüler.
Varsayılan olarak Aspose.cells, çalışma sayfası verilerindeki herhangi iki tarih arasındaki en küçük farkı temel alarak tarih ekseni için temel birimleri belirler. Örneğin, tarihler arasındaki en küçük farkın yedi gün olduğu hisse senedi fiyatları verileriniz varsa, Excel temel birimi gün olarak ayarlar, ancak stoğun performansını görmek istiyorsanız temel birimi ay veya yıl olarak değiştirebilirsiniz. daha uzun bir süre.
## **Tarih Eksenini Microsoft Excel gibi kullanın**
 Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına koyan aşağıdaki örnek koda bakın.
 Sonra bir grafik ekliyoruz ve türünü ayarlıyoruz.[**eksen**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 ile[**Zaman Ölçeği**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) ve ardından temel birimleri Gün olarak ayarlayın.

![yapılacaklar:resim_alternatif_metin](excel.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
