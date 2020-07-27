+++
title = "Hide or Unhide a Worksheet in Php" 
description = "" 
weight = 24853 
+++

Aspose.Cells for Java : Hide or Unhide a Worksheet in Php  

# Aspose.Cells for Java : Hide or Unhide a Worksheet in Php


## Aspose.Cells - Hide or Unhide a Worksheet

##### Hiding a Worksheet

To hide worksheet using Aspose.Cells Java for PHP, call **hideunhideworksheet** module.

**PHP Code**

{{< code lang="cs" >}}
//Instantiating a Workbook object by excel file path
$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file
$worksheets = $workbook->getWorksheets();
$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file
$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir . "output.xls");

{{< /code >}}

## Download Running Code

Download **Hide or Unhide a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)

