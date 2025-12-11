---
title: Display or Hide Gridlines in PHP
type: docs
weight: 10
url: /java/display-or-hide-gridlines-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display or Hide Gridlines**
### **Hiding Gridlines**
To hide a worksheet using **Aspose.Cells Java for PHP**, call the **DisplayHideGridlines** module.

**PHP Code**

{{< highlight php >}}

$data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) . '/data/';

// Instantiating a Workbook object by Excel file path
$workbook = new Workbook($data_dir . "book1.xls");

// Accessing the first worksheet in the Excel file
$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

// Hiding the grid lines of the first worksheet in the Excel file
$worksheet->setGridlinesVisible(false);

// Saving the modified Excel file in the default (Excel 2000) format
$workbook->save($data_dir . "output.xls");

{{< /highlight >}}

## **Download Running Code**
Download **Display or Hide Gridlines (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
