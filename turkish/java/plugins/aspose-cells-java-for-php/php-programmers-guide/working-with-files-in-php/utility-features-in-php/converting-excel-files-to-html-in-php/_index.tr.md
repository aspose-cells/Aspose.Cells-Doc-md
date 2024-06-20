---
title: PHP de Excel Dosyalarını HTML e Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Excel Dosyalarını HTML'e Dönüştürme**
PHP'de Aspose.Cells for Java kullanarak Excel'i HTML'e dönüştürmek için, basitçe Dönüştürücü modülünün worksheet_to_html() metodunu çağırın.

PHP Kodu

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile Excel Dosyalarını HTML'e Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
