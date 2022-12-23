---
title: 删除 Excel 文件中工作表的现有打印机设置
type: docs
weight: 40
url: /zh/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **可能的使用场景**
有时开发人员希望阻止 Excel 包含*。垃圾桶*保存的 XLSX 文件中的打印机设置文件。打印机设置文件位于*“[文件“root”]\xl\printerSettings”*.本文档说明如何使用 Aspose.Cells API 删除现有打印机设置。
## **删除 Excel 文件中工作表的现有打印机设置**
Aspose.Cells 允许您删除为 Excel 文件中的不同工作表指定的现有打印机设置。以下示例代码说明了如何删除工作簿中所有工作表的现有打印机设置。请看其[示例 Excel 文件](45056023.xlsx), [输出Excel文件](45056024.xlsx)，控制台输出以及屏幕截图以供参考。
## **截屏**
![待办事项：图片_替代_文本](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **控制台输出**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
