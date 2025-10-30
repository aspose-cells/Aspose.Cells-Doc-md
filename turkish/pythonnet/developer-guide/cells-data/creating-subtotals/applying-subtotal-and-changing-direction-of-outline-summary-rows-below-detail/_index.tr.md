---
title: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for Python via .NET API kullanarak alt toplamı nasıl uygulayacağınızı ve detayın altında Özet Satırlarını değiştirme yöntemini öğrenin.
keywords: Python Excel Kütüphanesi, Alt toplamı Uygula, Alt toplam ekle, Detayın altındaki Özet Satırlarının yönünü değiştir, Detayın sağında Özet özeti Sutunlarının yönünü değiştir, Alt toplam oluştur ve Detayın altındaki Özet Satırlarının yönünü değiştir
---

{{% alert color="primary" %}}

Bu makale, verilere toplam uygulamanın nasıl yapılacağını ve özet detay altında yönün nasıl değiştirileceğini açıklayacaktır.

Verilere [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool) yöntemini kullanarak toplam uygulayabilirsiniz. Aşağıdaki parametreleri alır.

- **ca** - Alt toplam uygulanacak aralık
- **group_by** - Bir sıfıra dayalı tamsayı ofset olarak gruplandırılacak alan
- **function** - Alt toplama işlevi
- **total_list** - Alt toplamların eklendiği sıfıra dayalı alan ofsetleri dizisi
- **replace** - Mevcut alt toplamların değiştirilip değiştirilmeyeceğini gösterir
- **page_breaks** - Gruplar arasına sayfa sonu eklenip eklenmeyeceğini gösterir
- **summary_below_data** - Verinin altına özet eklenip eklenmeyeceğini gösterir

Ayrıca, Şekil5'te gösterildiği gibi Çalışsayı.Outline.SummaryRowBelow özelliğini kullanarak Özet satırların altındaki detay yönünü kontrol edebilirsiniz. Bu ayarı **Veri > Özet > Ayarlar** kullanarak Microsoft Excel'de açabilirsiniz.

![todo:image_alt_text](1.png)

{{% /alert %}}

## **Kaynak ve çıktı dosyalarının görüntüleri**

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, toplam A2:B11 aralığına uygulanmış ve özetin yönü detayın altında bulunmaktadır.

![todo:image_alt_text](3.png)

## **Alt toplam uygulamak ve özet özet satırlarının yönünü değiştirmek için Python kodu**

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod burada bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
