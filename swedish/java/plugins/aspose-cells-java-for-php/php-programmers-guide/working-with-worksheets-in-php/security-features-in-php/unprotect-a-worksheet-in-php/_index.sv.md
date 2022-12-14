---
title: Ta bort skyddet av ett arbetsblad i Php
type: docs
weight: 20
url: /sv/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells - Ta bort skyddet av ett arbetsblad**
 För att skydda kalkylblad med hjälp av**Aspose.Cells Java för PHP** , ringa upp**unprotect_worksheet** metod av**skydd** modul.

**PHP-kod**

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
## **Ladda ner Running Code**
Ladda ner**Ta bort skyddet av ett kalkylblad (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
