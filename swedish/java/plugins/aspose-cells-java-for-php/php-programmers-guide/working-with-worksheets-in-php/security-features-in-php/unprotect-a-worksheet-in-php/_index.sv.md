---
title: Avskydda ett arbetsblad i Php
type: docs
weight: 20
url: /sv/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Avskydda ett kalkylblad**
För att skydda arbetsblad med **Aspose.Cells Java för PHP**, anropa **unprotect_worksheet** metoden för **protection** modulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Avskydda ett kalkylblad (Aspose.Cells)** från någon av nedan nämnda sociala kodbaser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
