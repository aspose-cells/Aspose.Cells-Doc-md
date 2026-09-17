---
title: 转置区域
linktitle: 转置区域
description: 本文介绍如何使用 Aspose.Cells for Python via Java 通过三种不同方法在 Excel 文件中转置或旋转数据，将行转为列，反之亦然。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
url: /zh/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java 支持以三种不同方式转置（旋转）数据，使行变为列、列变为行。第一种方法使用就地执行的 `Range.transpose()` 方法，兼容所有 Excel 版本；第二种方法使用 `Cell.setDynamicArrayFormula()` 写入现代动态数组公式 `=TRANSPOSE(...)`，该公式可在 Excel 365 或 Excel 2021 中自动溢出；第三种方法使用 `Cell.setArrayFormula()` 写入经典的 Ctrl+Shift+Enter（CSE）数组公式，兼容较旧版本的 Excel。本文通过分步说明和完整的代码示例逐一讲解每种方法。
{{% /alert %}}

## **介绍**
转置区域意味着将其旋转，使原本作为行的内容变为列，原本作为列的内容变为行，从而沿主对角线反射数据。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 用于执行此操作，相关概念参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。同样的思路可以编程方式应用于单元格区域，这在许多业务和报表场景中都非常有用。
转置有用的常见场景包括以下几种。
- 调整季度或年度销售报表的方向，使季度通常横跨页面、区域纵向排列，反之亦然。
- 交换仪表板或图表中的坐标轴方向，使时间序列纵向排列而非横向排列。
- 重塑从外部系统导入的数据，使其符合下游分析或报表模板所期望的布局。
为使后续内容具体化，所有示例均使用以下按区域和季度划分的小型销售表。在示例工作簿中，此表占用区域 **A1:D5**，其中 **A1** 留空作为左上角，**B1:D1** 存放区域标题，**A2:A5** 存放季度标题。
| 区域            | 欧洲       | 亚洲       | 北美         |
|-----------------|-----------|-----------|-------------|
| 第一季度         | 21704714  | 8774099   | 12094215    |
| 第二季度         | 17987034  | 12214447  | 10873099    |
| 第三季度         | 19485029  | 14356879  | 15689543    |
| 第四季度         | 22567894  | 15763492  | 17456723    |
本文随后介绍使用 Aspose.Cells for Python via Java 转置此数据的三种不同方法，每种方法适用于不同的 Excel 版本和用例。

## **方法一 — 就地转置区域 (Range.transpose)**
当您需要在不使用 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方法。它适用于 **所有 Excel 版本**，不依赖动态数组，是最安全的跨版本兼容选项。当您仅需要最终的转置结果而无需在工作簿中保留原始 `TRANSPOSE` 公式时，这是理想选择。

### **使用的 API**
`Range.transpose()` 是 `com.aspose.cells.Range` 类的一个实例方法。调用它可就地翻转区域，交换其行和列，使原本作为行的内容变为列，原本作为列的内容变为行。该方法直接修改底层单元格而不写入任何公式。

### **步骤**
1. 通过调用 `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，并将 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.getWorksheets().get(0)` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.getCells()` 访问工作表的单元格集合。
4. 通过调用 `cells.createRange("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 就地旋转区域，交换行和列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，相同的锚定区域将持有旋转后的数据。第一行显示（空、**欧洲**、**亚洲**、**北美**），第一列显示（空、**第一季度**、**第二季度**、**第三季度**、**第四季度**）。每个原始销售列变为转置区域中的一行。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **方法二 — 使用动态数组公式转置 (Excel 365 / 2021)**
当您希望将 `=TRANSPOSE(A1:D5)` 公式作为活动公式保留在输出工作簿中，以便在源数据更改时自动更新结果，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本** 中打开时，请使用此方法。

### **使用的 API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` 是 `com.aspose.cells.Cell` 上的一个方法，用于将单元格的公式设置为 **动态数组公式**。Excel 对该公式仅求值一次，并自动将结果溢出到周围的单元格中。第三个参数设置为 `True` 时，指示 Aspose.Cells 在写入时也计算结果值。

### **步骤**
1. 使用 `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 通过调用 `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)` 将动态数组公式放在源区域正下方的单元格 **A6** 上。
4. `None` 参数传入默认的 `FormulaParseOptions`，第三个参数 `True` 告诉 Aspose.Cells 将该公式视为动态数组并对其求值，以便将溢出值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 持有公式 `=TRANSPOSE(A1:D5)`，Excel 自动将结果溢出到区域 **A6:D10**，这是一个 5 行 4 列的块，与转置数据相匹配。

{{% alert color="primary" %}}
此方法仅适用于 **Excel 365 / 2021 或更高版本**。较旧版本的 Excel 无法正确溢出动态数组公式。
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# 移植代码如下
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **方法三 — 使用经典数组公式转置 (CSE)**
当您希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能在不支持动态数组溢出的 **较旧 Excel 版本（2021 之前，包括 2019、2016、2013 等）** 中打开时，请使用此方法。经典 CSE（Ctrl+Shift+Enter）数组公式是所有 Excel 版本都能求值的传统兼容替代方案。

### **使用的 API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` 是 `com.aspose.cells.Cell` 上的一个方法，用于为锚定单元格指定 **经典数组（CSE）公式** 并声明结果数组的维度。Aspose.Cells 写入多单元格数组公式标记，以便 Excel 将该公式作为填充所声明区域的单个数组表达式进行求值。

### **步骤**
1. 使用与前面方法相同的方式加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚定单元格，求值后的数组从 A6 开始跨越 4 行 5 列，与 A1:D5 源转置后的维度相匹配。Excel 在结果区域上写入单个数组公式标记，以便较旧版本的 Excel 正确求值。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 求值 `TRANSPOSE` 表达式的经典方式，此方法在所有 Excel 版本中通用兼容。
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# 使用 xlsx LoadOptions 加载源工作簿
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# 访问第一个工作表及其单元格集合
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# 在单元格 A6 上设置经典 CSE 数组公式。
# 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源区域
# 转置为 4 行 x 5 列的数组。第二个参数 (4) 是行数
# 第三个参数 (5) 是结果数组的列数。
# Aspose.Cells 写入 CSE 数组公式标记，以便 Excel 将其作为
# 单个多单元格数组公式进行求值，兼容较旧版本的 Excel
# （2019、2016、2013 等）不支持动态数组溢出。
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# 保存工作簿以使数组公式标记持久化
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **比较 — 何时使用每种方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留源公式？ | 输出区域 |
|------|-----------|-----------|------------------|----------|
| 方法一 — 就地转置 | `Range.transpose()` | 所有 Excel 版本 | 否（仅值） | 相同锚定区域，5×4 |
| 方法二 — 动态数组公式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚定单元格溢出 |
| 方法三 — 经典数组公式 (CSE) | `Cell.setArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式大小，4×5 |
当您需要快速的跨版本转换且只需要将转置后的值写入文件时，请使用 **方法一**。当保证使用现代 Excel，并且希望公式保持活动状态并在源数据更改时进行更新时，请使用 **方法二**。当您需要在每个 Excel 版本（包括不支持动态数组的较旧版本）中以保留公式获得最广泛的兼容性时，请使用 **方法三**。

## **相关文章**
- [SmartMarker 单单元格数组渲染 | Aspose.Cells for Python via Java](/cells/zh/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [将图片插入到单元格中](/cells/zh/python-java/inserting-an-image-into-a-cell/)
- [将 Excel 文件拆分为多个文件](/cells/zh/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}