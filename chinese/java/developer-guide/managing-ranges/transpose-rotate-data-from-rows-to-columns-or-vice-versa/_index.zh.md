---
title: 转置区域
linktitle: 转置区域
description: 本文介绍如何使用 Aspose.Cells for Java，通过三种不同的方法在 Excel 文件中将数据从行转置为列，或从列转置为行。
keywords: Aspose.Cells, Java 库, 电子表格, 转置区域, 旋转数据, TRANSPOSE 函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 从行到列
type: docs
weight: 80
url: /zh/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java 支持以三种不同方式转置（旋转）数据，使行变为列、列变为行。第一种方式使用原地的 `Range.transpose()` 方法，适用于所有 Excel 版本；第二种方式使用 `Cell.setDynamicArrayFormula()` 写入现代动态数组公式 `=TRANSPOSE(...)`，该公式会在 Excel 365 或 Excel 2021 中自动溢出。第三种方式使用 `Cell.setArrayFormula()` 写入经典 Ctrl+Shift+Enter (CSE) 数组公式，兼容较早的 Excel 版本。本文将逐步介绍每种方式，并提供完整的代码示例。
{{% /alert %}}

## **简介**
转置区域是指旋转该区域，使原来的行变为列、原来的列变为行，这相当于以主对角线为轴对数据进行翻转。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 可执行此操作。有关概念参考，请参阅 [Microsoft Excel 中的 `TRANSPOSE` 函数文档](https://support.microsoft.com/en-us/excel/functions/transpose-function)。可以在程序中将此概念应用于单元格区域，这在许多业务和报表场景中非常有用。
- 对通常按页面横向排列季度、按纵向排列区域的季度或年度销售报告重新定向，或执行相反操作。
- 在仪表板或图表中切换坐标轴方向，使时间序列沿页面纵向而非横向排列。
- 重塑从外部系统导入的数据，使其符合下游分析或报表模板所期望的布局。
为使本文其余内容更具体，每个示例都使用以下按区域和季度展示销售额的小型表格。在示例工作簿中，该表格位于单元格区域 **A1:D5**，其中 **A1** 作为左上角单元格保持为空，**B1:D1** 包含区域标题，**A2:A5** 包含季度标题。
| 区域       | 欧洲     | 亚洲     | 北美洲   |
|------------|----------|----------|----------|
| 第 1 季度  | 21704714 | 8774099  | 12094215 |
| 第 2 季度  | 17987034 | 12214447 | 10873099 |
| 第 3 季度  | 19485029 | 14356879 | 15689543 |
| 第 4 季度  | 22567894 | 15763492 | 17456723 |
随后，本文将介绍使用 Aspose.Cells for Java 转置此数据的三种不同方式，每种方式分别适用于不同的 Excel 版本和使用场景。

## **方式 1 — 原地转置区域（Range.transpose）**
如果需要在不涉及 `TRANSPOSE` 工作表函数的情况下转置数据，请使用此方式。它适用于**所有 Excel 版本**，不依赖动态数组，因此是跨版本兼容性最有保障的选项。如果只需要最终的转置结果，并且不需要在工作簿中保留原始 `TRANSPOSE` 公式，则此方式非常适合。

### **使用的 API**
`Range.transpose()` 是 `com.aspose.cells.Range` 类上的实例方法。调用该方法会原地翻转区域，通过交换行和列，使原来的行变为列、原来的列变为行。该方法直接修改底层单元格，而不写入公式。

### **步骤**
1. 调用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 打开源工作簿，并通过 `LoadOptions` 指定 `.xlsx` 格式。
2. 通过 `workbook.getWorksheets().get(0)` 获取工作簿中的第一个工作表。
3. 通过 `worksheet.getCells()` 访问该工作表的单元格集合。
4. 调用 `cells.createRange("A1:D5")` 创建涵盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 原地旋转该区域，交换行和列。
6. 通过 `workbook.save(outputFile)` 保存工作簿。
转置后，初始锚定区域将包含旋转后的数据。第一行的内容为（空、**欧洲**、**亚洲**、**北美洲**），第一列的内容为（空、**第 1 季度**、**第 2 季度**、**第 3 季度**、**第 4 季度**）。原表中的每个销售数据列都会变为转置区域中的一行。

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
Range source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **方式 2 — 使用动态数组公式转置（Excel 365 / 2021）**
如果希望将 `=TRANSPOSE(A1:D5)` 公式作为动态公式保留在输出工作簿中，以便源数据发生变化时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开，请使用此方式。

### **使用的 API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` 是 `com.aspose.cells.Cell` 类上的方法，用于将单元格的公式设置为**动态数组公式**。Excel 会对该公式求值一次，然后自动将结果溢出到周边单元格。第三个参数设为 `true` 时，会指示 Aspose.Cells 在写入时也计算生成的值。

### **步骤**
1. 使用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`，将动态数组公式设置在源区域正下方的单元格 **A6** 中。
4. 参数 `null` 用于采用默认的 `FormulaParseOptions`；第三个参数 `true` 指示 Aspose.Cells 将该公式视为动态数组并对其进行求值，从而将溢出值写入工作簿。
5. 通过 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 包含公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到区域 **A6:D10**。该区域是一个 5 行 × 4 列的区块，与转置后的数据相对应。

{{% alert color="primary" %}}
此方式**仅适用于 Excel 365 / 2021 或更高版本**。较早的 Excel 版本无法正确溢出动态数组公式。
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

## **方式 3 — 使用经典数组公式转置（CSE）**
如果希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能会在不支持动态数组溢出的**较早 Excel 版本（2021 之前，包括 2019、2016、2013 等）**中打开，请使用此方式。经典 CSE (Ctrl+Shift+Enter) 数组公式是一种向后兼容的替代方案，所有 Excel 版本均可对其进行计算。

### **使用的 API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` 是 `com.aspose.cells.Cell` 类上的方法，用于向锚点单元格指定**经典数组 (CSE) 公式**，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，使 Excel 将该公式作为单个数组表达式进行计算，并填充所声明的区域。

### **步骤**
1. 如前述方式所述，加载源工作簿。
2. 获取第一个工作表并访问其 `Cells` 集合。
3. 调用 `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 通过 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点，计算得到的数组从 A6 开始横跨 4 行 × 5 列，与 A1:D5 源区域转置后的维度相对应。Excel 会在整个结果区域中写入单个数组公式标记，使较早的 Excel 版本能够正确对其进行计算。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 对 `TRANSPOSE` 表达式进行计算的经典方式，此方式兼容所有 Excel 版本。
{{% /alert %}}

```java
import com.aspose.cells.*;
// 使用 xlsx LoadOptions 加载源工作簿
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// 访问第一个工作表及其 Cells 集合
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// 在 A6 单元格上设置经典 CSE 数组公式。
// 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源范围转换为
// 4 行 x 5 列的数组。第二个参数（4）是结果数组的行数，
// 第三个参数（5）是结果数组的列数。
// Aspose.Cells 会写入 CSE 数组公式标记，使 Excel 将其作为
// 单个多单元格数组公式进行求值，并兼容不支持动态数组溢出的
// 旧版 Excel（2019、2016、2013 等）。
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 保存工作簿，以持久保存数组公式标记
workbook.save("output.xlsx");
```

## **比较 — 各种方式的适用场景**
| 方式 | API / 方法 | Excel 版本 | 是否保留源公式？ | 输出区域 |
|------|------------|------------|------------------|----------|
| 方式 1 — 原地转置 | `Range.transpose()` | 所有 Excel 版本 | 否（仅值） | 初始锚定区域，5×4 |
| 方式 2 — 动态数组公式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点开始溢出 |
| 方式 3 — 经典数组公式 (CSE) | `Cell.setArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 明确指定大小，4×5 |
如果只需快速完成跨版本转换，并且只需要将转置后的值写入文件，请使用**方式 1**。如果可以确保使用现代 Excel，并希望公式保持动态且在源数据变化时自动更新，请使用**方式 2**。如果需要在所有 Excel 版本中保留公式并获得最广泛的兼容性，包括不支持动态数组的较早版本，请使用**方式 3**。

## **相关文章**
- [智能标记单单元格数组呈现 | Aspose.Cells for Java](/cells/zh/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [将图像插入单元格](/cells/zh/java/inserting-an-image-into-a-cell/)
- [将 Excel 文件拆分为多个文件](/cells/zh/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}