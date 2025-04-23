---
title: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for .NET API sını kullanarak alt detay altında toplam uygulamayı ve özet satırların yönünü değiştirmeyi öğrenin.
keywords: Alt detay altında toplam uygulama, toplam ekleme, özet detay altında özet satırların yönünü değiştirme, özet detay altında özet sütunlarını sağa değiştirme, toplam oluşturma ve özet detay altında özet satırlarının yönünü değiştirme
---

{{% alert color="primary" %}}

Bu makale, verilere toplam uygulamanın nasıl yapılacağını ve özet detay altında yönün nasıl değiştirileceğini açıklayacaktır.

Verilere [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) yöntemini kullanarak toplam uygulayabilirsiniz. Aşağıdaki parametreleri alır.

- **CellArea** - Toplam uygulanacak aralık
- **GroupBy** - Sıfıra dayalı bir tamsayı kaydırmak için alan
- **Function** - Toplam işlevi
- **TotalList** - Toplam eklenen sıfıra dayalı alan kaydırmaları dizisi
- **Replace** - Mevcut toplamı değiştirip değiştirmeyeceğini gösterir
- **PageBreaks** - Gruplar arasına sayfa sonu ekleyip eklemediğini gösterir
- **SummaryBelowData** - Verilerin altına özet ekleyip eklemediğini gösterir

Ayrıca, Şekil5'te gösterildiği gibi Çalışsayı.Outline.SummaryRowBelow özelliğini kullanarak Özet satırların altındaki detay yönünü kontrol edebilirsiniz. Bu ayarı **Veri > Özet > Ayarlar** kullanarak Microsoft Excel'de açabilirsiniz.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, toplam A2:B11 aralığına uygulanmış ve özetin yönü detayın altında bulunmaktadır.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Toplam uygulama ve özet detay satır yönünün değiştirilmesi için C# kodu

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod burada bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
