---
title: Zaman çizelgesi ekle
linktitle: Zaman çizelgeleri
type: docs
weight: 170
url: /tr/nodejs-cpp/create-timeline/
description: Aspose.Cells for Node.js via C++ ile zaman çizelgesi oluşturmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Tarihleri göstermek için filtreleri ayarlamak yerine, PivotTable Zaman Çizelgesi kullanabilirsiniz — bu, tarih/zaman ile kolayca filtreleme ve kaydırıcı kontrolü ile dönemi yakınlaştırma yapmanıza olanak tanıyan dinamik bir filtre seçeneğidir. Microsoft Excel, bir pivot tablo seçerek sonra *Ekle > Zaman Çizelgesi* tıklayarak zaman çizelgesi oluşturmanıza izin verir. Aspose.Cells for Node.js via C++ ayrıca [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-) yöntemi kullanarak zaman çizelgesi oluşturmanıza da olanak tanır.

## **Bir Pivot Tablosuna Zaman Çizelgesi Oluştur**

Lütfen aşağıdaki örnek kodu inceleyin. Bu, pivot tabloyu içeren [örnek Excel dosyasını](input.xlsx) yükler. Ardından zaman çizelgesini ilk temel pivot alanına göre oluşturur. Son olarak, çalışma kitabını [dışa aktarma XLSX](output.xlsx) formatında kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells for Node.js via C++ tarafından oluşturulan zaman çizelgesini içerir.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

