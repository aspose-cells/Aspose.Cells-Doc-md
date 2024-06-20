---
title: Arbeitsblätter in PHP kopieren und verschieben
type: docs
weight: 10
url: /de/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - Kopieren und Verschieben von Arbeitsblättern**
### **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**
Um ein Arbeitsblatt mit **Aspose.Cells for Java in PHP** zu kopieren, rufen Sie die Methode **copy_worksheet** des Moduls **copyworksheets** auf. Nachfolgend finden Sie ein Beispiel für den Code.

**PHP-Code**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**
Um ein Arbeitsblatt mit **Aspose.Cells for Java in PHP** zu verschieben, rufen Sie die Methode **move_worksheet** des Moduls **copyworksheets** auf. Nachfolgend finden Sie ein Beispiel für den Code.

**PHP-Code**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Kopieren und Verschieben von Arbeitsblättern (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
