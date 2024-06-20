---
title: Excel in PDF Dateien in PHP konvertieren
type: docs
weight: 30
url: /de/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Konvertierung von Excel in PDF-Dateien**
Um Excel in eine PDF-Datei mit Aspose.Cells for Java in PHP umzuwandeln, rufen Sie einfach die excel_to_pdf() Methode des Converter-Moduls auf.

**PHP-Code**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die **Konvertierung von Excel in PDF-Dateien (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
