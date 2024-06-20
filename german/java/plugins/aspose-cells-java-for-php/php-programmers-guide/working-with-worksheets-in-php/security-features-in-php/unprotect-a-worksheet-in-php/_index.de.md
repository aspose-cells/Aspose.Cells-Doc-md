---
title: Ein Arbeitsblatt in PHP entriegeln
type: docs
weight: 20
url: /de/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Ein Arbeitsblatt entschützen**
Um ein Arbeitsblatt mit **Aspose.Cells Java für PHP** zu schützen, rufen Sie die Methode **unprotect_worksheet** des Moduls **protection** auf.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Unprotect a Worksheet (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
