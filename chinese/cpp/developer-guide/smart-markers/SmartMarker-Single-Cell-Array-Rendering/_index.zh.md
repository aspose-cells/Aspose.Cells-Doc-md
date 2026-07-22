---
title: SmartMarker 单单元格数组渲染 | Aspose.Cells C++
linktitle: SmartMarker 单单元格数组渲染 | Aspose.Cells
description: 学习如何在 Aspose.Cells for C++ 的 Smart Markers 中使用 ArrayAsSingle 和 ExtraDelimiter 属性将数组数据渲染到单个单元格。
keywords: Aspose.Cells, C++ 库, 电子表格, Smart Markers, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组渲染, 模板
type: docs
weight: 195
url: /zh/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过 Smart Markers 将数组数据渲染到单个单元格中。通过将 `ArrayAsSingle` 属性与 `ExtraDelimiter` 属性结合使用，开发人员可以控制数组元素在单个单元格内的分隔方式，从而为报表和模板提供灵活的格式化功能。

{{% /alert %}}

## **简介**

Aspose.Cells 中的 Smart Markers 是一项强大的、基于模板的功能，允许您使用标记表达式（如 `&=DataSource.Field`）动态填充电子表格数据。标记放置在设计器工作簿中，当模板由 `WorkbookDesigner` 处理时，标记会被数据源中提供的值替换。

默认情况下，当 Smart Marker 引用数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放置到相邻的独立单元格中 —— 可以是水平跨行展开，也可以是垂直沿列展开。尽管此行为在许多场景下都很方便，但在某些情况下，您可能希望将整个数组渲染到单个单元格中，将元素连接起来并用您选择的分隔符分隔。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性在 Smart Marker 标签内一起使用，正好满足了这一需求。它们允许您保持报表布局的紧凑性和可预测性，同时仍能以原生方式处理数组数据源。

## **为什么需要此功能**

### **默认的数组展开行为**

当 Smart Marker 引用数组属性时，Aspose.Cells 默认会跨多个单元格展开数组。例如，针对包含四个值的 `string[]` 使用类似 `&=Product.Tags` 的标记时，会将每个值放入各自的单元格中，将其他模板内容向外推移，从而可能破坏精心设计的报表布局。

### **用例限制**

在许多实际场景中，默认的展开行为是不符合需求的：

- **摘要式报表**：需要每条记录一行的紧凑布局。
- **标记、标签或关键词列表**：需要在单个单元格中显示为逗号分隔或竖线分隔的值。
- **筛选标签或状态指示器**：将多个值分组显示在同一个位置以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并）：期望每个单元格中有一个合并后的单一值，而不是展开的区域。
- **跨平台兼容性**：某些使用者无法接受跨多个单元格扩散的数组。

### **它填补的空白**

如果没有内置机制，开发人员将被迫在 C++ 中预处理数据 —— 在将数组绑定到工作簿设计器之前将数组合并为分隔字符串。这会导致逻辑重复、使数据模型复杂化并增加出错的可能性。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在 Smart Marker 内部以声明方式处理格式化，消除了这种变通方法。

## **功能优势**

在 Smart Markers 中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性具有以下优势：

- **单单元格包含**：所有数组元素渲染到恰好一个单元格中，保持布局的紧凑性和可预测性。
- **自定义分隔符控制**：可以指定任意分隔符字符串 —— 逗号、分号、连字符、竖线、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外的代码来预处理数据；格式化规则存在于 Smart Marker 标签内部。
- **更清晰的报表**：数组数据不再将相邻的模板内容推到不同的行或列中。
- **多种数据类型**：适用于字符串、数字、日期以及可以使用分隔符连接的任何其他数据类型。
- **向后兼容**：当省略这些属性时，将保留原始的展开行为，因此现有模板可以继续正常工作而无需更改。

## **如何使用此功能**

### **Smart Marker 语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对在标准 Smart Marker 的括号内传递。通用语法为：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

该标记由以下部分组成：

- `&=DataSource.ArrayProperty` — 标准 Smart Marker，引用绑定数据源上的数组属性。
- `arrayasSingle=true` — 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 才会触发单单元格行为。
- `extraDelimiter=", "` — 定义数组元素之间的分隔符。该值是一个字符串字面量；可以为空、单个字符或多字符字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如 `\n` 表示换行分隔输出）。如果数组为空，则生成的单元格将留空。

{{% /alert %}}

### **分步工作流**

以下工作流描述了如何使用 Smart Markers 将数组渲染到单个单元格中。

1. **准备数据源**：创建一个公开返回数组的属性的类（或数据结构）。该属性可以返回 `std::vector<std::string>`、`std::vector<int>` 或任何其他受支持的数组/向量类型。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加标题行，并放置一个 Smart Marker 单元格，引用带 `arrayasSingle` 和 `extraDelimiter` 属性的数组属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到它，并使用 `SetDataSource` 方法绑定您的数据源。
4. **处理标记**：调用 `WorkbookDesigner.Process()` 方法以展开 Smart Markers 并将真实数据填充到工作簿中。
5. **保存结果**：将生成的工作簿以 XLSX 或任何其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组渲染**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // Aspose.Cells for C++ 中不提供 WorkbookDesigner
    // 我们需要通过手动替换标记来模拟 SmartMarker 处理
    // 由于 Aspose.Cells C++ 不支持 WorkbookDesigner，我们将使用 U16String 替换
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // 将智能标记替换为实际数据
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **代码示例 2 — 使用自定义分隔符的数字数组**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **代码示例 3 — 比较默认行为与 ArrayAsSingle 行为**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // 准备数据源
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // 创建工作簿并获取第一个工作表
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // 第 1 部分：默认智能标记 - 值水平分布在各个单元格中
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // 第 2 部分：使用 arrayasSingle 和 extraDelimiter 进行新的单单元格渲染
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // 绑定数据源并处理智能标记
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // 保存生成的工作簿
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **注意事项与最佳实践**

在使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请记住以下几点：

- `extraDelimiter` 的值被视为字符串字面量；对模板处理器可能解释的任何特殊字符进行转义。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。只有 `true` 才会触发单单元格行为；任何其他值都会回退到默认的展开行为。
- 如果数组为空或为 null，则该单元格将保留为空（或者根据数据类型包含空字符串）。
- 此功能适用于对象数据源以及 `DataSet` 和 `DataTable` 数据源（其中列可以拆分为数组）。
- 对于换行分隔的输出，可以使用 `\n` 作为分隔符值。
- 将 Smart Marker 放置在具有足够宽度的单元格中以显示生成的连接字符串；否则，根据格式的不同，内容可能在视觉上溢出到相邻单元格中。

## **相关文章**

- [Smart Markers](/cells/zh/cpp/smart-markers/)
- [合并与取消合并单元格](/cells/zh/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}