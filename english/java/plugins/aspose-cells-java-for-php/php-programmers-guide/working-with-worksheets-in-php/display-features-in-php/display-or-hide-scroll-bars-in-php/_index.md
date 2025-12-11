---
title: Display or Hide Scroll Bars in PHP
type: docs
weight: 20
url: /java/display-or-hide-scroll-bars-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display or Hide Scroll Bars**
### **Hiding Scroll Bars**
To hide scroll bars using **Aspose.Cells Java for PHP**, call the **DisplayHideScrollBars** module.

**PHP Code**

{{< highlight php >}}

 // Instantiating an Excel object by the Excel file path
$workbook = new Workbook($dataDir . "book1.xls");

// Hiding the vertical scroll bar of the Excel file
$workbook->getSettings()->setVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
$workbook->getSettings()->setHScrollBarVisible(false);

// Saving the modified Excel file in the default (Excel 2003) format
$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Download Running Code**
Download **Display or Hide Scroll Bars (Aspose.Cells)** from the social coding sites mentioned below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
