---
title: 将单元格添加到Microsoft Excel公式监视窗口
description: 如何使用 Aspose.Cells 库在 Excel 中添加单元格到公式观察窗口。通过加载现有的 Excel 文件或创建新的文件，我们可以操作其中的单元格并设置公式。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells、Excel、公式观察窗口、单元格、添加
type: docs
weight: 60
url: /zh/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel 观察窗口是一个方便查看单元格值和公式的工具。您可以通过在 Microsoft Excel 中单击 *公式 > 观察窗口* 来打开*观察窗口*。它有一个*添加观察*按钮，可用于添加要检查的单元格。同样，您可以使用 [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index) 方法使用 Aspose.Cells API 将单元格添加到 *观察窗口*。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了单元格 C1 和 E1 的公式，并将它们都添加到观察窗口中。然后将工作簿保存为[输出 Excel 文件](67338481.xlsx)。如果您打开输出的 Excel 文件并查看*观察窗口*，您将看到如此图所示的两个单元格。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
