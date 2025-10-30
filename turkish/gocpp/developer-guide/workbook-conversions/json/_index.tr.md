---
title: Golang kullanarak C++ ile Çalışma Kitabını JSON a dönüştürün.
linktitle: Çalışma Kitabını JSON’a Dönüştürme
type: docs
weight: 300
url: /tr/go-cpp/convert-workbook-to-json/
description: Aspose.Cells for C++ kullanılarak Excel çalışma kitaplarını JSON biçimine nasıl dönüştüreceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabını JSON (JavaScript Nesne Gösterimi) dosyasına dönüştürme desteği sağlar.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Aspose.Cells API, çalışma sayfalarını JSON formatına dönüştürmeye destek sağlar. Çalışma kitabını JSON’a aktarmak için, [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yönteminin ikinci parametresi olarak [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) kullanın. Ayrıca, çalışma sayfasını JSON’a aktarımını özelleştirmek için [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif çalışma sayfasını [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) enum üyelerini kullanarak JSON’a nasıl aktaracağınızı gösterir. Lütfen, [kaynak dosyasını](book1.xlsx) [dönüştürmek için](book1.json) kodu referans olarak inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **Gelişmiş Konular**
- [CSV'yi JSON'a dönüştür](/cells/tr/cpp/convert-csv-to-json/)
- [Excel’i JSON’a dönüştürmek](/cells/tr/cpp/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/cpp/convert-json-to-csv/)
- [JSON’u Excel’e dönüştürmek](/cells/tr/cpp/convert-json-to-excel/)
