---
title: Rimuovere la protezione di un foglio di lavoro in Php
type: docs
weight: 20
url: /it/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells - Rimuovere la protezione di un foglio di lavoro**
 Per proteggere il foglio di lavoro utilizzando**Aspose.Cells Giava for PHP** , chiamata**unprotect_worksheet** metodo di**protezione** modulo.

**Codice PHP**

{{< highlight "php" >}}

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
Scarica**Rimuovere la protezione di un foglio di lavoro (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
