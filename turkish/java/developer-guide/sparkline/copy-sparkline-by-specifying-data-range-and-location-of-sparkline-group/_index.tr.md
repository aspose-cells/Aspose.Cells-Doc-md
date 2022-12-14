---
title: Mini Grafik Grubunun Veri Aralığını ve Konumunu Belirterek Mini Tabloyu Kopyalayın
type: docs
weight: 120
url: /tr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
MS Excel'de Sparkline Grubunun Veri Aralığını ve Konumunu Belirterek Mini Tabloyu Kopyalayın

Microsoft Excel, Mini Grafik Grubunun Veri Aralığı ve Konumunu belirterek bir Mini Grafik kopyalamanıza olanak tanır. Sparkline'ınızı diğer hücrelere kopyalamak için bu adımları izleyin.

- Sparkline'ınızı içeren hücreyi seçin.
-  Seçme**Verileri Düzenle** dan**küçük resim** içindeki bölüm**Tasarım** sekme
-  Seçmek**Grup Konumunu ve Verilerini Düzenle...**
- Veri Aralığı ve Konumunu belirtin ve Tamam'a tıklayın.

## Örnek

 Aspose.Cells şunları sağlar:[**SparklineCollection.add(dataRange, satır, sütun)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) Mini Grafik Grubunun Veri Aralığını ve Konumunu belirtme yöntemi.

### Kaynak ve çıktı dosyalarının ekran görüntüleri

Aşağıdaki ekran görüntüsü, kodun içinde kullanılan kaynak Excel dosyasını göstermektedir. Kırmızıyla vurgulanan alan "**Grup Konumunu ve Verilerini Düzenle...**Mini grafik grubunun veri aralığını ve konumunu belirtmek için " seçeneği. P4 hücresi, Aspose.Cells kullanılarak sarı renkle doldurulmuş diğer dört hücreye kopyalanacak mini grafiği gösterir.

![yapılacaklar:resim_alternatif_Metin](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını gösterir. Gördüğünüz gibi, P4 hücresindeki mini grafik, her biri farklı veri aralığına sahip P sütunundaki sonraki dört hücreye kopyalanmıştır.

![yapılacaklar:resim_alternatif_Metin](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Mini grafik grubunun veri aralığını ve konumunu belirterek mini grafiği kopyalamak için Java kodu

Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ardından ilk mini grafik grubuna erişir ve mini grafik grubu içindeki veri aralıklarını ve konumları ekler. Son olarak, yukarıdaki ekran görüntüsünde de gösterilen çıktı Excel dosyasını diske yazar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
