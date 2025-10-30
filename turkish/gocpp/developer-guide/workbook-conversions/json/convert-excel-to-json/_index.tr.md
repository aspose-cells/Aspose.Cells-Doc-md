---
title: Excel i JSON a Dönüştür, Golang ve C++ ile
linktitle: Excel den JSON a Dönüştürme
type: docs
weight: 300
url: /tr/go-cpp/convert-excel-to-json/
description: Aspose.Cells kullanarak C++ ile excel dosyasını JSON a dönüştürmeyi öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan çalışma kitabını json olarak dışa aktarma
---

{{% alert color="primary" %}}

Aspose.Cells, bir Workbook'ü Json (JavaScript Object Notation) dosyasına dönüştürmeyi destekler.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Excel İş Kitabı'nı JSON'a dönüştürmek için nasıl yapılacağını merak etmeyin, çünkü Aspose.Cells for C++ kütüphanesi en iyi çözümü sağlar. Aspose.Cells API'si, tabloları JSON formatına dönüştürmek için destek sağlar. İş kitabını JSON'a aktarmak için, [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) önemli parametre olarak [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoduna geçirin. Ayrıca, sayfayı JSON'a dışa aktarırken ek ayarları belirlemek için [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, Excel İş Kitabını JSON'a dışa aktarmayı göstermektedir. Referans için, [kaynak dosyasını](sample.xlsx) JSON çıktı dosyasına dönüştürmek için kodu inceleyebilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
JsonSaveOptions sınıfını kullanarak ek ayarları belirten aşağıdaki kod örneği, Excel İş Kitabını JSON'a dışa aktarmayı gösterir. Referans olarak, [kaynak dosyayı](sample.xlsx) JSON çıktısına dönüştürmek için kodu inceleyebilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
