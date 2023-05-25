---
title: 删除 Excel 文件中工作表的现有打印机设置
type: docs
weight: 60
url: /zh/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 在本文中，您将学习如何使用示例代码使用 C# API 或 .NET 库，通过页面设置对象以编程方式删除 Excel 文件中工作表的现有 PrinterSettings。
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **可能的使用场景**
有时开发人员希望阻止 Excel 包含*。垃圾桶*保存的 XLSX 文件中的打印机设置文件。打印机设置文件位于*“[文件“root”]\xl\printerSettings”。*本文档说明如何使用 Aspose.Cells API 删除现有打印机设置。
##  **删除 Excel 文件中工作表的现有打印机设置**
Aspose.Cells 允许您删除为 Excel 文件中的不同工作表指定的现有打印机设置。以下示例代码说明了如何删除工作簿中所有工作表的现有打印机设置。请看其[示例 Excel 文件](45056020.xlsx), [输出Excel文件](45056021.xlsx)，控制台输出以及屏幕截图以供参考。
##  **截屏**
![待办事项：image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **控制台输出**
{{< highlight "java" >}}

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
