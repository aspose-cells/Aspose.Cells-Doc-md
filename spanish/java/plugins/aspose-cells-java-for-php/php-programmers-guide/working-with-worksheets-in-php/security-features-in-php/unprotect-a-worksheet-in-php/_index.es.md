---
title: Desproteger una hoja de cálculo en Php
type: docs
weight: 20
url: /es/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Desproteger una hoja de cálculo**
Para desproteger la hoja de cálculo usando **Aspose.Cells Java para PHP**, llame al método **unprotect_worksheet** del módulo **protection**.

**Código PHP**

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
## **Descargar Código en Ejecución**
Descargar **Desproteger una hoja de cálculo (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
