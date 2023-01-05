---
title: 添加 Cells 到 Microsoft Excel 公式监视窗口
type: docs
weight: 60
url: /zh/net/add-cells-to-microsoft-excel-formula-watch-window/
---
## **可能的使用场景**

Microsoft Excel 监视窗口是一个有用的工具，可以方便地在窗口中监视单元格值及其公式。你可以打开*监视窗口*使用 Microsoft Excel 通过单击*公式 > 观看* *窗户*.它有*添加手表*按钮，可用于添加要检查的单元格。同样，您可以使用[**工作表.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index)添加单元格的方法*监视窗口*使用 Aspose.Cells API。

## **添加 Cells 到 Microsoft Excel 公式监视窗口**

以下示例代码设置单元格 C1 和 E1 的公式，并将它们都添加到监视窗口。然后将工作簿另存为[输出Excel文件](67338481.xlsx).如果打开输出 Excel 文件并查看*监视窗口*，您将看到两个单元格，如屏幕截图所示。

![待办事项：图片_替代_文本](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
