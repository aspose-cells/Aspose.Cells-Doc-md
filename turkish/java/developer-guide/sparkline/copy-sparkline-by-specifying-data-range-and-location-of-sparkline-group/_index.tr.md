---
title: Belirli Veri Aralığını ve Sparkline Grubu Konumunu Belirterek Sparkline Kopyalama
type: docs
weight: 120
url: /tr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

MS Excel'de Sparkline Grubunun Veri Aralığını ve Konumunu Belirleyerek Sparkline Kopyalama

Microsoft Excel, Sparkline'ı kopyalamak için Veri Aralığını ve Sparkline Grubunun Konumunu belirleyerek izin verir. Sparkline'ınızı diğer hücrelere kopyalamak için şu adımları izleyin.

- Sparkline'ı içeren hücreyi seçin.
- **Tasarım** sekmesi içindeki **Sparkline** bölümünden **Düzenle Veri**'yi seçin.
- **Grup Konumunu Düzenle & Veriyi Düzenle...**'yi seçin.
- Veri Aralığını ve Konumu belirleyin ve Tamam'ı tıklayın.

## Örnek

Aspose.Cells, Sparkline Grubunun Veri Aralığını ve Konumunu belirlemek için [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) yöntemini sağlar.

### Kaynak ve çıktı dosyalarının ekran görüntüleri

Aşağıdaki ekran görüntüsü, kod içinde kullanılan kaynak Excel dosyasını göstermektedir. Kırmızı vurgulanmış alan, 'Grup Konumunu Düzenle & Veri...' seçeneğini gösterir ve kıvılcım çizgisi grubunun veri aralığını ve konumunu belirtmek içindir. P4 hücresi, Aspose.Cells kullanarak sarı renkli dört hücreye kopyalanan kıvılcım çizgisini gösterir.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Gördüğünüz gibi, P4 hücresindeki kıvılcım, sırasıyla farklı veri aralıklarına sahip P sütunundaki diğer dört hücreye kopyalanmıştır.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

Kıvılcım grubu veri aralığını ve konumunu belirterek kıvılcım kopyalama için Java kodu

Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ardından ilk kıvılcım grubuna erişir ve kıvılcım grubu içindeki veri aralıklarını ve konumlarını ekler. Son olarak, aynı şekilde ekran görüntüsünde gösterildiği gibi çıktı Excel dosyasını diske yazar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
