---
title: 在 Php 中显示或隐藏滚动条
type: docs
weight: 20
url: /zh/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - 显示或隐藏滚动条**
### **隐藏滚动条**
隐藏滚动条使用**Aspose.Cells Java 用于 PHP**， 称呼**显示隐藏滚动条**模块。

**PHP代码**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **下载运行代码**
下载**显示或隐藏滚动条 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
