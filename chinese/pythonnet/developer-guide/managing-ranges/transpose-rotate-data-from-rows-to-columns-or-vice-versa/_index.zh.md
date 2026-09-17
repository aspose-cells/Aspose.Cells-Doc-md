---
title: 转置区域
linktitle: 转置区域
description: 本文介绍如何使用 Aspose.Cells for Python via .NET 通过三种不同方式在 Excel 文件中将数据从行转置或旋转到列，反之亦然。
keywords: Aspose.Cells for Python via .NET, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
url: /zh/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET 支持以三种不同的方式转置（旋转）数据，使行变为列、列变为行。第一种方法使用原地执行的 `range.transpose()` 方法，适用于所有 Excel 版本；第二种方法使用 `cell.set_dynamic_array_formula()` 来编写一个现代的动态数组 `=TRANSPOSE(...)` 公式，该公式可在 Excel 365 或 Excel 2021 上自动溢出；第三种方法使用 `cell.set_array_formula()` 来编写一个兼容旧版本 Excel 的经典 Ctrl+Shift+Enter (CSE) 数组公式。本文将逐一介绍每种方法，并提供分步说明和完整的代码示例。
{{% /alert %}}

## **简介**
转置区域意味着对其进行旋转，使原来的行变为列、原来的列变为行，从而实现数据沿主对角线的镜像翻转。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 用于执行此操作，相关概念参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。此概念可以以编程方式应用于单元格区域，在许多业务和报表场景中非常有用。
- 重新调整季度或年度销售报表的方向，使季度通常沿页面横向排列、区域沿页面纵向排列，或反之。
- 在仪表板或图表中切换坐标轴方向，使时间序列沿页面纵向排列而非横向排列。
- 重塑从外部系统导入的数据，使其与下游分析或报表模板所期望的布局相匹配。
为使本文后续内容更具体，每个示例都使用以下按区域和季度划分的小型销售数据表。在示例工作簿中，该表位于区域 **A1:D5**，其中 **A1** 留空作为左上角，**B1:D1** 为区域标题行，**A2:A5** 为季度标题列。
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
本文接下来将介绍使用 Aspose.Cells for Python via .NET 转置此数据的三种不同方式，每种方式适用于不同的 Excel 版本和用例。

## **方法 1 — 原地转置区域 (range.transpose)**
当您需要在不涉及 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方法。它适用于**所有 Excel 版本**，且不依赖动态数组，因此是最安全的跨版本兼容方案。当您只需要最终的转置输出而无需在工作簿中保留原始 `TRANSPOSE` 公式时，此方法是理想之选。

### **使用的 API**
`range.transpose()` 是 `Aspose.Cells.Range` 类上的一个实例方法。调用该方法会原地翻转区域，交换其行和列，使原来的行变为列、原来的列变为行。该方法直接修改底层单元格，而不会写入公式。

### **步骤**
1. 通过调用 `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，并将 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.worksheets[0]` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.cells` 访问工作表的单元格集合。
4. 通过调用 `cells.create_range("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 原地旋转区域，交换行和列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，初始锚点区域将保存旋转后的数据。第一行为（空、**Europe**、**Asia**、**North America**），第一列为（空、**Qtr 1**、**Qtr 2**、**Qtr 3**、**Qtr 4**）。原始的每个销售列都会变为转置区域中的一行。

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **方法 2 — 使用动态数组公式进行转置 (Excel 365 / 2021)**
当您希望将 `=TRANSPOSE(A1:D5)` 公式作为活动公式保留在输出工作簿中，以便在源数据更改时结果能自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开时，请使用此方法。

### **使用的 API**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` 是 `Aspose.Cells.Cell` 类上的一个方法，用于将单元格的公式设置为**动态数组公式**。Excel 仅计算一次公式，并自动将结果溢出到周围的单元格中。第三个参数设置为 `True` 时，会指示 Aspose.Cells 在写入时同时计算结果值。

### **步骤**
1. 使用 `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `cells` 集合。
3. 通过调用 `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)` 在源区域正下方的单元格 **A6** 上放置动态数组公式。
4. `None` 参数传递默认的 `FormulaParseOptions`，第三个参数 `True` 告诉 Aspose.Cells 将该公式视为动态数组并对其进行计算，以便将溢出值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 保存公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到区域 **A6:D10**，即一个 5 行 4 列的块，与转置后的数据相对应。

{{% alert color="primary" %}}
此方法**仅适用于 Excel 365 / 2021 或更高版本**。较旧的 Excel 版本将无法正确溢出动态数组公式。
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **方法 3 — 使用经典数组公式 (CSE) 进行转置**
当您希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能在不支持动态数组溢出的**较旧 Excel 版本（2021 之前，包括 2019、2016、2013 等）**中打开时，请使用此方法。经典的 CSE (Ctrl+Shift+Enter) 数组公式是所有 Excel 版本都能计算的向后兼容替代方案。

### **使用的 API**
`cell.set_array_formula(array_formula, n_rows, n_columns)` 是 `Aspose.Cells.Cell` 类上的一个方法，用于将**经典数组 (CSE) 公式**分配给锚点单元格，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，以便 Excel 将该公式作为单个数组表达式进行计算，从而填充所声明的区域。

### **步骤**
1. 按照前述方法加载源工作簿。
2. 获取第一个工作表并访问其 `cells` 集合。
3. 调用 `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点，所计算的数组从 A6 开始跨越 4 行 5 列，与 A1:D5 源区域的转置维度相匹配。Excel 会在结果区域写入一个数组公式标记，以便较旧的 Excel 版本能够正确计算。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 中计算 `TRANSPOSE` 表达式的经典方式，此方法在所有 Excel 版本中都通用兼容。
{{% /alert %}}

```python
import aspose.cells as ac
# 使用 xlsx LoadOptions 加载源工作簿
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# 访问第一个工作表及其 Cells 集合
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# 在单元格 A6 上设置经典的 CSE 数组公式。
# 公式 =TRANSPOSE(A1:D5) 将 5 行 4 列的源区域旋转
# 为 4 行 5 列的数组。第二个参数 (4) 是行数
# 第三个参数 (5) 是结果数组的列数。
# Aspose.Cells 写入 CSE 数组公式标记，以便 Excel 将其作为
# 单个多单元格数组公式进行计算，兼容较旧的 Excel 版本
# （2019、2016、2013 等）这些版本不支持动态数组溢出。
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# 保存工作簿以使数组公式标记持久化
workbook.save("output.xlsx")
```

## **对比 — 何时使用每种方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留源公式 | 输出区域 |
|----------|--------------|---------------|--------------------------|--------------|
| 方法 1 — 原地转置 | `range.transpose()` | 所有 Excel 版本 | 否（仅值） | 初始锚点区域，5×4 |
| 方法 2 — 动态数组公式 | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点溢出 |
| 方法 3 — 经典数组公式 (CSE) | `cell.set_array_formula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式大小，4×5 |
当您需要快速进行跨版本转换、且仅需要将转置后的值写入文件时，请使用**方法 1**。当可以确定使用现代 Excel 且希望公式保持活动状态并在源数据更改时自动更新时，请使用**方法 2**。当您需要在每个 Excel 版本（包括不支持动态数组的较旧版本）中以保留公式的方式获得最广泛的兼容性时，请使用**方法 3**。

## **相关文章**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/zh/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/zh/python-net/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/zh/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}