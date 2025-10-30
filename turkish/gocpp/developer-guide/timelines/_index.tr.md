---
title: Zaman Çizelgesi Ekleme Golang kullanarak C++ ile
linktitle: Zaman çizelgeleri
type: docs
weight: 170
url: /tr/go-cpp/create-timeline/
description: Aspose.Cells kullanarak C++ ile bir zaman çizelgesi nasıl oluşturulur öğrenin.
---

## **Olası Kullanım Senaryoları**

Tarihleri göstermek için filtreleri ayarlamak yerine, PivotTable Zaman Çizelgesi — tarih/zaman ile kolayca filtre yapmanızı ve kaydırıcı kontrolü ile istediğiniz döneme yakınlaşmanızı sağlayan dinamik filtre seçeneğini kullanabilirsiniz. Microsoft Excel, bir pivot tabloyu seçip ardından *Ekle > Zaman Çizelgesi* tıklayarak bir zaman çizelgesi oluşturmanıza izin verir. Aspose.Cells ayrıca [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/) yöntemi kullanılarak zaman çizelgesi oluşturmanıza da olanak tanır.

## **Bir Pivot Tablosuna Zaman Çizelgesi Oluştur**

Aşağıdaki örnek kodu inceleyin. İçinde Pivot tablosu bulunan [örnek Excel dosyasını](input.xlsx) yükler. Ardından, ilk temel Pivot alanına dayalı olarak zaman çizelgesi oluşturur. Son olarak, çalışma kitabını [çıktı XLSX](output.xlsx) biçiminde kaydeder. Aşağıdaki ekran resmi, Aspose.Cells tarafından oluşturulan zaman çizelgesini çıktı Excel dosyasında göstermektedir.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
