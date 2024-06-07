---
title: 在Php中显示或隐藏滚动条
type: docs
weight: 20
url: /zh/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - 显示或隐藏滚动条**
### **隐藏滚动条**
要使用**Aspose.Cells Java for PHP**隐藏滚动条，请调用**displayhidescrollbars**模块。

**PHP代码**

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
## **下载运行代码**
从以下社交编码网站之一下载**显示或隐藏滚动条（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
