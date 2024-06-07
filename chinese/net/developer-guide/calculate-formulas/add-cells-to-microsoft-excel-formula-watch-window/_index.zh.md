---
title: 将单元格添加到Microsoft Excel公式监视窗口
description: 如何使用Aspose.Cells库将单元格添加到Excel中的公式监视窗口。通过加载现有的Excel文件或创建一个新文件，我们可以操作其中的单元格并设置公式。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells，Excel，公式监视窗口，单元格，添加
type: docs
weight: 60
url: /zh/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel Watch Window是一个方便查看单元格数值及其公式的工具。您可以通过单击*公式>监视*窗口*在Microsoft Excel中打开*监视窗口*。它具有*添加监视*按钮，可用于将单元格添加到进行检查。同样，您可以使用Aspose.Cells API的[**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index)方法将单元格添加到*监视窗口*。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了单元格C1和E1的公式，并将它们都添加到监视窗口中。然后将工作簿保存为[输出Excel文件](67338481.xlsx)。如果您打开输出的Excel文件并查看*监视窗口*，您将看到如此截图中显示的两个单元格。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
