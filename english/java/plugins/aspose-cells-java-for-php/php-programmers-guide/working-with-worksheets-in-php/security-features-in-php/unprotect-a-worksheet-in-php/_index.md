---
title: Unprotect a Worksheet in PHP
type: docs
weight: 20
url: /java/unprotect-a-worksheet-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Unprotect a Worksheet**
To unprotect a worksheet using **Aspose.Cells Java for PHP**, call the **unprotect** method of the **protection** module.

**PHP Code**

{{< highlight php >}}
$filesFormatType = new FileFormatType();

// Instantiating a Workbook object
$workbook = new Workbook($dataDir . "book1.xls");
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);
$protection = $worksheet->getProtection();

// Unprotecting the worksheet with a password
$worksheet->unprotect("aspose");

// Save the Excel file.
$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003);
{{< /highlight >}}

## **Download Running Code**
Download **Unprotect a Worksheet (Aspose.Cells)** from any of the below-mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
