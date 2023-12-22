---
title: Alt Toplamın Uygulanması ve Detayın Altındaki Anahat Özeti Satırlarının Yönünün Değiştirilmesi
type: docs
weight: 100
url: /tr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for .NET API'i kullanarak alt toplamı nasıl uygulayacağınızı ve Ayrıntı Altındaki Anahat Özet Satırlarının yönünü nasıl değiştireceğinizi öğrenin.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

Bu makalede, Alt Toplamın verilere nasıl uygulanacağı ve Ayrıntı altındaki Anahat Özet Satırlarının yönünün nasıl değiştirileceği açıklanacaktır.

 Aşağıdakileri kullanarak verilere Alt Toplam uygulayabilirsiniz:[**Çalışma Sayfası.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) yöntem. Aşağıdaki parametreleri alır.

- **Hücre Alanı** - Ara toplamın uygulanacağı aralık
- **Gruplandırmaya Göre** - Sıfır tabanlı tamsayı uzaklığı olarak gruplandırılacak alan
- **İşlev** - Alt toplam işlevi.
- **Toplam Liste** Alt toplamların eklendiği alanları gösteren sıfır tabanlı alan uzaklıkları dizisi.
- **Yer değiştirmek** - Geçerli alt toplamların değiştirilip değiştirilmeyeceğini gösterir
- **Sayfa Sonları** - Gruplar arasında sayfa sonu eklenip eklenmeyeceğini belirtir
- **ÖzetAşağıdakiVeriler** - Verilerin altına özet eklenip eklenmeyeceğini belirtir.

 Ayrıca Anahat'ın yönünü de kontrol edebilirsiniz.**Ayrıntıların altındaki özet satırları** Worksheet.Outline.SummaryRowBelow özelliğini kullanarak aşağıdaki ekran görüntüsünde gösterildiği gibi. Bu ayarı Microsoft Excel'de kullanarak açabilirsiniz.**Veri > Anahat > Ayarlar**

![yapılacak şey:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, A ve B sütunlarındaki bazı verileri içeren, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını göstermektedir.

![yapılacak şey:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü örnek kod tarafından oluşturulan çıktı Excel dosyasını gösterir. Gördüğünüz gibi A2:B11 aralığına ara toplam uygulandı ve ana hatların yönü detayın altındaki özet satırlarıdır.

![yapılacak şey:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Alt toplamı uygulamak ve anahat özeti satırlarının yönünü değiştirmek için C# kodu

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod aşağıdadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
