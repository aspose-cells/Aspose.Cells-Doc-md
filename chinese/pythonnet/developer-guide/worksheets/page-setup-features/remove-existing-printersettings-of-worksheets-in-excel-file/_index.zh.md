---
title: 删除Excel文件中工作表的现有打印设置
type: docs
weight: 60
url: /zh/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 在本文中，您将学习如何通过Aspose.Cells for Python Excel库以编程方式使用示例代码移除Excel文件中工作表的现有打印设置。
keywords: Python Excel库，Python移除工作表的打印设置，Python移除Excel工作表的打印设置。
---

## **可能的使用场景**
有时开发人员希望阻止Excel在保存XLSX文件时包含*.bin*格式的打印设置文件。打印设置文件位于*[文件"根"]\xl\printerSettings*下。本文说明了如何使用Aspose.Cells for Python via .NET API移除现有的打印设置。

## **删除Excel文件中工作表的现有打印设置**
Aspose.Cells for Python via .NET允许您移除Excel文件中不同工作表的现有打印设置。以下示例代码说明了如何移除工作簿中所有工作表的现有打印设置。请参阅其[示例Excel文件](45056020.xlsx)、[输出Excel文件](45056021.xlsx)、控制台输出以及屏幕截图进行参考。

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
