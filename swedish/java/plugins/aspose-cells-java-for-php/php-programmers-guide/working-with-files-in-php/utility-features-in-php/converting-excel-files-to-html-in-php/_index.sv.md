---
title: Konvertera Excel filer till HTML i PHP
type: docs
weight: 20
url: /sv/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Konvertera Excel-filer till HTML**
För att konvertera Excel till HTML med Aspose.Cells for Java i PHP, helt enkelt anropa worksheet_to_html()-metoden i Converter-modulen.

**PHP-kod**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Konvertera Excel-filer till HTML (Aspose.Cells)** från någon av de sociala kodningssidorna som nämns nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
