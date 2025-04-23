---
title: 使用Aspose.Cells中的FormulaText功能与Python.NET
linktitle: 使用FormulaText函数
type: docs
weight: 60
url: /zh/python-net/using-formulatext-function-in-aspose-cells/
description: 了解如何使用Aspose.Cells for Python via .NET处理Excel的FORMULATEXT函数。获取和设置单元格公式，同时保持表格完整性。
keywords: Aspose.Cells、Python、Excel、FORMULATEXT、公式处理、电子表格自动化
---

{{% alert color="primary" %}} 

FORMULATEXT是Excel 2013及之后版本的函数。不支持早于Excel 2010或2007等版本。如其名，显示指定单元格中的公式文本。本文演示如何使用Aspose.Cells for Python via .NET调用此函数。

{{% /alert %}} 

以下示例代码展示了使用Aspose.Cells的FORMULATEXT。代码首先在A1单元格写入一个公式，然后在A2单元格使用FORMULATEXT显示公式文本。

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **控制台输出**
上述示例代码的控制台输出：

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
