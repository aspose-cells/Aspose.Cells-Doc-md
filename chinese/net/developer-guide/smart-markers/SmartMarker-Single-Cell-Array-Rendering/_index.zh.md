---
title: 智能标记单单元格数组渲染 | Aspose.Cells .NET
linktitle: 智能标记单单元格数组渲染 | Aspose.Cells
description: 了解如何在 Aspose.Cells for .NET 中使用 Smart Markers 的 ArrayAsSingle 和 ExtraDelimiter 属性将数组数据渲染到单个单元格。
keywords: Aspose.Cells, .NET 库, 电子表格, Smart Markers, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组渲染, 模板
type: docs
weight: 195
url: /zh/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过 Smart Markers 将数组数据渲染到单个单元格。通过同时使用 `ArrayAsSingle` 属性和 `ExtraDelimiter` 属性，开发人员可以控制数组元素在单个单元格中的分隔方式，从而为报表和模板提供灵活的格式化功能。

{{% /alert %}}

## **简介**

Aspose.Cells 中的 Smart Markers 是一项强大的基于模板的功能，允许您使用标记表达式（如 `&=DataSource.Field`）动态填充电子表格数据。标记放置在设计器工作簿中，当模板由 `WorkbookDesigner` 处理时，标记将被替换为所提供数据源中的值。

默认情况下，当 Smart Marker 引用数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放置到相邻的独立单元格中——可以水平跨行排列，也可以垂直沿列排列。虽然在许多场景中这种行为很方便，但在某些情况下，您可能更倾向于将整个数组渲染到单个单元格中，将所有元素连接起来并以您选择的分隔符分隔。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性在 Smart Marker 标签内一起使用，正好可以满足这一需求。它们使您能够在保持报表布局紧凑且可预测的同时，仍能原生使用数组数据源。

## **为什么需要此功能**

### **默认的数组展开行为**

当 Smart Marker 引用数组属性时，Aspose.Cells 默认会将数组展开到多个单元格中。例如，针对包含四个值的 `string[]`，使用 `&=Product.Tags` 这样的标记会将每个值放入各自的单元格中，从而将其他模板内容向外推移，可能会破坏精心设计的报表布局。

### **使用场景的局限性**

在许多实际场景中，默认的展开行为是不可取的：

- **摘要式报表**，需要每条记录一行的紧凑布局。
- **标签、名称或关键字列表**，需要在单个单元格中以逗号分隔或管道分隔的值形式显示。
- **筛选标签或状态指示器**，将多个值组合在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并），这些管道期望每个单元格只包含一个合并后的值，而不是一个展开的区域。
- **跨平台兼容性**，某些使用者无法接受数组跨多个单元格展开的情况。

### **它填补的空白**

如果没有内置机制，开发人员将被迫在 C# 或 VB.NET 中预处理数据——在将数组绑定到工作簿设计器之前将其连接为带分隔符的字符串。这会导致逻辑重复、数据模型复杂化，并增加出错的几率。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在 Smart Marker 内部以声明方式处理格式化，消除了这种变通方法。

## **功能优势**

在 Smart Markers 中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性可带来以下多项优势：

- **单单元格包含**：所有数组元素都将渲染到恰好一个单元格中，使布局保持紧凑且可预测。
- **自定义分隔符控制**：可以指定任意分隔符字符串——逗号、分号、连字符、管道、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外的代码来预处理数据；格式化规则位于 Smart Marker 标签内部。
- **更清晰的报表**：数组数据不再将相邻的模板内容推入不同的行或列。
- **多用途的数据类型**：适用于字符串、数字、日期以及任何可以使用分隔符连接的其他数据类型。
- **向后兼容**：当省略这些属性时，将保留原始的展开行为，因此现有模板可以继续正常工作而无需更改。

## **如何使用此功能**

### **Smart Marker 语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对传递，放在标准 Smart Marker 的圆括号内。通用语法为：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

该标记由以下部分组成：

- `&=DataSource.ArrayProperty` — 引用绑定数据源上数组属性的标准 Smart Marker。
- `arrayasSingle=true` — 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 才会触发单单元格行为。
- `extraDelimiter=", "` — 定义放置在数组元素之间的分隔符。该值是字符串字面量；可以为空、单个字符或多字符字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如 `\n` 用于换行分隔的输出）。如果数组为空，则结果单元格将留空。

{{% /alert %}}

### **分步工作流程**

以下工作流程描述了如何使用 Smart Markers 将数组渲染到单个单元格中。

1. **准备数据源**：创建一个类（或数据结构），该类公开一个返回数组的属性。该属性可以返回 `string[]`、`int[]` 或任何其他受支持的数组类型。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加一个表头行，并放置一个 Smart Marker 单元格，该单元格使用 `arrayasSingle` 和 `extraDelimiter` 属性引用数组属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到该对象，并使用 `SetDataSource` 方法绑定您的数据源。
4. **处理标记**：调用 `WorkbookDesigner.Process()` 方法以展开 Smart Markers 并将真实数据填充到工作簿中。
5. **保存结果**：将生成的工作簿以 XLSX 或任何其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组渲染**

```csharp
using System;
using Aspose.Cells;

class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }

    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();

        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **代码示例 2 — 带有自定义分隔符的数字数组**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}

public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };

        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **代码示例 3 — 比较默认行为与 ArrayAsSingle 行为**

```csharp
using System;
using Aspose.Cells;

public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };

        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;

        // 第 1 节:默认智能标记 - 值水平分布到各个单元格
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // 第 2 节:使用 arrayasSingle 和 extraDelimiter 进行新的单单元格渲染
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // 绑定数据源并处理智能标记
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // 保存生成的工作簿
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **注意事项与最佳实践**

在使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请牢记以下几点：

- `extraDelimiter` 值被视为字符串字面量；请对模板处理器可能解释的特殊字符进行转义。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。只有 `true` 才会触发单单元格行为；任何其他值都将回退到默认的展开行为。
- 如果数组为空或为 null，则该单元格将留空（或者根据数据类型包含空字符串）。
- 该功能适用于对象数据源，以及列可以拆分为数组的 `DataSet` 和 `DataTable` 数据源。
- 对于换行分隔的输出，您可以使用 `\n` 或 `Environment.NewLine` 作为分隔符值。
- 将 Smart Marker 放置在具有足够宽度的单元格中，以显示最终的连接字符串；否则，根据格式的不同，内容可能会在视觉上溢出到相邻的单元格中。

## **相关文章**

- [Smart Markers](/cells/zh/net/smart-markers/)
- [Merging and Unmerging Cells](/cells/zh/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}