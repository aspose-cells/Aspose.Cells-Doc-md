---
title: Copying and Moving Worksheets in Php
type: docs
weight: 10
url: /java/copying-and-moving-worksheets-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Copying and Moving Worksheets**
### **Copy Worksheets within a Workbook**
To copy worksheet using **Aspose.Cells for Java in PHP**, call **copy_worksheet** method of **copyworksheets** module. Below you can see code example.

**PHP Code**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Move Worksheets within a Workbook**
To move worksheet using **Aspose.Cells for Java in PHP**, call **move_worksheet** method of **copyworksheets** module. Below you can see code example.

**PHP Code**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Download Running Code**
Download **Copying and Moving Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
