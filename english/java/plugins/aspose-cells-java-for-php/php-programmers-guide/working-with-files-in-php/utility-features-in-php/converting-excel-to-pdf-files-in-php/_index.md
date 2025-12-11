---
title: Converting Excel to PDF Files in PHP
type: docs
weight: 30
url: /java/converting-excel-to-pdf-files-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Excel to PDF Files**
To convert an Excel file to a PDF using Aspose.Cells for Java in PHP, simply invoke the `excel_to_pdf()` method of the Converter module.

**PHP Code**

{{< highlight php >}}
$saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

// Save the document in PDF format
$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);
{{< /highlight >}}

## **Download Running Code**
Download **Converting Excel to PDF Files (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
