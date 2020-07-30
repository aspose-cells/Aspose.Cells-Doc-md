---
title : "Display or Hide Gridlines in Php" 
description : "" 
weight : 24849 
toc : false
type: docs
url: /java/plugins/php/guide/worksheets/display/display+or+hide+gridlines+in+php/
---

# Aspose.Cells for Java : Display or Hide Gridlines in Php


## Aspose.Cells - Display or Hide Gridlines

##### Hiding Gridlines

To hide worksheet using **Aspose.Cells Java for PHP**, call **displayhidegridlines** module.

**PHP Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'//Instantiating a Workbook object by excel file path$workbook = new Workbook($dataDir . "book1.xls");//Accessing the first worksheet in the Excel file$worksheets = $workbook->getWorksheets();$worksheet = $worksheets->get(0);//Hiding the grid lines of the first worksheet of the Excel file$worksheet->setGridlinesVisible(false);//Saving the modified Excel file in default (that is Excel 2000) format$workbook->save($dataDir . "output.xls");

## Download Running Code

Download **Display or Hide Gridlines (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)

