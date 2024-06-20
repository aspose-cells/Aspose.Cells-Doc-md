---
title: Konvertera Excel till PDF filer i PHP
type: docs
weight: 30
url: /sv/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Konvertera Excel till PDF-filer**
För att konvertera Excel till Pdf-fil med Aspose.Cells for Java i PHP, helt enkelt anropa excel_to_pdf() metoden i konverteringsmodulen.

**PHP-kod**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Konvertera Excel till PDF-filer (Aspose.Cells)** från någon av de sociala kodningssidorna som nämns nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
