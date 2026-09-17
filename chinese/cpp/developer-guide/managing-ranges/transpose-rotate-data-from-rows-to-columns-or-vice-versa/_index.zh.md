---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for C++ with three different approaches.
linktitle: 转置区域
url: /zh/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, C++ 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ 支持以三种不同的方式对数据进行转置（旋转），使行变为列、列变为行。第一种方式使用就地（原地）的 `Range.Transpose()` 方法，兼容所有 Excel 版本；第二种方式使用 `Cell.SetDynamicArrayFormula()` 写入现代动态数组公式 `=TRANSPOSE(...)`，可在 Excel 365 或 Excel 2021 中自动溢出；第三种方式使用 `Cell.SetArrayFormula()` 写入兼容旧版 Excel 的经典 Ctrl+Shift+Enter (CSE) 数组公式。本文将通过分步说明和完整的代码示例逐一介绍这三种方式。
{{% /alert %}}

## **简介**
所谓转置区域，就是将其旋转，使得原本的行变为列、原本的列变为行，实际上就是将数据沿主对角线进行翻转。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 用于执行此操作，其概念参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。同样的思路也可应用于对单元格区域进行编程操作，这在许多业务和报表场景中都非常实用。
以下是一些常见的适合使用转置的场景。
- 调整季度或年度销售报表的方向：通常情况下，季度沿页面横向排列、地区沿纵向排列，反之亦然，此时需要交换两者的方向。
- 在仪表板或图表中切换坐标轴方向，使时间序列沿纵向排列而非横向排列。
- 对从外部系统导入的数据进行重塑，使其与下游分析或报表模板所要求的布局一致。
为了让后续内容更加具体，本文所有示例都使用下面这张按地区、按季度划分的小型销售表。在示例工作簿中，此表占据的区域为 **A1:D5**，其中 **A1** 留空作为左上角，**B1:D1** 存放地区表头，**A2:A5** 存放季度表头。
| 地区             | 欧洲        | 亚洲        | 北美         |
|------------------|-------------|-------------|--------------|
| 第 1 季度        | 21704714    | 8774099     | 12094215     |
| 第 2 季度        | 17987034    | 12214447    | 10873099     |
| 第 3 季度        | 19485029    | 14356879    | 15689543     |
| 第 4 季度        | 22567894    | 15763492    | 17456723     |
接下来，本文将介绍使用 Aspose.Cells for C++ 对此数据进行转置的三种不同方式，每种方式分别适用于不同的 Excel 版本和用例。

## **方式 1 — 就地转置区域（Range.Transpose）**
当您希望在不涉及 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方式。它兼容**所有 Excel 版本**，且不依赖动态数组功能，因此是跨版本兼容性最安全的选择。当您只需要最终的转置结果而不需要在工作簿中保留原始的 `TRANSPOSE` 公式时，此方式最为理想。

### **使用的 API**
`Range.Transpose()` 是 `Aspose.Cells.Range` 类上的实例方法。调用该方法会就地翻转该区域，交换其行和列，使原本的行变为列、原本的列变为行。该方法会直接修改底层单元格，而不会写入任何公式。

### **步骤**
1. 通过创建 `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` 来打开源工作簿，其中 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.GetWorksheets().Get(0)` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.GetCells()` 访问该工作表的单元格集合。
4. 调用 `cells.CreateRange(u"A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.Transpose()` 就地旋转该区域，交换行和列。
6. 使用 `workbook.Save(outputFile)` 保存工作簿。
转置之后，同一锚点区域中将存放旋转后的数据。第一行变为（空、**欧洲**、**亚洲**、**北美**），第一列变为（空、**第 1 季度**、**第 2 季度**、**第 3 季度**、**第 4 季度**）。原始的每一列销售数据在转置后的区域中都变为一行。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **方式 2 — 使用动态数组公式进行转置（Excel 365 / 2021）**
当您希望将 `=TRANSPOSE(A1:D5)` 公式作为活动公式保留在输出工作簿中，以便在源数据发生变化时结果能够自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开时，请使用此方式。

### **使用的 API**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` 是 `Aspose.Cells.Cell` 上的一个方法，用于将该单元格的公式设置为**动态数组公式**。Excel 只会计算该公式一次，并将结果自动溢出到周围的单元格中。第三个参数在设置为 `true` 时，会指示 Aspose.Cells 在写入时同时计算结果值。

### **步骤**
1. 通过构造 `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` 加载源工作簿。
2. 通过 `workbook.GetWorksheets().Get(0)` 获取第一个工作表，并通过 `worksheet.GetCells()` 访问其 `Cells` 集合。
3. 通过调用 `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`，在源区域正下方的 **A6** 单元格上设置动态数组公式。
4. `nullptr` 参数传入默认的 `FormulaParseOptions`，第三个参数 `true` 则告诉 Aspose.Cells 将此公式视为动态数组并对其求值，以便将溢出后的值写入工作簿。
5. 使用 `workbook.Save(outputFile)` 保存工作簿。
**A6** 单元格中保存公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到 **A6:D10** 区域，即一个 5 行 4 列、与转置后数据一致的块。

{{% alert color="primary" %}}
此方式**仅适用于 Excel 365 / 2021 或更高版本**。旧版 Excel 无法正确溢出动态数组公式。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **方式 3 — 使用经典数组公式（CSE）进行转置**
当您希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能会在不支持动态数组溢出的**旧版 Excel（2021 之前的版本，包括 2019、2016、2013 等）**中打开时，请使用此方式。经典 CSE（Ctrl+Shift+Enter）数组公式是兼容旧版的替代方案，所有 Excel 版本都可以对其求值。

### **使用的 API**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` 是 `Aspose.Cells.Cell` 上的一个方法，用于将**经典数组（CSE）公式**分配给锚点单元格，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，以便 Excel 将该公式作为填充所声明区域的单一数组表达式进行求值。

### **步骤**
1. 与前面几种方式相同，通过构造 `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` 加载源工作簿。
2. 通过 `workbook.GetWorksheets().Get(0)` 获取第一个工作表，并通过 `worksheet.GetCells()` 访问其 `Cells` 集合。
3. 调用 `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
4. 使用 `workbook.Save(outputFile)` 保存工作簿。
**A6** 是数组公式的锚点单元格，求值后的数组从 A6 开始跨越 4 行 5 列，与 A1:D5 源区域转置后的维度一致。Excel 会在结果区域范围内写入一个统一的数组公式标记，以便旧版 Excel 能够正确地对其求值。

{{% alert color="primary" %}}
CSE 数组公式是对 `TRANSPOSE` 表达式求值的经典 Excel 方式，此方式在所有 Excel 版本中都具有普遍兼容性。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 使用 xlsx LoadOptions 加载源工作簿
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // 访问第一个工作表及其单元格集合
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // 在单元格 A6 上设置经典的 CSE 数组公式。
    // 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源范围
    // 旋转为 4 行 x 5 列的数组。第二个参数 (4) 是结果数组的行数,
    // 第三个参数 (5) 是结果数组的列数。
    // Aspose.Cells 会写入 CSE 数组公式标记,以便 Excel
    // 将其作为单一的多单元格数组公式进行计算,
    // 从而兼容不支持动态数组溢出的旧版 Excel
    // (2019、2016、2013 等)。
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // 保存工作簿以持久化数组公式标记
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **对比 — 何时使用每种方式**
| 方式 | API / 方法 | Excel 版本 | 是否保留源公式 | 输出区域 |
|------|------------|------------|----------------|----------|
| 方式 1 — 就地转置 | `Range.Transpose()` | 所有 Excel 版本 | 否（仅写入值） | 同一锚点区域，5×4 |
| 方式 2 — 动态数组公式 | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点溢出 |
| 方式 3 — 经典数组公式（CSE） | `Cell.SetArrayFormula` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式大小，4×5 |
当您需要快速、跨版本的转换，并且只需要将转置后的值写入文件时，请使用**方式 1**。当能够确保使用现代 Excel，并且希望公式保持活动状态、在源数据发生变化时能够自动更新时，请使用**方式 2**。当您需要在所有 Excel 版本（包括不支持动态数组的旧版本）上保留公式并获得最广泛的兼容性时，请使用**方式 3**。

## **相关文章**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/zh/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/zh/cpp/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/zh/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}