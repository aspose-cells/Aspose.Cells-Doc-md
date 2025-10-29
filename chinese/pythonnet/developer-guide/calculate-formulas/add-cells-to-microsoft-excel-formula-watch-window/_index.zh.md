---
title: 用 Python.NET 将单元格添加到 Microsoft Excel 公式监视窗口中
linktitle: 向公式监视窗口添加单元格
type: docs
weight: 60
url: /zh/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: 学习如何使用Aspose.Cells for Python via .NET在Excel的公式观察窗口中监视单元格。包括代码示例和API参考。
keywords: Python excel，公式监视窗口，单元格监控，aspose.cells，python.net
---

## **可能的使用场景**

Microsoft Excel 的监视窗口是一个方便的工具，用于在专用窗口中监控单元格值和公式。你可以通过导航到 *公式 > 监视窗口* 来打开 *监视窗口*。添加监视的按钮允许你添加需要观察的单元格。同样，你也可以使用 [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) 方法，利用 Aspose.Cells API 以编程方式将单元格添加到监视窗口中。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码为单元格 C1 和 E1 设置公式，然后将它们添加到监视窗口中。它将工作簿保存为 [输出Excel文件](67338481.xlsx)。在Excel中打开输出文件时，两个单元格都将显示在监视窗口中，如下图所示：

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
