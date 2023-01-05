---
title: Ayrıntı altındaki Anahat Özeti Satırlarının Ara Toplamını Uygulama ve Yönünü Değiştirme
type: docs
weight: 100
url: /tr/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Bu makale, ara toplamın verilere nasıl uygulanacağını ve Ayrıntı altındaki Anahat Özeti Satırlarının yönünün nasıl değiştirileceğini açıklayacaktır.

 Alt Toplam'ı kullanarak verilere uygulayabilirsiniz.[**Çalışma sayfası.Cells.alt toplam()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) yöntem. Aşağıdaki parametreleri alır.

- **hücre alanı** Ara toplamın uygulanacağı aralık
- **Gruplandıran** - Sıfır tabanlı bir tamsayı ofseti olarak gruplandırılacak alan
- **İşlev** - Alt toplam işlevi.
- **Toplam Liste** - Ara toplamların eklendiği alanları gösteren sıfır tabanlı alan ofsetleri dizisi.
- **Yer değiştirmek** - Geçerli ara toplamların değiştirilip değiştirilmediğini gösterir
- **Sayfa Sonları** - Gruplar arasına sayfa sonu eklenip eklenmeyeceğini belirtir
- **ÖzetVeri Altında** - Verilerin altına özet eklenip eklenmeyeceğini belirtir.

 Ayrıca, Anahat yönünü de kontrol edebilirsiniz.**Detayın altındaki özet satırları** kullanarak aşağıdaki ekran görüntüsünde gösterildiği gibi[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) Emlak. Bu ayarı kullanarak Microsoft Excel'de açabilirsiniz.**Veri > Anahat > Ayarlar**

![yapılacaklar:resim_alternatif_metin](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Örnek vermek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan ve A ve B sütunlarında bazı veriler içeren kaynak Excel dosyasını göstermektedir.

![yapılacaklar:resim_alternatif_metin](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını gösterir. Gördüğünüz gibi ara toplam aralığa uygulandı**A2:B11** ve taslağın yönü detayın altındaki özet satırlarıdır.

![yapılacaklar:resim_alternatif_metin](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java kodu, alt toplamı uygulamak ve detayın altındaki anahat özet satırlarının yönünü değiştirmek için

Yukarıda gösterilen çıktıyı elde etmek için örnek kod aşağıdadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
