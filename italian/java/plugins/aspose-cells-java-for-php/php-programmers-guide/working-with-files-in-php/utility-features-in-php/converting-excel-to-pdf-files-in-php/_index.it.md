---
title: Conversione di Excel in file PDF in PHP
type: docs
weight: 30
url: /it/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - Conversione di Excel in file PDF**
Per convertire Excel in file Pdf usando Aspose.Cells for Java in PHP, basta invocare excel_a_pdf() del modulo Converter.

**Codice PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Conversione di Excel in file PDF (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
