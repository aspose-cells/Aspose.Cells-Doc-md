---
title: Excel i JSON a Dönüştür
type: docs
weight: 300
url: /tr/net/convert-excel-to-json/
description: Aspose.Cells ile excel dosyasını JSON a dönüştürmenin nasıl yapılacağını öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan çalışma kitabını json olarak dışa aktarma
---

{{% alert color="primary" %}}

Aspose.Cells, bir Workbook'ü Json (JavaScript Object Notation) dosyasına dönüştürmeyi destekler.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Excel Workbook'ü JSON'a dönüştürmenin nasıl yapılacağını merak etmenize gerek yok, çünkü Apose.Cells for .NET kütüphanesi en iyi kararı sunar. Aspose.Cells API'si, elektronik tabloları JSON formatına dönüştürmeyi destekler. Workbook'ü JSON'a aktarmak için, [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) metodunun ikinci parametresi olarak [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)'i geçirin. Ayrıca, çalışma sayfasını JSON'a aktarmak için ek ayarları belirtmek için [**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, Excel Workbook'ünü Json olarak dışa aktarmanın bir örneğini göstermektedir. Referans için kodu görmek için [kaynak dosyayı](sample.xlsx) kodla üretilen Json dosyası ile birlikte inceleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

Aşağıdaki kod örneği, ek ayarları belirtmek için JsonSaveOptions sınıfını kullanan Excel Workbook'ünü Json olarak dışa aktarmanın bir örneğini göstermektedir. Referans için kodu görmek için [kaynak dosyayı](sample.xlsx) kodla üretilen Json dosyası ile birlikte inceleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}

