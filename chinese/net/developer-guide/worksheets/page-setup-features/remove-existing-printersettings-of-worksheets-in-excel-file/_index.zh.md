---
title: 删除Excel文件中工作表的现有PrinterSettings
type: docs
weight: 60
url: /zh/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 本文中，您将学习如何通过Page Setup对象以编程方式使用C# API或.NET库的示例代码在Excel文件中删除工作表的现有PrinterSettings。
keywords: 以C#方式删除工作表的打印机设置，以C#方式删除Excel工作表的打印机设置
---

## **可能的使用场景**
有时，开发人员希望阻止Excel在保存为XLSX文件时包含打印设置的*.bin*文件。打印设置文件位于“[file "root"]\xl\printerSettings”下。本文介绍使用Aspose.Cells APIs如何删除现有的打印机设置。
## **删除Excel文件中工作表的现有PrinterSettings**
Aspose.Cells允许您删除Excel文件中不同工作表指定的现有打印机设置。以下示例代码说明如何删除工作簿中所有工作表的现有打印机设置。请参考其[sample Excel file](45056020.xlsx)，[output Excel file](45056021.xlsx)，控制台输出以及截图。
## **截图**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **控制台输出**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
