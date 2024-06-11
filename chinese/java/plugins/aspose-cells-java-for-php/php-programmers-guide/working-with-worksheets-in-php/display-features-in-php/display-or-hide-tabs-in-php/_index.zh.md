---
title: 在PHP中显示或隐藏标签
type: docs
weight: 30
url: /zh/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - 显示或隐藏标签页**
### **隐藏选项卡**
要使用**Aspose.Cells Java for PHP**隐藏标签，调用**displayhidetabs**模块。

**PHP 代码**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**隐藏或显示标签页 (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
