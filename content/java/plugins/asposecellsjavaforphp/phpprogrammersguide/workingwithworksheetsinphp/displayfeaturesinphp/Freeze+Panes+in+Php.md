+++
title = "Freeze Panes in Php" 
description = "" 
weight = 24852 
+++

Aspose.Cells for Java : Freeze Panes in Php  

# Aspose.Cells for Java : Freeze Panes in Php


## Aspose.Cells - Freeze Panes

To Freeze Panes in the Spreadsheet Document using **Aspose.Cells Java for PHP**, simply invoke **FreezePanes** module.

**PHP Code**

{{< code lang="cs" >}}
//Instantiating a Excel object by excel file path
$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);

//Applying freeze panes settings
$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format
$workbook->save($dataDir . "book.out.xls");
{{< /code >}}

## Download Running Code

Download **Freeze Panes (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)

