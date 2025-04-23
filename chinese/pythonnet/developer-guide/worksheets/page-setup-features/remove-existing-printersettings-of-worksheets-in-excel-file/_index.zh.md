---
title: 删除Excel文件中工作表的现有打印设置
type: docs
weight: 60
url: /zh/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 本文将教你如何通过 Page Setup 对象，程序化移除 Excel 文件中工作表的现有 PrinterSettings（打印机设置），附带示例代码。
keywords: Python Excel 库，Python 移除工作表的打印机设置，Python 移除工作表的打印机设置。
---

## **可能的使用场景**
有时开发者希望阻止 Excel 在保存的 XLSX 文件中包含 *.bin* 格式的打印机设置文件。打印机设置文件位于 *“[file "root"]\xl\printerSettings”* 位置。本文介绍如何使用 Aspose.Cells for Python via .NET API 移除现有的打印机设置。

## **删除Excel文件中工作表的现有打印设置**
Aspose.Cells for Python via .NET 允许你删除为Excel文件中不同工作表指定的现有打印机设置。以下示例代码演示如何删除工作簿中所有工作表的现有打印机设置。请参阅其[sample Excel文件](45056020.xlsx)、[输出Excel文件](45056021.xlsx)、控制台输出以及截图作为参考。

## **屏幕截图**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
