---
title: Excel Dateien in HTML in PHP konvertieren
type: docs
weight: 20
url: /de/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Konvertierung von Excel-Dateien in HTML**
Um Excel in HTML mit Aspose.Cells for Java in PHP zu konvertieren, rufen Sie einfach die Methode worksheet_to_html() des Converter-Moduls auf.

**PHP-Code**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die **Konvertierung von Excel-Dateien in HTML (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
