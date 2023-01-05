---
title: 在 Php 中拆分窗格
type: docs
weight: 70
url: /zh/java/split-panes-in-php/
---
## **Aspose.Cells - 拆分窗格**
拆分窗格使用**Aspose.Cells Java for PHP** 只需调用**分割面板**模块。

**PHP代码**

{{< highlight "php" >}}

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
下载**拆分窗格 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
