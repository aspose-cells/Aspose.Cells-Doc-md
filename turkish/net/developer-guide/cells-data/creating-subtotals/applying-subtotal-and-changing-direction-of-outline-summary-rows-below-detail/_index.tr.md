---
title: Ayrıntı altındaki Anahat Özeti Satırlarının Ara Toplamını Uygulama ve Yönünü Değiştirme
type: docs
weight: 100
url: /tr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Bu makale, ara toplamın verilere nasıl uygulanacağını ve Ayrıntı altındaki Anahat Özeti Satırlarının yönünün nasıl değiştirileceğini açıklayacaktır.

 Alt Toplam'ı kullanarak verilere uygulayabilirsiniz.[**Worksheet.Cells.Ara toplam()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) yöntem. Aşağıdaki parametreleri alır.

- **hücre alanı** - Ara toplamın uygulanacağı aralık
- **Gruplandıran** - Sıfır tabanlı bir tamsayı ofseti olarak gruplandırılacak alan
- **İşlev** - Alt toplam işlevi.
- **Toplam Liste** - Ara toplamların eklendiği alanları gösteren sıfır tabanlı alan ofsetleri dizisi.
- **Yer değiştirmek** - Geçerli ara toplamların değiştirilip değiştirilmediğini gösterir
- **Sayfa Sonları** - Gruplar arasında sayfa sonu eklenip eklenmeyeceğini gösterir
- **ÖzetVeri Altında** - Verilerin altına özet eklenip eklenmeyeceğini belirtir.

 Ayrıca, Anahat yönünü de kontrol edebilirsiniz.**Detayın altındaki özet satırları** Worksheet.Outline.SummaryRowBelow özelliği kullanılarak aşağıdaki ekran görüntüsünde gösterildiği gibi. Bu ayarı kullanarak Microsoft Excel'de açabilirsiniz.**Veri > Anahat > Ayarlar**

![yapılacaklar:resim_alternatif_Metin](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan ve A ve B sütunlarında bazı veriler içeren kaynak Excel dosyasını göstermektedir.

![yapılacaklar:resim_alternatif_Metin](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını gösterir. Görüldüğü gibi A2:B11 aralığına ara toplam uygulanmış ve ana hatların yönü detayın altında özet satırları şeklindedir.

![yapılacaklar:resim_alternatif_Metin](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# ara toplamı uygulamak ve ana hat özet satırlarının yönünü değiştirmek için kod

Yukarıda gösterilen çıktıyı elde etmek için örnek kod aşağıdadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
