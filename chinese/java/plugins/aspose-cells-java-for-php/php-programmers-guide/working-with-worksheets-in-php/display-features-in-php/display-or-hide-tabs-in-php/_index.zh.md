---
title: 在Php中显示或隐藏选项卡
type: docs
weight: 30
url: /zh/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - 显示或隐藏选项卡**
### **隐藏选项卡。**
要隐藏选项卡，请在**Aspose.Cells Java for PHP**中调用**displayhidetabs**模块。

**PHP代码**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **下载运行代码**
从以下社交编码网站之一下载**隐藏或显示选项卡（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
