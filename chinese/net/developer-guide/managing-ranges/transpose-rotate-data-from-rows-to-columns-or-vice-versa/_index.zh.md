---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for .NET with three different approaches.
linktitle: 转置区域
url: /zh/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, .NET 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET 支持以三种不同的方式转置（旋转）数据，使行变为列、列变为行。第一种方法是使用 `Range.Transpose()` 方法就地完成转置，适用于所有 Excel 版本；第二种方法使用 `Cell.SetDynamicArrayFormula()` 写入现代动态数组 `=TRANSPOSE(...)` 公式，可在 Excel 365 或 Excel 2021 中自动溢出；第三种方法使用 `Cell.SetArrayFormula()` 写入兼容旧版 Excel 的经典 Ctrl+Shift+Enter（CSE）数组公式。本文将逐步介绍每种方法，并提供完整的代码示例。
{{% /alert %}}

## **简介**
转置区域意味着将其旋转，使原本为行的内容变为列，原本为列的内容变为行，实际上是沿主对角线镜像数据。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 用于执行此操作，相关概念参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。同样的思路可以以编程方式应用于单元格区域，这在许多业务和报表场景中非常有用。
适合使用转置操作的常见场景包括以下几种。
- 调整季度或年度销售报表的方向，例如季度通常横向排列而地区纵向排列，反之亦然。
- 在仪表板或图表中交换坐标轴方向，使时间序列沿页面向下排列而不是横向排列。
- 重新调整从外部系统导入的数据形状，使其符合下游分析或报表模板所预期的布局。
为了让本文后续内容更加具体，所有示例都使用以下这张按地区、按季度划分的销售数据表。在示例工作簿中，该表占用区域 **A1:D5**，其中 **A1** 留空作为左上角，**B1:D1** 放置地区表头，**A2:A5** 放置季度表头。
| 地区            | 欧洲      | 亚洲      | 北美        |
|-----------------|-----------|-----------|-------------|
| 第一季度        | 21704714  | 8774099   | 12094215    |
| 第二季度        | 17987034  | 12214447  | 10873099    |
| 第三季度        | 19485029  | 14356879  | 15689543    |
| 第四季度        | 22567894  | 15763492  | 17456723    |
本文随后将介绍使用 Aspose.Cells for .NET 转置此数据的三种不同方法，每种方法适用于不同的 Excel 版本和用例。

## **方法一 — 就地转置区域（Range.Transpose）**
当您希望在不涉及 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方法。它适用于**所有 Excel 版本**，并且不依赖动态数组，因此是跨版本兼容性最安全的选择。当您只需要最终的转置输出而无需在工作簿中保留原始的 `TRANSPOSE` 公式时，它是理想之选。

### **使用的 API**
`Range.Transpose()` 是 `Aspose.Cells.Range` 类的一个实例方法。调用该方法会就地翻转该区域，交换其行和列，使原本为行的内容变为列，原本为列的内容变为行。该方法直接修改底层单元格，不会写入任何公式。

### **步骤**
1. 通过调用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，其中 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.Worksheets[0]` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.Cells` 访问工作表的单元格集合。
4. 通过调用 `cells.CreateRange("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.Transpose()` 就地旋转该区域，交换行和列。
6. 使用 `workbook.Save(outputFile)` 保存工作簿。
转置后，相同的锚点区域将存放旋转后的数据。第一行变为（空、**欧洲**、**亚洲**、**北美**），第一列变为（空、**第一季度**、**第二季度**、**第三季度**、**第四季度**）。每个原本的销售列都会成为转置区域中对应的一行。

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **方法二 — 使用动态数组公式进行转置（Excel 365 / 2021）**
当您希望将 `=TRANSPOSE(A1:D5)` 公式作为活动公式保留在输出工作簿中，以便源数据更改时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本** 中打开时，请使用此方法。

### **使用的 API**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` 是 `Aspose.Cells.Cell` 类的一个方法，用于将单元格的公式设置为**动态数组公式**。Excel 只会计算该公式一次，然后将结果自动溢出到周围的单元格中。第三个参数设置为 `true` 时，会指示 Aspose.Cells 在写入时一并计算结果值。

### **步骤**
1. 使用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 通过调用 `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` 在单元格 **A6**（源区域正下方）放置动态数组公式。
4. `null` 参数使用默认的 `FormulaParseOptions`，第三个参数 `true` 告诉 Aspose.Cells 将该公式视为动态数组并对其求值，以便将溢出值写入工作簿。
5. 使用 `workbook.Save(outputFile)` 保存工作簿。
单元格 **A6** 保存公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到区域 **A6:E9**，即 4 行 5 列的块，与转置后的数据一致。

{{% alert color="primary" %}}
此方法**仅适用于 Excel 365 / 2021 或更高版本**。旧版 Excel 无法正确地溢出动态数组公式。
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **方法三 — 使用经典数组公式（CSE）进行转置**
当您希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能会在**不支持动态数组溢出的旧版 Excel（2021 之前的版本，包括 2019、2016、2013 等）** 中打开时，请使用此方法。经典 CSE（Ctrl+Shift+Enter）数组公式是所有 Excel 版本都可计算的旧式兼容方案。

### **使用的 API**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` 是 `Aspose.Cells.Cell` 类的一个方法，用于将**经典数组（CSE）公式**分配给锚点单元格，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，以便 Excel 作为一个数组表达式计算该公式并填充到所声明的区域。

### **步骤**
1. 以与前面方法相同的方式加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.Save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点，计算后的数组从 A6 开始横跨 4 行 5 列，与源区域 A1:D5 的转置维度一致。Excel 会在结果区域上写入单个数组公式标记，使旧版 Excel 也能正确地计算该公式。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 中计算 `TRANSPOSE` 表达式的经典方式，此方法在所有 Excel 版本中都具有通用兼容性。
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// 使用 xlsx LoadOptions 加载源工作簿
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// 访问第一个工作表及其单元格集合
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// 在单元格 A6 上设置经典的 CSE 数组公式
// 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源区域
// 旋转为 4 行 x 5 列的数组。第二个参数 (4) 是行数
// 第三个参数 (5) 是结果数组的列数。
// Aspose.Cells 写入 CSE 数组公式标记，以便 Excel 将其作为
// 单个多单元格数组公式进行计算，兼容不支持动态数组溢出的旧版 Excel
// (2019、2016、2013 等)。
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 保存工作簿，以便数组公式标记被持久化
workbook.Save("output.xlsx");
```

## **对比 — 何时使用每种方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留源公式 | 输出区域 |
|------|------------|------------|----------------|----------|
| 方法一 — 就地转置 | `Range.Transpose()` | 所有 Excel 版本 | 否（仅数值） | 相同锚点区域，5×4 |
| 方法二 — 动态数组公式 | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点溢出 |
| 方法三 — 经典数组公式（CSE） | `Cell.SetArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式大小，4×5 |
当您需要快速、跨版本的转换，并且只需要将转置后的数值写入文件时，请使用**方法一**。当确定使用现代 Excel，并且希望公式保持活动状态以便在源数据更改时自动更新时，请使用**方法二**。当您需要在所有 Excel 版本（包括不支持动态数组的旧版本）中保留公式并获得最广泛的兼容性时，请使用**方法三**。

## **相关文章**
- [SmartMarker 单单元格数组渲染 | Aspose.Cells .NET](/cells/zh/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [在单元格中插入图像](/cells/zh/net/inserting-an-image-into-a-cell/)
- [将 Excel 文件拆分为多个文件](/cells/zh/net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="csharp" >}}