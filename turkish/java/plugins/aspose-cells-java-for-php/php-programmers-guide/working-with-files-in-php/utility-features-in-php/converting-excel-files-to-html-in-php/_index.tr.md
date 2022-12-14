---
title: PHP'de Excel Dosyalarını HTML'ye Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - Excel Dosyalarını HTML'ye Dönüştürme**
PHP'de Aspose.Cells for Java kullanarak Excel'i HTML'ye dönüştürmek için çalışma sayfasını çağırmanız yeterlidir_ile_Dönüştürücü modülünün html() yöntemi.

**PHP Kodu**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Excel Dosyalarını HTML'ye Dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
