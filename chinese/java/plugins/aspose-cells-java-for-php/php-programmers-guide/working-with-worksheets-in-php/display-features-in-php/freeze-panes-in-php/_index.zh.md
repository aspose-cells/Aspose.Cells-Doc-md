---
title: 在Php中冻结窗格
type: docs
weight: 40
url: /zh/java/freeze-panes-in-php/
---

## **Aspose.Cells - 冻结窗格**
要在**Aspose.Cells Java for PHP**中的电子表格文档中冻结窗格，简单调用**FreezePanes**模块。

**PHP代码**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **下载运行代码**
从下面列出的任何社交编码站点下载**冻结窗格（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
