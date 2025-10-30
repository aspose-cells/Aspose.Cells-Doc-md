---
title: Golang ve C++ kullanarak Toplam Satırlarını Uygulama ve Detayların Altındaki Yön Değiştirme
linktitle: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for C++ API kullanarak, detayın altında kontur özet satırlarının yönünü değiştirme ve toplam uygulama yollarını öğrenin.
keywords: Alt detay altında toplam uygulama, toplam ekleme, özet detay altında özet satırların yönünü değiştirme, özet detay altında özet sütunlarını sağa değiştirme, toplam oluşturma ve özet detay altında özet satırlarının yönünü değiştirme
---

{{% alert color="primary" %}}

 Bu makale, veriye toplam uygulama ve detayın altındaki Kontur Özet Satırlarının yönünü değiştirmeyi açıklayacaktır.

 Verilere toplam uygulamak için [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/) yöntemini kullanabilirsiniz. Aşağıdaki parametreleri alır:

- **CellArea** - Toplam uygulanacak aralık
- **GroupBy** - Sıfıra dayalı bir tamsayı kaydırmak için alan
- **Function** - Toplam işlevi
- **TotalList** - Toplam eklenen sıfıra dayalı alan kaydırmaları dizisi
- **Replace** - Mevcut toplamların değiştirilip değiştirilmayacağını belirtir
- **PageBreaks** - Gruplar arasında sayfa sonu eklenip eklenmeyeceğini belirtir
- **SummaryBelowData** - Özette özetin veri altında eklenip eklenmeyeceğini belirtir.

Ayrıca, aşağıdaki ekran görüntüsünde gösterildiği gibi `Worksheet.Outline.SummaryRowBelow` özelliği kullanılarak Detayların altında özet satırlarının yönü kontrol edilebilir. Bu ayarı Microsoft Excel'de **Veri > Kontur > Ayarlar** kullanarak açabilirsiniz.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, toplam A2:B11 aralığına uygulanmış ve özetin yönü detayın altında bulunmaktadır.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Toplam uygulama ve kontur özet satırlarının yönünü değiştirmek için C++ kodu

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod burada bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
