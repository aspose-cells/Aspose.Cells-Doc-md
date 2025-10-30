---
title: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/nodejs-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Subtotal uygulamayı ve detay altındaki Satırların yönerge özetinin yönünü değiştirmeyi Aspose.Cells for Node.js via C++ API kullanarak öğrenin.
keywords: Alt detay altında toplam uygulama, toplam ekleme, özet detay altında özet satırların yönünü değiştirme, özet detay altında özet sütunlarını sağa değiştirme, toplam oluşturma ve özet detay altında özet satırlarının yönünü değiştirme
---

{{% alert color="primary" %}}

Bu makale, verilere toplam uygulamanın nasıl yapılacağını ve özet detay altında yönün nasıl değiştirileceğini açıklayacaktır.

Verilere [**Worksheet.getCells().subtotal()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-) yöntemini kullanarak toplam uygulayabilirsiniz. Aşağıdaki parametreleri alır.

- **CellArea** - Toplam uygulanacak aralık
- **GroupBy** - Sıfıra dayalı bir tamsayı kaydırmak için alan
- **Function** - Toplam işlevi
- **TotalList** - Toplam eklenen sıfıra dayalı alan kaydırmaları dizisi
- **Replace** - Mevcut toplamı değiştirip değiştirmeyeceğini gösterir
- **PageBreaks** - Gruplar arasına sayfa sonu ekleyip eklemediğini gösterir
- **SummaryBelowData** - Verilerin altına özet ekleyip eklemediğini gösterir

Ayrıca, Şekil5'te gösterildiği gibi Çalışsayı.Outline.SummaryRowBelow özelliğini kullanarak Özet satırların altındaki detay yönünü kontrol edebilirsiniz. Bu ayarı **Veri > Özet > Ayarlar** kullanarak Microsoft Excel'de açabilirsiniz.

![todo:image_alt_text](1.png)

{{% /alert %}}

## Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, toplam A2:B11 aralığına uygulanmış ve özetin yönü detayın altında bulunmaktadır.

![todo:image_alt_text](3.png)

## Node.js ile subtotal uygulama ve özet satırlarının yönünü değiştirme

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod burada bulunmaktadır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
