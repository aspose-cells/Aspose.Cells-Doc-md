---
title: Tarih Ekseni
description: Aspose.Cells for Java numaralı telefondan tarih eksenini nasıl yöneteceğinizi öğrenin. Kılavuzumuz çeşitli tarih formatları, zaman ölçekleri ve onay etiketi frekanslarıyla nasıl çalışacağınızı anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /tr/java/date-axis/
---
##  **Olası Kullanım Senaryoları**
Tarihleri kullanan çalışma sayfası verilerinden bir grafik oluşturduğunuzda ve tarihler grafikteki yatay (kategori) eksen boyunca çizildiğinde, Aspose.cells kategori eksenini otomatik olarak tarih (zaman ölçeği) eksenine dönüştürür.
Tarih ekseni, çalışma sayfasındaki tarihler sıralı sırada veya aynı temel birimlerde olmasa bile, tarihleri belirli aralıklarla veya gün, ay veya yıl sayısı gibi temel birimlerde kronolojik sırada görüntüler.
Varsayılan olarak Aspose.cells, çalışma sayfası verilerindeki herhangi iki tarih arasındaki en küçük farka göre tarih ekseninin temel birimlerini belirler. Örneğin, tarihler arasındaki en küçük farkın yedi gün olduğu hisse senedi fiyatları verileriniz varsa, Excel temel birimi gün olarak ayarlar ancak hisse senedinin performansını görmek istiyorsanız temel birimi aylar veya yıllar olarak değiştirebilirsiniz. daha uzun bir süre.
##  **Tarih Eksenini Microsoft Excel gibi kullanın**
 Lütfen yeni bir Excel dosyası oluşturan ve grafiğin değerlerini ilk çalışma sayfasına koyan aşağıdaki örnek koda bakın.
 Daha sonra bir grafik ekliyoruz ve türü belirliyoruz.[**Eksen**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
 ile[**Zaman Ölçeği**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) ve ardından temel birimleri Gün olarak ayarlayın.

![yapılacak şey:image_alt_text](excel.png)

 Aşağıdaki örnek kod şunu oluşturur:[Excel dosyasının çıktısı](DateAxis.xlsx).

##  **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
