+++
title = "Copying and Moving Worksheets in Php" 
description = "" 
weight = 24864 
+++

Aspose.Cells for Java : Copying and Moving Worksheets in Php  

# Aspose.Cells for Java : Copying and Moving Worksheets in Php


## Aspose.Cells - Copying and Moving Worksheets

##### Copy Worksheets within a Workbook

To copy worksheet using **Aspose.Cells for Java in PHP**, call **copy\_worksheet** method of **copyworksheets** module. Below you can see code example.

**PHP Code**

{{< code lang="cs" >}}
# Create a Worksheets object with reference to the sheets of the Workbook.
$sheets = $workbook->getWorksheets();

# Copy data to a new sheet from an existing sheet within the Workbook.
$sheets->addCopy("Sheet1");

# Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir . "Copy Worksheet.xls");

{{< /code >}}

##### Move Worksheets within a Workbook

To move worksheet using **Aspose.Cells for Java in PHP**, call **move\_worksheet** method of **copyworksheets** module. Below you can see code example.

**PHP Code**

{{< code lang="cs" >}}
# Get the first worksheet in the book.
$sheet = $workbook->getWorksheets()->get(0);

# Move the first sheet to the third position in the workbook.
$sheet->moveTo(2);

# Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir . "Move Worksheet.xls");
{{< /code >}}

## Download Running Code

Download **Copying and Moving Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)

