---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
linktitle: 转置区域
url: /zh/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via C++ 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ 支持以三种不同的方式转置（旋转）数据，使行变成列、列变成行。第一种方式使用就地调用的 `range.transpose()` 方法，适用于所有 Excel 版本；第二种使用 `cell.setDynamicArrayFormula()` 写入现代的动态数组 `=TRANSPOSE(...)` 公式，可在 Excel 365 或 Excel 2021 中自动溢出；第三种使用 `cell.setArrayFormula()` 写入兼容旧版 Excel 的经典 Ctrl+Shift+Enter（CSE）数组公式。本文将逐步讲解每种方式，并提供完整的代码示例。
{{% /alert %}}

## **简介**
转置区域是指对其进行旋转，使原本的行变为列、原本的列变为行，从而沿着主对角线镜像数据。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 用于执行此操作，其概念参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。同样的思路也可以通过编程方式应用于单元格区域，这在许多业务和报表场景中非常有用。
以下列举了转置操作有用的常见场景。
- 调整季度或年度销售报表的方向，例如季度通常横向排列、区域纵向排列，反之亦然。
- 切换仪表板或图表中的坐标轴方向，使时间序列纵向排列而非横向排列。
- 重新调整从外部系统导入的数据形状，使其匹配下游分析或报表模板所期望的布局。
为了使后续内容具体化，所有示例都使用下面这个按区域和季度划分的销售表。在示例工作簿中，该表占据 **A1:D5** 区域，其中 **A1** 留空作为左上角，**B1:D1** 存放区域标题，**A2:A5** 存放季度标题。
| 区域             | Europe    | Asia      | North America |
|------------------|-----------|-----------|---------------|
| 第一季度         | 21704714  | 8774099   | 12094215      |
| 第二季度         | 17987034  | 12214447  | 10873099      |
| 第三季度         | 19485029  | 14356879  | 15689543      |
| 第四季度         | 22567894  | 15763492  | 17456723      |
接下来本文将介绍使用 Aspose.Cells for Node.js via C++ 转置此数据的三种不同方式，每种方式分别适用于不同的 Excel 版本和用例。

## **方式一 — 就地转置区域（range.transpose）**
当您希望在不使用 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方式。它适用于**所有版本的 Excel**，不依赖动态数组，因此是跨版本兼容性最安全的选择。当您只需要最终的转置结果而无需在工作簿中保留原始的 `TRANSPOSE` 公式时，此方式最为理想。

### **使用的 API**
`range.transpose()` 是 `Aspose.Cells.Range` 类的一个实例方法。调用该方法会就地翻转该区域，交换其行和列，使原本的行变为列、原本的列变为行。该方法直接修改底层单元格，而不会写入任何公式。

### **步骤**
1. 通过调用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，并将 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.getWorksheets().get(0)` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.getCells()` 访问工作表的单元格集合。
4. 调用 `cells.createRange("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 就地旋转该区域，交换行和列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，相同的锚定区域将保存旋转后的数据。第一行变为（空、**Europe**、**Asia**、**North America**），第一列变为（空、**第一季度**、**第二季度**、**第三季度**、**第四季度**）。每个原始的销售列都成为转置区域中的一行。

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **方式二 — 使用动态数组公式进行转置（Excel 365 / 2021）**
当您希望在输出工作簿中保留 `=TRANSPOSE(A1:D5)` 公式作为活动公式，以便在源数据变化时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开时，请使用此方式。

### **使用的 API**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` 是 `Aspose.Cells.Cell` 的一个方法，用于将该单元格的公式设置为**动态数组公式**。Excel 会对该公式进行一次求值，并将结果自动溢出到周围的单元格中。第三个参数设置为 `true` 时，会指示 Aspose.Cells 在写入时同时计算生成的值。

### **步骤**
1. 使用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 通过调用 `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`，将动态数组公式置于源区域正下方的 **A6** 单元格。
4. `null` 参数传入默认的 `FormulaParseOptions`，第三个参数 `true` 告诉 Aspose.Cells 将该公式视为动态数组并进行求值，以便将溢出的值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
**A6** 单元格保存公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到 **A6:D10** 区域，即一个 5 行 4 列、等于转置数据的块。

{{% alert color="primary" %}}
此方式**仅适用于 Excel 365 / 2021 或更高版本**。较旧版本的 Excel 无法正确溢出动态数组公式。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **方式三 — 使用经典数组公式进行转置（CSE）**
当您希望在工作中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能会在不支持动态数组溢出的**较旧版本 Excel（2021 之前的版本，包括 2019、2016、2013 等）**中打开时，请使用此方式。经典 CSE（Ctrl+Shift+Enter）数组公式是所有 Excel 版本都能求值的、向后兼容的替代方案。

### **使用的 API**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` 是 `Aspose.Cells.Cell` 的一个方法，用于将**经典数组（CSE）公式**分配给锚定单元格，并声明所生成数组的维度。Aspose.Cells 会写入多单元格数组公式标记，以便 Excel 将该公式作为填充到所声明区域的单一数组表达式进行求值。

### **步骤**
1. 以与前面方式相同的方式加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
**A6** 单元格是数组公式的锚点，求值后的数组从 A6 开始跨越 4 行 5 列，与 A1:D5 源区域的转置维度相匹配。Excel 会在结果区域上写入一个数组公式标记，以便较旧版本的 Excel 能够正确求值。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 求值 `TRANSPOSE` 表达式的经典方式，此方式在所有 Excel 版本中具有普遍兼容性。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// 使用 xlsx LoadOptions 加载源工作簿
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// 访问第一个工作表及其 Cells 集合
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// 在 A6 单元格设置经典的 CSE 数组公式
// 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源范围
// 转换为 4 行 x 5 列的数组。第二个参数 (4) 是结果数组的行数
// 第三个参数 (5) 是结果数组的列数
// Aspose.Cells 写入 CSE 数组公式标记，以便 Excel 将其作为
// 单个多单元格数组公式进行计算，兼容旧版 Excel
// （2019、2016、2013 等）不支持动态数组溢出
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 保存工作簿以使数组公式标记持久化
workbook.save("output.xlsx");
```

## **对比 — 各方式的适用场景**
| 方式 | API / 方法 | Excel 版本 | 是否保留源公式 | 输出区域 |
|------|------------|------------|----------------|----------|
| 方式一 — 就地转置 | `range.transpose()` | 所有 Excel 版本 | 否（仅值） | 同一锚定区域，5×4 |
| 方式二 — 动态数组公式 | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点溢出 |
| 方式三 — 经典数组公式（CSE） | `cell.setArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式大小，4×5 |
当您需要快速、跨版本的转换，并且只需要将转置后的值写入文件时，请使用**方式一**。当可以保证使用较新版本的 Excel，并且希望公式保持活动状态以便在源数据变化时自动更新时，请使用**方式二**。当您需要在每个 Excel 版本（包括不支持动态数组的旧版本）中获得最广泛的兼容性并保留公式时，请使用**方式三**。

## **相关文章**
- [SmartMarker 单单元格数组渲染](/cells/zh/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [在单元格中插入图像](/cells/zh/nodejs-cpp/inserting-an-image-into-a-cell/)
- [将 Excel 文件拆分为多个文件](/cells/zh/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}