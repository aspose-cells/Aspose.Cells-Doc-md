---
title: PHP'de Excel'i PDF Dosyalarına Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - Excel'i PDF Dosyalarına Dönüştürme**
PHP'de Aspose.Cells for Java kullanarak Excel'i PDF dosyasına dönüştürmek için excel'i çağırmanız yeterlidir_ile_Dönüştürücü modülünün pdf() yöntemi.

**PHP Kodu**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Excel'i PDF Dosyalarına Dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
