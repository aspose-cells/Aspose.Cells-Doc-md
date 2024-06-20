---
title: Tarih Ekseni
description: Aspose.Cells for Java da tarih ekseni nasıl yöneteceğinizi öğrenin. Rehberimiz, çeşitli tarih formatları, zaman aralıkları ve işaret etiketi frekansları ile nasıl çalışılacağını anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for Java, tarih ekseni, yönet, tarih formatları, zaman aralıkları, işaret etiketi frekansları.
type: docs
weight: 200
url: /tr/java/date-axis/
---

## **Olası Kullanım Senaryoları**
Tarih kullanılan çalışma sayfası verilerinden bir grafik oluşturduğunuzda ve tarihler grafikte yatay (kategori) eksende çizilmişse, Aspose.Cells otomatik olarak kategori ekseni tarih (zaman ölçeği) ekseni olarak değiştirir.
Tarih ekseni, çalışma sayfasındaki tarihleri belirli aralıklarda veya temel birimlerde, örneğin gün, ay veya yıl sayısını kronolojik sırada görüntüler, hatta çalışma sayfasındaki tarihler sıralı veya aynı temel birimlerde değilse bile.
Varsayılan olarak, Aspose.Cells, çalışma sayfasındaki herhangi iki tarih arasındaki en küçük farka dayanarak tarih ekseni için temel birimleri belirler. Örneğin, çalışma sayfasında tarih farkı en küçük olan yedi gün ise, Excel temel birimi gün olarak ayarlar, ancak stok performansını daha uzun bir süre boyunca görmek istiyorsanız, temel birimi aylar veya yıllara değiştirebilirsiniz.
## **Microsoft Excel gibi Tarih Ekseni Yönetimi**
Yeni bir Excel dosyası oluşturan ve grafik değerlerini ilk çalışma sayfasına koyan aşağıdaki örnek kodu inceleyin. 
Ardından bir grafik ekleriz ve [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) tipini ayarlarız 
[**TimeScale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) 'e ayarlar dikkate alınarak, base units için Days olarak ayarlarız.

![todo:image_alt_text](excel.png)

Aşağıdaki örnek kod, [çıktı Excel dosyasını](DateAxis.xlsx) oluşturur.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
