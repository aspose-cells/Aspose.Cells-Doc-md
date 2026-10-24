---
title: 转置区域
linktitle: 转置区域
description: 本文介绍如何使用 Aspose.Cells for Python via .NET 在 Excel 文件中转置或旋转数据，将行转换为列或将列转换为行，并说明三种不同的实现方法。
keywords: Aspose.Cells for Python via .NET, 电子表格, 转置区域, 旋转数据, TRANSPOSE 函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
url: /zh/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET 支持通过三种不同方式转置（旋转）数据，使行变为列、列变为行。第一种方式使用 `range.transpose()` 方法就地转置数据，适用于所有 Excel 版本；第二种方式使用 `cell.set_dynamic_array_formula()` 写入现代动态数组公式 `=TRANSPOSE(...)`，该公式会在 Excel 365 或 Excel 2021 中自动溢出；第三种方式使用 `cell.set_array_formula()` 写入经典 Ctrl+Shift+Enter (CSE) 数组公式，与较旧的 Excel 版本兼容。本文通过分步说明和完整的代码示例介绍每种方式。
{{% /alert %}}

## **简介**
转置区域是指旋转该区域，使原本的行变为列、原本的列变为行，即以主对角线为轴翻转数据。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 可执行此操作。有关此概念，请参阅 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。这一概念可通过编程方式应用于单元格区域，适用于许多业务和报表场景。
- 重新调整季度或年度销售报告的方向，使季度通常横跨页面的布局变为区域沿页面纵向排列，或反之。
- 交换仪表板或图表中的轴方向，使时间序列沿页面纵向而非横向延伸。
- 调整从外部系统导入数据的布局，使其符合下游分析或报表模板的预期。
为了使后续内容更加直观，每个示例都使用以下按区域和季度划分的小型销售表。在示例工作簿中，该表占据 **A1:D5** 区域，其中 **A1** 作为左上角保持为空，**B1:D1** 包含区域标题，**A2:A5** 包含季度标题。
| 区域             | 欧洲       | 亚洲       | 北美洲     |
|------------------|-----------|-----------|-----------|
| 第一季度         | 21704714  | 8774099   | 12094215  |
| 第二季度         | 17987034  | 12214447  | 10873099  |
| 第三季度         | 19485029  | 14356879  | 15689543  |
| 第四季度         | 22567894  | 15763492  | 17456723  |
随后，本文将介绍使用 Aspose.Cells for Python via .NET 转置此数据的三种不同方式，每种方式都适用于不同的 Excel 版本和使用场景。

## **方法 1 — 就地转置区域（range.transpose）**
如果希望在不调用 `TRANSPOSE` 工作表函数的情况下转置数据，请使用此方法。它适用于**所有 Excel 版本**，不依赖动态数组，因此是最安全的跨版本兼容选项。如果只需最终的转置结果，且无需在工作簿中保留 `TRANSPOSE` 公式，则适合使用此方法。

### **使用的 API**
`range.transpose()` 是 `Aspose.Cells.Range` 类的实例方法。调用该方法会就地转置区域，通过交换行和列，使原本的行变为列、原本的列变为行。该方法直接修改底层单元格，而不写入公式。

### **步骤**
1. 调用 `Workbook(srcFile, LoadOptions(LoadFormat.XLSX))` 打开源工作簿，并使用 `LoadOptions` 指定 `.xlsx` 格式。
2. 使用 `workbook.worksheets[0]` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.cells` 访问工作表的 `cells` 集合。
4. 调用 `cells.create_range("A1:D5")` 创建涵盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 就地转置该区域，交换行和列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，初始锚定区域包含旋转后的数据。第一行显示（空、**欧洲**、**亚洲**、**北美洲**），第一列显示（空、**第一季度**、**第二季度**、**第三季度**、**第四季度**）。销售数据中的每个原始列都会成为转置后区域中的一行。

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

## **方法 2 — 使用动态数组公式转置（Excel 365 / 2021）**
如果希望将 `=TRANSPOSE(A1:D5)` 作为动态公式保留在输出工作簿中，使源数据发生变化时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开，请使用此方法。

### **使用的 API**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` 是 `Aspose.Cells.Cell` 类的方法，用于将单元格的公式设置为**动态数组公式**。Excel 仅对公式求值一次，然后自动将结果溢出到周边单元格。第三个参数设为 `True` 时，Aspose.Cells 会在写入文件时一并计算生成的值。

### **步骤**
1. 使用 `Workbook(srcFile, LoadOptions(LoadFormat.XLSX))` 加载源工作簿。
2. 获取第一个工作表并访问其 `cells` 集合。
3. 在源区域正下方的单元格 **A6** 中设置动态数组公式，调用 `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`。
4. `None` 参数用于传入默认的 `FormulaParseOptions`；第三个参数 `True` 指示 Aspose.Cells 将该公式视为动态数组并进行计算，从而将溢出值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 中包含公式 `=TRANSPOSE(A1:D5)`，Excel 会将结果自动溢出到 **A6:D10** 区域，即一个 5 行 × 4 列的块，与转置后的数据一致。

{{% alert color="primary" %}}
此方法**仅适用于 Excel 365 / 2021 或更高版本**。较旧的 Excel 版本无法正确处理动态数组公式的溢出。
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells.get("A6").set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.XLSX)
```

## **方法 3 — 使用经典数组公式转置（CSE）**
如果希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能会在**较旧的 Excel 版本（2021 之前，包括 2019、2016、2013 等）中打开，而这些版本不支持动态数组溢出，请使用此方法。经典 CSE (Ctrl+Shift+Enter) 数组公式是一种向后兼容的替代方案，所有 Excel 版本均可对其进行求值。

### **使用的 API**
`cell.set_array_formula(array_formula, n_rows, n_columns)` 是 `Aspose.Cells.Cell` 类的方法，用于为锚点单元格设置**经典数组 (CSE) 公式**，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，使 Excel 将该公式作为单个数组表达式求值并填充指定的区域。

### **步骤**
1. 按前述方法加载源工作簿。
2. 获取第一个工作表并访问其 `cells` 集合。
3. 调用 `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点。求值后的数组从 A6 开始，覆盖 4 行 × 5 列的区域，与 A1:D5 源区域转置后的维度一致。Excel 会在结果区域中写入单个数组公式标记，使较旧的 Excel 版本能够正确对该公式求值。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 对 `TRANSPOSE` 表达式求值的经典方式，此方法与所有 Excel 版本兼容。
{{% /alert %}}

```python
import aspose.cells as ac
# 使用 xlsx LoadOptions 加载源工作簿
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
# 访问第一个工作表及其 Cells 集合
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# 在单元格 A6 上设置经典 CSE 数组公式。
# 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源范围
# 转换为 4 行 x 5 列的数组。第二个参数 (4) 是结果数组的行数，
# 第三个参数 (5) 是结果数组的列数。
# Aspose.Cells 会写入 CSE 数组公式标记，以便 Excel 将其作为
# 单个多单元格数组公式进行计算，兼容不支持动态数组溢出的旧版 Excel
# 版本（2019、2016、2013 等）。
cells.get("A6").set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# 保存工作簿，以持久化数组公式标记
workbook.save("output.xlsx")
```

## **比较 — 何时使用每种方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留公式？ | 输出区域 |
|------|------------|------------|------------------|----------|
| 方法 1 — 就地转置 | `range.transpose()` | 所有 Excel 版本 | 否（仅写入值） | 初始锚定区域，5×4 |
| 方法 2 — 动态数组公式 | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点开始溢出 |
| 方法 3 — 经典数组公式 (CSE) | `cell.set_array_formula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式维度，4×5 |
如果需要快速完成跨版本转换，且只需将转置后的值写入文件，请使用**方法 1**。如果可确保使用现代 Excel，并希望公式保持动态，在源数据发生变化时自动更新，请使用**方法 2**。如果需要在所有 Excel 版本（包括不支持动态数组的较旧版本）中保留公式并获得最广泛的兼容性，请使用**方法 3**。

## **相关文章**
- [SmartMarker 单单元格数组呈现 | Aspose.Cells for Python via .NET](/cells/zh/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [将图像插入单元格](/cells/zh/python-net/inserting-an-image-into-a-cell/)
- [将 Excel 文件拆分为多个文件](/cells/zh/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}