---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via Java, with three different approaches.
linktitle: Transpose Range
url: /zh/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via Java library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

1. First alert at the top
2. Alert after approach 2
3. Alert after approach 3
Three alert blocks total, each must be balanced (open and close). Got it.
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java 支持通过三种不同的方式转置（旋转）数据，使行变成列、列变成行。第一种方法使用就地调用的 `Range.transpose()` 方法，适用于所有 Excel 版本；第二种使用 `Cell.setDynamicArrayFormula()` 写入现代的动态数组 `=TRANSPOSE(...)` 公式，可在 Excel 365 或 Excel 2021 中自动溢出；第三种使用 `Cell.setArrayFormula()` 写入经典的 Ctrl+Shift+Enter (CSE) 数组公式，兼容旧版 Excel。本文将逐步讲解每种方法并提供完整的代码示例。
{{% /alert %}}

## **简介**
转置区域意味着旋转它，使原本是行的内容变成列，原本是列的内容变成行，实际上是沿主对角线反射数据。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 执行此操作，相关参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。同样的思路也可以以编程方式应用于单元格区域，这在许多业务和报表场景中非常有用。
以下是转置操作常用的应用场景。
- 重新调整季度或年度销售报表的方向，使季度通常横向排列、区域纵向排列，或者反之。
- 在仪表板或图表中切换坐标轴方向，使时间序列纵向而非横向显示。
- 重塑从外部系统导入的数据，使其与下游分析或报表模板所期望的布局相匹配。
为了使本文后面的内容具体化，所有示例都使用以下这张按区域、按季度的小型销售表。在示例工作簿中，该表占据的区域为 **A1:D5**，其中 **A1** 留空作为左上角，**B1:D1** 存放区域标题，**A2:A5** 存放季度标题。
| 区域              | 欧洲      | 亚洲      | 北美        |
|-------------------|-----------|-----------|-------------|
| 第1季度           | 21704714  | 8774099   | 12094215    |
| 第2季度           | 17987034  | 12214447  | 10873099    |
| 第3季度           | 19485029  | 14356879  | 15689543    |
| 第4季度           | 22567894  | 15763492  | 17456723    |
接下来，本文将介绍使用 Aspose.Cells for Node.js via Java 转置此数据的三种不同方式，每种方式适用于不同的 Excel 版本和用例。

## **方法 1 — 就地转置区域 (Range.transpose)**
每当你希望在不涉及 `TRANSPOSE` 工作表函数的情况下转置数据时，可以使用该方法。它适用于**所有版本的 Excel**，并且不依赖于动态数组，因此是兼容性最强的跨版本方案。当你只需要最终的转置结果且不需要在文件中保留原始 `TRANSPOSE` 公式时，它是理想选择。

### **使用的 API**
`Range.transpose()` 是 `com.aspose.cells.Range` 类的一个实例方法。调用它会就地翻转区域，交换其行和列，使原本是行的内容变成列、原本是列的内容变成行。该方法直接修改底层单元格，不会写入任何公式。

### **步骤**
1. 通过 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，并将 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.getWorksheets().get(0)` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.getCells()` 访问工作表的单元格集合。
4. 通过调用 `cells.createRange("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 就地旋转区域，交换行和列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，相同的锚定区域将存放旋转后的数据。第一行读取（空、**欧洲**、**亚洲**、**北美**），第一列读取（空、**第1季度**、**第2季度**、**第3季度**、**第4季度**）。原始的每个销售列变成转置区域中的一行。

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **方法 2 — 使用动态数组公式进行转置 (Excel 365 / 2021)**
当你希望在输出文件中保留 `=TRANSPOSE(A1:D5)` 公式作为活动公式，以便在源数据更改时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开时，可以使用此方法。

### **使用的 API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` 是 `com.aspose.cells.Cell` 类的方法，用于将该单元格的公式设置为**动态数组公式**。Excel 会对该公式进行一次求值，并自动将结果溢出到周围的单元格。第三个参数设置为 `true` 时，会指示 Aspose.Cells 在写入时也计算结果值。

### **步骤**
1. 使用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 通过调用 `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` 在单元格 **A6**（源区域正下方）放置动态数组公式。
4. `null` 参数传入默认的 `FormulaParseOptions`，第三个参数 `true` 告诉 Aspose.Cells 将该公式视为动态数组并对其求值，以便将溢出的值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 存放公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到区域 **A6:D10**，这是一个与转置后数据相等的 5 行 × 4 列的块。

{{% alert color="primary" %}}
此方法仅适用于 **Excel 365 / 2021 或更高版本**。旧版 Excel 无法正确溢出动态数组公式。
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **方法 3 — 使用经典数组公式进行转置 (CSE)**
当你希望在文件中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能在不支持动态数组溢出的**旧版 Excel（2021 之前，包括 2019、2016、2013 等）**中打开时，可以使用此方法。经典的 CSE (Ctrl+Shift+Enter) 数组公式是所有 Excel 版本都能求值的传统兼容替代方案。

### **使用的 API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` 是 `com.aspose.cells.Cell` 类的方法，用于为锚定单元格分配**经典数组 (CSE) 公式**，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，使 Excel 将该公式作为单个数组表达式进行求值，从而填充所声明的区域。

### **步骤**
1. 以与前面方法相同的方式加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚定点，求值后的数组从 A6 开始跨越 4 行 × 5 列，与 A1:D5 源的转置维度相匹配。Excel 会在结果区域写入单个数组公式标记，以便旧版 Excel 能够正确地对其进行求值。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 中求值 `TRANSPOSE` 表达式的经典方式，并且此方法在所有 Excel 版本中均具有通用兼容性。
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// 使用 xlsx LoadOptions 加载源工作簿
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// 访问第一个工作表及其 Cells 集合
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// 在单元格 A6 上设置经典 CSE 数组公式。
// 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源范围旋转为 4 行 x 5 列的数组。
// 第二个参数 (4) 是结果数组的行数，第三个参数 (5) 是结果数组的列数。
// Aspose.Cells 会写入 CSE 数组公式标记，使 Excel 将其作为单一的多单元格数组公式进行求值，
// 以兼容不支持动态数组溢出的旧版 Excel（2019、2016、2013 等）。
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 保存工作簿以持久化数组公式标记
workbook.save("output.xlsx");
```

## **对比 — 何时使用每种方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留源公式 | 输出区域 |
|------|------------|------------|----------------|----------|
| 方法 1 — 就地转置 | `Range.transpose()` | 所有 Excel 版本 | 否（仅值） | 相同锚定区域，5×4 |
| 方法 2 — 动态数组公式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚定单元格溢出 |
| 方法 3 — 经典数组公式 (CSE) | `Cell.setArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式大小，4×5 |
当你需要快速、跨版本的转换，并且只需要将转置后的值写入文件时，请使用**方法 1**。当你确定使用现代 Excel，并且希望公式保持活动状态、在源数据更改时自动更新时，请使用**方法 2**。当你需要在每个 Excel 版本（包括不支持动态数组的旧版本）中保留公式并获得最广泛的兼容性时，请使用**方法 3**。

## **相关文章**
- [SmartMarker 单单元格数组渲染 | Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [在单元格中插入图像](/cells/zh/nodejs-java/inserting-an-image-into-a-cell/)
- [将 Excel 文件拆分为多个文件](/cells/zh/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}