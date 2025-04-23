---
title: Zaman çizelgesi ekle
linktitle: Zaman çizelgeleri
type: docs
weight: 170
url: /tr/java/create-timeline/
description: Java için Aspose.Cells ile zaman çizelgesi oluşturmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Tarihleri göstermek için filtreleri ayarlamak yerine, dinamik bir filtre seçeneği olan PivotTable Timeline'ı kullanabilirsiniz - bu seçenekle tarih/saat bazında kolayca filtreleme yapabilir ve kaydırmalı denetimi kullanarak istediğiniz döneme yakınlaşabilirsiniz. Microsoft Excel, bir pivot tablosunu seçerek ve ardından *Ekle > Zaman Çizelgesi*'ne tıklayarak zaman çizelgesi oluşturmanıza olanak tanır. Aspose.Cells Java'da da **Worksheet.getTimelines.add()** yöntemini kullanarak zaman çizelgesi oluşturmanıza olanak tanır.

## **Bir Pivot Tablosuna Zaman Çizelgesi Oluştur**

Aşağıdaki örnek kodu inceleyin. İçinde Pivot tablosu bulunan [örnek Excel dosyasını](input.xlsx) yükler. Ardından, ilk temel Pivot alanına dayalı olarak zaman çizelgesi oluşturur. Son olarak, çalışma kitabını [çıktı XLSX](output.xlsx) biçiminde kaydeder. Aşağıdaki ekran resmi, Aspose.Cells tarafından oluşturulan zaman çizelgesini çıktı Excel dosyasında göstermektedir.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

{{< app/cells/assistant language="java" >}}
