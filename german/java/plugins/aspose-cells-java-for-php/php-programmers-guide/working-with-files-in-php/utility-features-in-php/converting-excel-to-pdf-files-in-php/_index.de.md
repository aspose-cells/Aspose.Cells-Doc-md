---
title: Konvertieren von Excel in PDF-Dateien in PHP
type: docs
weight: 30
url: /de/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells – Konvertieren von Excel in PDF-Dateien**
Um Excel mit Aspose.Cells for Java in PHP in eine PDF-Datei zu konvertieren, rufen Sie einfach Excel auf_zu_pdf()-Methode des Converter-Moduls.

**PHP-Code**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Konvertieren von Excel in PDF-Dateien (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
