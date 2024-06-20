---
title: Sbloccare un foglio di lavoro in Php
type: docs
weight: 20
url: /it/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Sbloccare un foglio di lavoro**
Per proteggere il foglio di lavoro utilizzando **Aspose.Cells Java per PHP**, chiamare il metodo **unprotect_worksheet** del modulo **protection**.

**Codice PHP**

{{< highlight php >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Sbloccare un foglio di lavoro (Aspose.Cells)** da uno dei siti di codice sociale di seguito indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
