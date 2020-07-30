---
title : "Display or Hide Tabs in Php" 
description : "" 
weight : 24851 
toc : false
type: docs
url: /java/plugins/php/guide/worksheets/display/display+or+hide+tabs+in+php/
---

# Aspose.Cells for Java : Display or Hide Tabs in Php


## Aspose.Cells - Display or Hide Tabs

##### Hiding Tabs

To hide tabs using **Aspose.Cells Java for PHP**, call **displayhidetabs** module.

**PHP Code**

{{< code lang="cs" >}}
//Instantiating a Workbook object by excel file path
$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file
$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format
$workbook->save($dataDir + "output.xls");
{{< /code >}}

## Download Running Code

Download **Hide or Display or Hide Tabs (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)

