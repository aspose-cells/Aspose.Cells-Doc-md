---
title: Konvertieren von Excel-Dateien in HTML in PHP
type: docs
weight: 20
url: /de/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells – Konvertieren von Excel-Dateien in HTML**
Um Excel mit Aspose.Cells for Java in PHP in HTML zu konvertieren, rufen Sie einfach das Arbeitsblatt auf_zu_html()-Methode des Converter-Moduls.

**PHP-Code**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Konvertieren von Excel-Dateien in HTML (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
