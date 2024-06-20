---
title: Kopiera och flytta arbetsblad i Php
type: docs
weight: 10
url: /sv/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - Kopiera och flytta kalkylblad**
### **Kopiera Kalkylblad inom en Arbetsbok**
För att kopiera arbetsblad med **Aspose.Cells for Java i PHP**, anropa **copy_worksheet** metoden för **copyworksheets** modulen. Nedan kan du se kodexemplet.

**PHP-kod**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Flytta kalkylblad inom en arbetsbok**
För att flytta arbetsblad med **Aspose.Cells for Java i PHP**, anropa **move_worksheet** metoden för **copyworksheets** modulen. Nedan kan du se kodexemplet.

**PHP-kod**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Ladda ned körbar kod**
Hämta **Kopiera och Flytta Arbeitsblad (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
