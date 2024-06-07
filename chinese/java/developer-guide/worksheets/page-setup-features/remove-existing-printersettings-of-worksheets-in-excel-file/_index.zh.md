---
title: 删除Excel文件中工作表的现有PrinterSettings
type: docs
weight: 40
url: /zh/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **可能的使用场景**
有时开发人员希望防止Excel在保存的XLSX文件中包括打印设置的*.bin*文件。打印设置文件位于“[文件“根”]\xl\printerSettings”下。本文解释了如何使用Aspose.Cells API去除现有的打印设置。
## **删除Excel文件中工作表的现有PrinterSettings**
Aspose.Cells允许您去除Excel文件中各个工作表指定的现有打印设置。以下示例代码演示了如何去除工作簿中所有工作表的现有打印设置。请参阅其[示例Excel文件](45056023.xlsx)、[输出Excel文件](45056024.xlsx)、控制台输出以及屏幕截图。
## **截图**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **控制台输出**
{{< highlight java >}}

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
