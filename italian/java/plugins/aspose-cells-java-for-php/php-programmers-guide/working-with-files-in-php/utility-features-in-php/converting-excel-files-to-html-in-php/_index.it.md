---
title: Convertire file Excel in HTML in PHP
type: docs
weight: 20
url: /it/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Convertire file Excel in HTML**
Per convertire Excel in HTML usando Aspose.Cells for Java in PHP, basta invocare il metodo worksheet_to_html() del modulo Converter.

**Codice PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Convertire file Excel in HTML (Aspose.Cells)** da uno dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
