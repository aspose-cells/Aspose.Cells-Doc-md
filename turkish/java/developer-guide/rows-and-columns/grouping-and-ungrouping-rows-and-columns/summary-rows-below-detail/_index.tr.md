---
title: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

Bu makale, verilere toplam uygulamanın nasıl yapılacağını ve özet detay altında yönün nasıl değiştirileceğini açıklayacaktır.

Verilere [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal-com.aspose.cells.CellArea-int-int-int[]-) yöntemini kullanarak toplam uygulayabilirsiniz. Aşağıdaki parametreleri alır.

- **CellArea** - Toplam uygulanacak aralık
- **GroupBy** - Sıfıra dayalı bir tamsayı kaydırmak için alan
- **Function** - Toplam işlevi
- **TotalList** - Toplam eklenen sıfıra dayalı alan kaydırmaları dizisi
- **Replace** - Mevcut toplamı değiştirip değiştirmeyeceğini gösterir
- **PageBreaks** - Gruplar arasına sayfa sonu eklemeniz gerekip gerekmediğini gösterir
- **SummaryBelowData** - Verilerin altına özet ekleyip eklemediğini gösterir

Ayrıca, aşağıdaki ekran görüntüsünde gösterildiği gibi, Ayrıntılar altında özet satırlarının yönünü [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) özelliği kullanarak kontrol edebilirsiniz. Bu ayarın Microsoft Excel'de **Veri > Ayrıntı > Ayarlar** yoluyla açabilirsiniz.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Örnek

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, aralık **A2:B11** 'e toplam uygulanmış ve ayrıntıların altındaki özetin yönü.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Detayın altında özet satırlarının toplamını uygulamak ve yönünü değiştirmek için Java kodu

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod burada bulunmaktadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
{{< app/cells/assistant language="java" >}}
