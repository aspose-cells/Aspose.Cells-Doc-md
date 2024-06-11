---
title: 在PHP中冻结窗格
type: docs
weight: 40
url: /zh/java/freeze-panes-in-php/
---

## **Aspose.Cells - 冻结窗格**
要使用 **Aspose.Cells Java for PHP** 冻结电子表格文件中的窗格, 只需调用 **FreezePanes** 模块。

**PHP 代码**

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
从以下提到的任何社交编码站点下载**Freeze Panes (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
