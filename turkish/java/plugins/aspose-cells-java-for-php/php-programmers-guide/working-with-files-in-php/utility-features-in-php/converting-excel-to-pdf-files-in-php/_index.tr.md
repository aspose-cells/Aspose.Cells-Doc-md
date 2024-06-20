---
title: PHP de Excel Dosyalarını PDF e Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Excel Dosyalarını PDF'e Dönüştürme**
PHP'de Aspose.Cells for Java kullanarak Excel'i PDF dosyasına dönüştürmek için, basitçe Dönüştürücü modülünün excel_to_pdf() metodunu çağırın.

PHP Kodu

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile Excel'den PDF Dosyalarına Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
