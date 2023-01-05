---
title: 在 Php 中冻结窗格
type: docs
weight: 40
url: /zh/java/freeze-panes-in-php/
---
## **Aspose.Cells - 冻结窗格**
要冻结电子表格文档中的窗格，请使用**Aspose.Cells Java for PHP** 只需调用**冻结窗格**模块。

**PHP代码**

{{< highlight "php" >}}

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
下载**冻结窗格 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
