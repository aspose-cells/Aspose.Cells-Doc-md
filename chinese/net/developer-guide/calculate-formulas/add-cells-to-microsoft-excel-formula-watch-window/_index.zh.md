---
title: 将 Cells 添加到 Microsoft Excel 公式监视窗口
description: 如何使用 Aspose.Cells 库将单元格添加到 Excel 中的公式监视窗口。通过加载现有的 Excel 文件或创建新文件，我们可以操作其中的单元格并设置公式。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, Formula Watch Window, Cells, Adding
type: docs
weight: 60
url: /zh/net/add-cells-to-microsoft-excel-formula-watch-window/
---
##  **可能的使用场景**

Microsoft Excel 观察窗口是一个有用的工具，可以在窗口中方便地观察单元格值及其公式。您可以打开*观察窗*使用 Microsoft Excel，单击*公式 > 观看* *窗户*。它有*添加手表*按钮可用于添加要检查的单元格。同样，您可以使用[**工作表.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index)方法将细胞添加到*观察窗*使用 Aspose.Cells API。

##  **将 Cells 添加到 Microsoft Excel 公式监视窗口**

以下示例代码设置单元格 C1 和 E1 的公式，并将它们都添加到监视窗口。然后将工作簿另存为[输出Excel文件](67338481.xlsx)。如果您打开输出 Excel 文件并查看*观察窗口*，您将看到两个单元格，如本屏幕截图所示。

![待办事项：图像_替代_文本](add-cells-to-microsoft-excel-formula-watch-window_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
