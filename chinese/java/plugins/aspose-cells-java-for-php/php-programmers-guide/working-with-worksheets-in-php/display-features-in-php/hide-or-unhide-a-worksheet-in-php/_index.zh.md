---
title: 在 Php 中隐藏或取消隐藏工作表
type: docs
weight: 50
url: /zh/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - 隐藏或取消隐藏工作表**
### **隐藏工作表**
要使用 Aspose.Cells Java for PHP 隐藏工作表，请调用**隐藏取消隐藏工作表**模块。

**PHP代码**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **下载运行代码**
下载**隐藏或取消隐藏工作表 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
