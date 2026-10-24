---
title: 转置区域
description: 本文介绍如何使用 Aspose.Cells for C++ 采用三种不同的方法，将 Excel 文件中的数据从行转置或旋转为列，或反之。
linktitle: 转置区域
url: /zh/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, C++ 库, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行转列
type: docs
weight: 80
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ 支持通过三种不同方式对数据进行转置（旋转），使行变为列、列变为行。第一种方式使用就地 `Range.Transpose()` 方法，适用于所有 Excel 版本；第二种方式使用 `Cell.SetDynamicArrayFormula()` 写入现代动态数组公式 `=TRANSPOSE(...)`，该公式会在 Excel 365 或 Excel 2021 中自动溢出。第三种方式使用 `Cell.SetArrayFormula()` 写入经典 Ctrl+Shift+Enter (CSE) 数组公式，与较旧的 Excel 版本兼容。本文将逐步介绍每种方式，并提供完整的代码示例。
{{% /alert %}}

## **简介**
对区域进行转置意味着对其进行旋转，使原来的行变为列、原来的列变为行，实际上就是沿主对角线反射数据。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 可执行此操作，相关概念参考文档见 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。可以在程序中将此概念应用于单元格区域，这在许多业务和报表场景中都很有用。
- 重新调整季度或年度销售报表的方向，使季度通常沿页面横向排列、区域沿页面纵向排列，或反之。
- 在仪表板或图表中交换坐标轴方向，使时间序列沿页面纵向而非横向排列。
- 重新组织从外部系统导入的数据，使其符合下游分析或报表模板所期望的布局。
为使本文后续内容更具体，每个示例都使用以下按区域和季度划分的小型销售数据表。在示例工作簿中，该表占据区域 **A1:D5**，其中左上角的 **A1** 保持为空，**B1:D1** 存放区域标题，**A2:A5** 存放季度标题。
| 区域             | 欧洲       | 亚洲       | 北美洲     |
|------------------|-----------|-----------|-----------|
| 第一季度         | 21704714  | 8774099   | 12094215  |
| 第二季度         | 17987034  | 12214447  | 10873099  |
| 第三季度         | 19485029  | 14356879  | 15689543  |
| 第四季度         | 22567894  | 15763492  | 17456723  |
随后，本文将介绍使用 Aspose.Cells for C++ 转置这些数据的三种不同方式，每种方式适用于不同的 Excel 版本和使用场景。

## **方法 1 — 原地转置区域 (Range.Transpose)**
如果希望在不调用 `TRANSPOSE` 工作表函数的情况下转置数据，请使用此方式。它适用于**所有 Excel 版本**，且不依赖动态数组，因此是跨版本兼容性最稳妥的选项。如果只需要最终的转置结果，并不需要在工作簿中保留原始 `TRANSPOSE` 公式，此方式非常适合。

### **使用的 API**
`Range.Transpose()` 是 `Aspose.Cells.Range` 类的实例方法。调用该方法会就地翻转区域，交换其中的行和列，使原来的行变为列、原来的列变为行。该方法直接修改底层单元格，而不写入公式。

### **步骤**
1. 通过创建 `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` 打开源工作簿，并将 `LoadOptions` 设置为 `.xlsx` 格式。
2. 使用 `workbook.GetWorksheets().Get(0)` 从工作簿中获取第一个工作表。
3. 通过 `worksheet.GetCells()` 访问工作表的单元格集合。
4. 调用 `cells.CreateRange(u"A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.Transpose()` 就地旋转该区域，交换行和列。
6. 使用 `workbook.Save(outputFile)` 保存工作簿。

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

## **方法 2 — 使用动态数组公式转置 (Excel 365 / 2021)**
如果希望在输出工作簿中将 `=TRANSPOSE(A1:D5)` 保留为实时公式，以便源数据发生变化时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 或更高版本**中打开，请使用此方式。

### **使用的 API**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` 是 `Aspose.Cells.Cell` 类的方法，用于将单元格的公式设置为**动态数组公式**。Excel 会对公式求值一次，并自动将结果溢出到周围的单元格中。第三个参数设为 `true` 时，指示 Aspose.Cells 在写入时也计算生成的值。

### **步骤**
1. 通过构造 `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` 加载源工作簿。
2. 通过 `workbook.GetWorksheets().Get(0)` 获取第一个工作表，并通过 `worksheet.GetCells()` 访问其 `Cells` 集合。
3. 在源区域正下方的单元格 **A6** 中放置动态数组公式，调用 `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`。
4. `nullptr` 参数传递默认 `FormulaParseOptions`，第三个参数 `true` 指示 Aspose.Cells 将该公式视为动态数组公式并进行计算，以便将溢出值写入工作簿。
5. 使用 `workbook.Save(outputFile)` 保存工作簿。
单元格 **A6** 包含公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到区域 **A6:D10**。该区域为一个 5 行 × 4 列的块，与转置后的数据一致。

{{% alert color="primary" %}}
此方式**仅适用于 Excel 365 / 2021 或更高版本**。较旧的 Excel 版本无法正确溢出动态数组公式。
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

## **方法 3 — 使用经典数组公式转置 (CSE)**
如果希望在保留工作簿中 `TRANSPOSE` 公式的同时，目标 Excel 文件还可能在不支持动态数组溢出的**较旧 Excel 版本（2021 之前，包括 2019、2016、2013 等）中打开，请使用此方式。经典 CSE (Ctrl+Shift+Enter) 数组公式是向后兼容的替代方案，所有 Excel 版本均可对其求值。

### **使用的 API**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` 是 `Aspose.Cells.Cell` 类的方法，用于为锚点单元格指定**经典数组 (CSE) 公式**，并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，使 Excel 将该公式作为单个数组表达式求值并填充所声明的区域。

### **步骤**
1. 通过 `workbook.GetWorksheets().Get(0)` 获取第一个工作表，并通过 `worksheet.GetCells()` 访问其 `Cells` 集合。
2. 调用 `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 是目标数组的行数，第三个参数 `5` 是列数。
3. 使用 `workbook.Save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点，计算后的数组从 A6 开始跨越 4 行 × 5 列，与 A1:D5 源区域的转置后维度一致。Excel 会在结果区域中写入一个数组公式标记，使较旧 Excel 版本能够正确求值。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 经典的方式来计算 `TRANSPOSE` 表达式，此方式与所有 Excel 版本完全兼容。
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
    // 访问第一个工作表及其 Cells 集合
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // 在单元格 A6 上设置经典 CSE 数组公式。
    // 公式 =TRANSPOSE(A1:D5) 将 5 行 × 4 列的源范围转换为
    // 4 行 × 5 列的数组。第二个参数 (4) 是结果数组的行数，
    // 第三个参数 (5) 是结果数组的列数。
    // Aspose.Cells 会写入 CSE 数组公式标记，使 Excel 将其作为
    // 单个多单元格数组公式进行计算，兼容不支持动态数组溢出的旧版 Excel 版本
    // (2019、2016、2013 等)。
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // 保存工作簿，以持久化数组公式标记
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **比较 — 何时使用每种方式**
| 方法                               | API / 方法                          | Excel 版本             | 是否保留源公式？             | 输出区域             |
|------------------------------------|-------------------------------------|------------------------|------------------------------|----------------------|
| 方法 1 — 原地转置                  | `Range.Transpose()`                 | 所有 Excel 版本         | 否（仅值）                   | 初始锚点区域，5×4    |
| 方法 2 — 动态数组公式              | `Cell.SetDynamicArrayFormula`       | Excel 365 / 2021+       | 是（动态溢出）               | 从锚点溢出           |
| 方法 3 — 经典数组公式 (CSE)        | `Cell.SetArrayFormula`              | 所有 Excel 版本         | 是（多单元格数组公式）       | 显式大小，4×5        |
如果需要快速执行跨版本转换，并且只需将转置后的值写入文件，请使用**方法 1**。如果确保使用现代 Excel，并希望公式保持实时且在源数据发生变化时自动更新，请使用**方法 2**。如果需要在所有 Excel 版本中保留公式并获得最广泛的兼容性，包括不支持动态数组的较旧版本，请使用**方法 3**。

{{< app/cells/assistant language="cpp" >}}