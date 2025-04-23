---
title: Zaman çizelgesi ekle
linktitle: Zaman çizelgeleri
type: docs
weight: 170
url: /tr/net/create-timeline/
description: Aspose.Cells ile zaman çizelgesi nasıl oluşturulur öğrenin.
---

## **Olası Kullanım Senaryoları**

Tarihleri göstermek için filtreleri ayarlamak yerine, bir PivotTable Zaman çizelgesi kullanabilirsiniz - kolayca tarih/saatlere göre filtrelemeyi sağlayan dinamik bir filtre seçeneği ve kaydırmalı bir kontrolle istediğiniz döneme yaklaşın. Microsoft Excel, bir Pivot tablosunu seçerek ve sonra *Ekle > Zaman Çizelgesi*’ne tıklayarak zaman çizelgesi oluşturmanıza olanak tanır. Aspose.Cells, aynı zamanda [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index) yöntemini kullanarak zaman çizelgesi oluşturmanıza olanak tanır.

## **Bir Pivot Tablosuna Zaman Çizelgesi Oluştur**

Aşağıdaki örnek kodu inceleyin. İçinde Pivot tablosu bulunan [örnek Excel dosyasını](input.xlsx) yükler. Ardından, ilk temel Pivot alanına dayalı olarak zaman çizelgesi oluşturur. Son olarak, çalışma kitabını [çıktı XLSX](output.xlsx) biçiminde kaydeder. Aşağıdaki ekran resmi, Aspose.Cells tarafından oluşturulan zaman çizelgesini çıktı Excel dosyasında göstermektedir.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

{{< app/cells/assistant language="csharp" >}}
