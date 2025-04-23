---
title: 删除Excel文件中工作表的现有打印设置
type: docs
weight: 60
url: /zh/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 在本文中，您将学习如何通过C# API或.NET库以编程方式使用示例代码移除Excel文件中工作表的现有PrinterSettings。
keywords: 移除工作表c#的打印机设置，移除Excel工作表c#的打印机设置
---

## **可能的使用场景**
有时开发人员希望阻止Excel在保存的XLSX文件中包含打印机设置的*.bin*文件。打印机设置文件位于*“[file "root"]\xl\printerSettings”*。本文介绍了如何使用Aspose.Cells API移除现有的打印机设置。
## **删除Excel文件中工作表的现有打印设置**
Aspose.Cells允许您移除Excel文件中不同工作表的现有打印机设置。以下示例代码说明了如何移除工作簿中所有工作表的现有打印机设置。请参阅其示例Excel文件，输出Excel文件，控制台输出以及屏幕截图以供参考。
## **屏幕截图**
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
{{< app/cells/assistant language="csharp" >}}
