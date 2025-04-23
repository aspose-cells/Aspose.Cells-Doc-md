---
title: Json
type: docs
weight: 300
url: /tr/net/convert-workbook-to-json/
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabını Json (JavaScript Object Notation) dosyasına dönüştürmeyi destekler.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Aspose.Cells API'si, elektronik tabloları JSON biçimine dönüştürmeyi destekler. Elektronik tabloyu JSON'a ihraç etmek için [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) adını ikinci parametre olarak [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) yöntemine geçirin. Ayrıca, JSON olarak dışa aktarma işlemi için ek ayarlar belirtmek için [**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, etkin çalışma sayfasını [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) numaralı üye kullanarak Json'a dönüştürme işlemini göstermektedir. Dönüşüm işlemine ilişkin referans için [kaynak dosyasını](book1.xlsx) ve kodla üretilen [çıktı Json dosyasını](book1.Json) görmek için lütfen kodu inceleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Gelişmiş Konular**
- [CSV'yi JSON'a dönüştür](/cells/tr/net/convert-csv-to-json/)
- [Excel'i JSON'a dönüştür](/cells/tr/net/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/net/convert-json-to-csv/)
- [JSON'ı Excel'e dönüştür](/cells/tr/net/convert-json-to-excel/)
{{< app/cells/assistant language="csharp" >}}
