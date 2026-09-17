---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Java, with three different approaches.
linktitle: 转置区域
url: /zh/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Java 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java 支持以三种不同方式转置（旋转）数据，使行变为列、列变为行。第一种方法使用就地调用的 `Range.transpose()` 方法，适用于所有 Excel 版本；第二种方法使用 `Cell.setDynamicArrayFormula()` 写入现代动态数组 `=TRANSPOSE(...)` 公式，可在 Excel 365 或 Excel 2021 中自动溢出；第三种方法使用 `Cell.setArrayFormula()` 写入经典的 Ctrl+Shift+Enter（CSE）数组公式，可兼容旧版 Excel。本文将逐步介绍每种方法，并提供完整的代码示例。
{{% /alert %}}

## **简介**
转置区域是指将其旋转，使原来的行变为列、原来的列变为行，实际上是沿主对角线对数据进行镜像。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 可执行此操作，相关概念参考见 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。同样的思路也可以通过编程方式应用于单元格区域，这在许多业务和报表场景中都很有用。
转置常用的场景包括以下几种。
- 调整季度或年度销售报表的方向——报表中季度通常沿页面横向排列、地区纵向排列（或相反）。
- 切换仪表板或图表中的坐标轴方向，使时间序列沿页面纵向排列而非横向排列。
- 重新塑形从外部系统导入的数据，使其与下游分析或报表模板所期望的布局相匹配。
为使后续内容具体化，所有示例均使用下面这张按地区、按季度统计的销售小表。在示例工作簿中，该表占据 **A1:D5** 区域，其中 **A1** 留空作为左上角，**B1:D1** 存放地区标题，**A2:A5** 存放季度标题。
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
随后，本文将介绍使用 Aspose.Cells for Java 转置此数据的三种不同方法，每种方法适用于不同的 Excel 版本和使用场景。

## **方法一 —— 就地转置区域（Range.transpose）**
当你希望在不涉及 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方法。它适用于**所有 Excel 版本**，且不依赖动态数组，因此是兼容性最强的跨版本选项。当你只需要最终的转置结果，而不需要在工作簿中保留原始的 `TRANSPOSE` 公式时，它是理想之选。

### **使用的 API**
`Range.transpose()` 是 `com.aspose.cells.Range` 类上的实例方法。调用此方法会原地翻转区域，交换其行和列——原来的行变为列、原来的列变为行。该方法直接修改底层单元格，不会写入任何公式。

### **步骤**
1. 通过调用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，其中 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.getWorksheets().get(0)` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.getCells()` 访问工作表的单元格集合。
4. 通过调用 `cells.createRange("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 原地旋转区域，交换行和列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，相同的锚定区域持有旋转后的数据。第一行内容为（空、**Europe**、**Asia**、**North America**），第一列内容为（空、**Qtr 1**、**Qtr 2**、**Qtr 3**、**Qtr 4**）。原来的每一列销售数据成为转置区域中的一行。

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **方法二 —— 使用动态数组公式转置（Excel 365 / 2021）**
当你希望在输出工作簿中保留 `=TRANSPOSE(A1:D5)` 公式作为实时公式，以便在源数据更改时结果自动更新，并且目标 Excel 文件将在支持动态数组与溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开时，请使用此方法。

### **使用的 API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` 是 `com.aspose.cells.Cell` 上的方法，用于将该单元格的公式设置为**动态数组公式**。Excel 仅评估该公式一次，并将结果自动溢出到周围的单元格中。当第三个参数设置为 `true` 时，会指示 Aspose.Cells 在写入时也计算结果值。

### **步骤**
1. 使用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 通过调用 `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`，将动态数组公式放置在源区域正下方的 **A6** 单元格上。
4. `null` 参数传入默认的 `FormulaParseOptions`，第三个参数 `true` 告诉 Aspose.Cells 将该公式视为动态数组并进行评估，以便将溢出后的值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 持有公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到 **A6:D10** 区域——一个 5 行 4 列的块，等于转置后的数据。

{{% alert color="primary" %}}
此方法仅适用于 **Excel 365 / 2021 或更高版本**。旧版 Excel 无法正确溢出动态数组公式。
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **方法三 —— 使用经典数组公式（CSE）转置**
当你希望在输出工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能在不支持动态数组溢出的**旧版 Excel（2021 之前的版本，包括 2019、2016、2013 等）**中打开时，请使用此方法。经典 CSE（Ctrl+Shift+Enter）数组公式是所有 Excel 版本都能评估的向后兼容替代方案。

### **使用的 API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` 是 `com.aspose.cells.Cell` 上的方法，用于将**经典数组（CSE）公式**分配给锚定单元格，并声明结果数组的维度。Aspose.Cells 写入多单元格数组公式标记，使 Excel 将该公式作为填充所声明区域的单一数组表达式进行评估。

### **步骤**
1. 以与前面方法相同的方式加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点，评估后的数组从 A6 起跨越 4 行 5 列，与 A1:D5 源区域的转置维度相匹配。Excel 在结果区域内写入单个数组公式标记，使旧版 Excel 也能正确对其进行评估。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 评估 `TRANSPOSE` 表达式的经典方式，此方法在所有 Excel 版本中均可通用。
{{% /alert %}}

```java
import com.aspose.cells.*;
// 使用 xlsx LoadOptions 加载源工作簿
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// 访问第一个工作表及其单元格集合
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// 在 A6 单元格上设置经典 CSE 数组公式
// 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源区域
// 旋转为 4 行 x 5 列的数组。第二个参数 (4) 是行数
// 第三个参数 (5) 是结果数组的列数
// Aspose.Cells 写入 CSE 数组公式标记，以便 Excel 将其作为
// 单个多单元格数组公式进行计算，兼容较旧的 Excel 版本
// (2019、2016、2013 等) 不支持动态数组溢出
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 保存工作簿以使数组公式标记持久化
workbook.save("output.xlsx");
```

## **对比 —— 何时使用各方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留源公式？ | 输出区域 |
|----------|--------------|---------------|--------------------------|--------------|
| 方法一 —— 就地转置 | `Range.transpose()` | 所有 Excel 版本 | 否（仅保留值） | 同一锚定区域，5×4 |
| 方法二 —— 动态数组公式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚定位置溢出 |
| 方法三 —— 经典数组公式（CSE） | `Cell.setArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式尺寸，4×5 |
当你需要快速、跨版本的转换，并且只需要将转置后的值写入文件时，请使用**方法一**。当现代 Excel 可用且希望公式保持实时、并能在源数据变化时自动更新时，请使用**方法二**。当你需要在所有 Excel 版本（包括不支持动态数组的旧版本）中获得最广泛的公式兼容性时，请使用**方法三**。

## **相关文章**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/zh/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/zh/java/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/zh/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}