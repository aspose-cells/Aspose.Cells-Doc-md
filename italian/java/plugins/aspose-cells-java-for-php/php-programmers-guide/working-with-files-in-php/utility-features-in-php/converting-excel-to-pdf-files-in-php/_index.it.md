---
title: Convertire file Excel in file PDF in PHP
type: docs
weight: 30
url: /it/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Conversione di file Excel in PDF**
Per convertire Excel in file Pdf usando Aspose.Cells for Java in PHP, basta invocare il metodo excel_to_pdf() del modulo Converter.

**Codice PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Conversione di file Excel in PDF (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale sotto elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
