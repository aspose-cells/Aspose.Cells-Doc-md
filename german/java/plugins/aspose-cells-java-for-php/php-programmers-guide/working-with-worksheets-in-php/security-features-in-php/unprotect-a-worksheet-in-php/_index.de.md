---
title: Entschützen Sie ein Arbeitsblatt in Php
type: docs
weight: 20
url: /de/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells – Schutz eines Arbeitsblatts aufheben**
 Arbeitsblatt mit schützen**Aspose.Cells Java for PHP** , Anruf**unprotect_worksheet** Methode von**Schutz** Modul.

**PHP-Code**

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
## **Laufcode herunterladen**
Download**Schutz eines Arbeitsblatts aufheben (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
