---
title: 智能标记单单元格数组呈现 | Aspose.Cells for .Net
linktitle: 智能标记单单元格数组呈现 | Aspose.Cells for .Net
description: 了解如何使用 Aspose.Cells for .Net 中的 arrayassingle 和 arraydelimiter 智能标记属性，将数组数据呈现到单个单元格中。
keywords: Aspose.Cells, .NET 类库, 电子表格, 智能标记, arrayassingle, arraydelimiter, 单单元格数组, 数组呈现, 模板
type: docs
weight: 195
url: /zh/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 可以通过智能标记将数组数据源呈现到单个单元格中。`arrayassingle` 属性会关闭默认的逐元素展开行为，`arraydelimiter` 属性用于指定连接数组元素时使用的分隔符——默认为逗号，也可以是您指定的任意单个字符或带引号的多字符字符串。
{{% /alert %}}

## **简介**

Aspose.Cells 中的智能标记是一项基于模板的功能，可使用 `&=DataSource.Field` 等标记表达式动态填充电子表格数据。该标记置于设计器工作簿中；模板由 `WorkbookDesigner` 处理后，标记会替换为所提供数据源中的值。
默认情况下，当智能标记引用数组属性时（例如，引用包含四个值的 `string[]` 的 `&=Product.Tags`），引擎会展开该数组，将每个元素放入各自的单元格，并从标记下方的同一列开始向下排列这些值。虽然此行为在许多场景中都很方便，但在某些情况下，您可能希望将整个数组呈现到一个单元格中，连接各元素并使用所选分隔符进行分隔。
`arrayassingle` 和 `arraydelimiter` 属性采用智能标记括号内的 `name:value` 形式，正是为了满足这一需求。它们使您能够保持报表布局紧凑、可预测，同时仍可原生处理数组数据源。

## **为什么需要此功能**

### **默认数组展开行为**

当智能标记引用数组属性时，Aspose.Cells 默认会将数组扩展到多个单元格。例如，对于包含四个值的 `string[]`，`&=Product.Tags` 等标记会将每个值放入标记下方的独立单元格，从而将其他模板内容向下移位，并可能破坏精心设计的报表布局。

### **使用场景限制**

在许多实际场景中，默认的展开行为并不理想：
- **汇总类报表**：需要采用每条记录占一行的紧凑布局。
- **标记、标签或关键字列表**：需要在单个单元格中显示以逗号或竖线分隔的值。
- **筛选标签或状态指示符**：需要将多个值集中显示在同一位置，以提高可读性。
- **下游流水线**（CSV 导出、PDF 呈现、邮件合并）：要求每个单元格只包含一个合并后的值，而不是扩展后的区域。
- **跨平台兼容性**：某些数据使用方无法接受数组跨越多个单元格扩展。

### **它解决的缺口**

如果缺少内置机制，开发人员将被迫在 C# 或 VB.NET 中预处理数据，在将数据源绑定到工作簿设计器之前，先将数组连接为带分隔符的字符串。这会导致逻辑重复、数据模型复杂化，并增加出错的可能性。`arrayassingle` 和 `arraydelimiter` 属性通过在智能标记内以声明方式完成格式处理，消除了这种变通操作。

## **功能优势**

在智能标记中使用 `arrayassingle` 和 `arraydelimiter` 属性具有以下优势：
- **单单元格呈现**：所有数组元素均呈现于同一个单元格中，使布局保持紧凑且可预测。
- **自定义分隔符**：可指定所需分隔符——默认逗号、分号、连字符、竖线，或带引号的多字符字符串（如 `" | "`）。
- **模板驱动的格式设置**：无需使用额外代码预处理数据；格式规则直接写在智能标记中。
- **更整洁的报表**：数组数据不再使相邻的模板内容移至其他行或列。
- **灵活的数据类型支持**：可处理对象数据源中的字符串数组和数值数组。
- **向后兼容性**：省略这些属性时，将保留原有的展开行为，因此现有模板无需更改即可继续使用。

## **如何使用此功能**

### **智能标记语法**

`arrayassingle` 和 `arraydelimiter` 属性在标准智能标记的括号内采用 Aspose.Cells 的 `name:value` 属性语法。通用语法如下：

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

该标记由以下部分组成：
- `&=DataSource.ArrayProperty` — 标准智能标记，用于引用绑定数据源上的数组属性。
- `arrayassingle:true` — 指示引擎将整个数组呈现到一个单元格中，而不是展开各个元素。
- `arraydelimiter:;` — 可选，用于定义数组元素之间的分隔符。省略此属性时，将使用逗号。

{{% alert color="warning" %}}
请以 `name:value` 形式编写属性（使用冒号，而不是等号），并用逗号分隔多个属性，且逗号后**不要留空格**。逗号后的空格会使解析得到的值偏移一个字符——`(arrayassingle:true, arraydelimiter:;)` 会错误地使用 `:;` 而不是 `;` 进行连接。
{{% /alert %}}

### **分隔符形式**

- 单个字符直接跟在冒号后：`arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 多字符分隔符需使用双引号：`arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **分步工作流**

以下工作流介绍了如何使用智能标记将数组呈现到单个单元格中。
1. **准备数据源**：创建一个公开返回数组属性的类，例如属性类型为 `string[]` 或 `int[]`，并绑定该类的 `List<T>`，使引擎每行读取一条记录。
2. **创建设计器工作簿**：创建新的 `Workbook`，添加表头行，并放置一个引用数组属性且带有 `arrayassingle` 属性的智能标记单元格（需要自定义分隔符时还需添加 `arraydelimiter`）。
3. **实例化 WorkbookDesigner**：基于该工作簿创建 `WorkbookDesigner`，并使用 `SetDataSource` 绑定数据源。
4. **处理标记**：调用 `WorkbookDesigner.Process()` 方法展开智能标记，并使用实际数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组呈现**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

此示例输出整个数组合并后的值。四个标签位于同一个单元格中，并使用默认逗号分隔：

```
C#,Aspose,SmartMarker,Excel
```

### **代码示例 2 — 使用自定义分隔符的数值数组**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

数值数组的连接方式与字符串数组完全相同——每个元素都保留其纯数值文本：

```
95-88-76-100-67
```

### **代码示例 3 — 比较默认呈现与单单元格呈现**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

默认智能标记在 B 列中为每个元素填充一个单元格并向下排列，而 `arrayassingle` 智能标记会将同一个数组合并到 C 列的单个单元格中：

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注意事项与最佳实践**

使用 `arrayassingle` 和 `arraydelimiter` 属性时，请注意以下要点：
- 属性值采用 `name:value` 形式。等号形式（例如 `arrayassingle=true`）无法识别，并且会静默回退到默认的展开行为。
- 使用逗号分隔多个属性，且不要留空格；逗号后的空格会使分隔符值偏移一个字符（参见上述警告）。
- `arraydelimiter` 的值可以是直接写在冒号后的单个字符，也可以是使用双引号包围的多字符字符串。
- 省略 `arraydelimiter` 时，各元素将使用逗号连接。
- 数据源必须允许引擎枚举记录：绑定 `List<T>`（或其他集合），且其元素类型公开数组属性。若绑定单个对象，正文标记将保持未解析状态。
- 相同的属性适用于字符串数组和数值数组；每个元素均以其纯文本值呈现。

## 相关文章
- [在 Aspose.Cells for .NET 中向数据透视表添加筛选字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .NET 中将样式应用于数据透视表](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/net/change-page-field-layout/)
- [在 Aspose.Cells for .NET 中将迷你图转换为图像和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)
- [将 Excel 转换为 OFD 格式](/cells/zh/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}