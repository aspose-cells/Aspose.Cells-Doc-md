---
title: Display or Hide Scroll Bars in Php
type: docs
weight: 20
url: /java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Display or Hide Scroll Bars**
### **Hiding Scroll Bars**
To hide Scroll Bars using **Aspose.Cells Java for PHP**, call **displayhidescrollbars** module.

**PHP Code**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Download Running Code**
Download **Display or Hide Scroll Bars (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
