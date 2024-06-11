---
title: 在PHP中显示或隐藏网格线
type: docs
weight: 10
url: /zh/java/display-or-hide-gridlines-in-php/
---

## **Aspose.Cells - 显示或隐藏网格线**
### **隐藏网格线**
要使用**Aspose.Cells Java for PHP**隐藏工作表，调用**displayhidegridlines**模块。

**PHP 代码**

{{< highlight php >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**Display or Hide Gridlines (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
