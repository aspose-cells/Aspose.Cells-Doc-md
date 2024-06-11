---
title: 在Php中分割窗格
type: docs
weight: 70
url: /zh/java/split-panes-in-php/
---

## **Aspose.Cells - 拆分窗格**
要使用 **Aspose.Cells Java for PHP** 拆分窗格, 只需调用 **SplitPanes** 模块。

**PHP 代码**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **下载运行代码**
从以下社交编码网站中下载**拆分窗格（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
