---
title : "Page Break Preview in Php" 
description : "" 
weight : 24854 
toc : false
type: docs
url: /java/plugins/php/guide/worksheets/display/page+break+preview+in+php/
---

# Aspose.Cells for Java : Page Break Preview in Php


## Aspose.Cells - Page Break Preview

To set worksheet to page break preview using **Aspose.Cells Java for PHP**, simply invoke **PageBreakPreview** module.

**PHP Code**

{{< code lang="cs" >}}
//Instantiating a Excel object by excel file path
$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object
$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview
$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format
$workbook->save($dataDir . "output.xls");
{{< /code >}}

## Download Running Code

Download **Page Break Preview (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)

