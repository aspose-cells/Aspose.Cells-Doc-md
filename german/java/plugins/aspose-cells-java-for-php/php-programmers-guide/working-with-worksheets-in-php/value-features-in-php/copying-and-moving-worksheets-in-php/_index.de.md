---
title: Kopieren und Verschieben von Arbeitsblättern in Php
type: docs
weight: 10
url: /de/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells – Kopieren und Verschieben von Arbeitsblättern**
### **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**
 Arbeitsblatt kopieren mit**Aspose.Cells for Java in PHP** , Anruf**copy_worksheet** Methode von**Arbeitsblätter kopieren** Modul. Unten sehen Sie ein Codebeispiel.

**PHP-Code**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**
 Arbeitsblatt verschieben mit**Aspose.Cells for Java in PHP** , Anruf**move_worksheet** Methode von**Arbeitsblätter kopieren** Modul. Unten sehen Sie ein Codebeispiel.

**PHP-Code**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Arbeitsblätter kopieren und verschieben (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
