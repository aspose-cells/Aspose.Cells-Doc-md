---
title: SmartMarker 单单元格数组渲染 | Aspose.Cells for Node.js via Java
description: 了解如何使用 Aspose.Cells for Node.js via Java 中的 ArrayAsSingle 和 ExtraDelimiter 属性，将数组数据渲染到单个单元格。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, Smart Markers, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组渲染, 模板
type: docs
weight: 195
url: /zh/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过 Smart Markers 将数组数据渲染到单个单元格。通过同时使用 `ArrayAsSingle` 属性和 `ExtraDelimiter` 属性，开发人员可以控制数组元素在单个单元格中的分隔方式，从而为报表和模板提供灵活的格式化功能。

{{% /alert %}}

## **简介**

Aspose.Cells 中的 Smart Markers 是一项功能强大的、基于模板的特性，允许您使用标记表达式（如 `&=DataSource.Field`）动态填充电子表格数据。该标记放置在设计器工作簿中，当模板由 `WorkbookDesigner` 处理时，标记将被替换为来自所提供数据源的值。

默认情况下，当 Smart Marker 引用数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放置到相邻的单独单元格中——可以是水平跨行排列，也可以是垂直沿列排列。虽然这种行为在许多场景下都很方便，但在某些情况下，您可能希望将整个数组渲染到一个单元格中，元素之间使用您选择的自定义分隔符进行连接。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性一起在 Smart Marker 标签中使用，正好可以满足这一需求。它们允许您保持报表布局的紧凑性和可预测性，同时仍能以原生方式使用数组数据源。

## **为何需要此功能**

### **默认数组展开行为**

当 Smart Marker 引用数组属性时，Aspose.Cells 默认会将数组展开到多个单元格中。例如，对于包含四个值的 `string[]`，标记 `&=Product.Tags` 会将每个值放置到各自的单元格中，将其他模板内容向外推移，从而可能破坏精心设计的报表布局。

### **使用场景的局限性**

在许多实际场景中，默认的展开行为并不理想：

- **摘要式报表**，需要每条记录一行的紧凑布局。
- **标签、标注或关键词列表**，需要以逗号分隔或竖线分隔的形式显示在单个单元格中。
- **筛选标签或状态指示器**，将多个值集中在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并），期望每个单元格只有一个合并后的值，而不是展开的区域。
- **跨平台兼容性**，某些消费者无法接受数组跨越多个单元格的情况。

### **它填补的空白**

如果没有内置机制，开发人员将不得不在 JavaScript 中预处理数据——在将数组绑定到工作簿设计器之前将数组合并为分隔符分隔的字符串。这会导致逻辑重复、使数据模型复杂化，并增加出错的几率。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在 Smart Marker 内部以声明方式处理格式设置，消除了这种变通方法。

## **功能优势**

在 Smart Markers 中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性具有以下优势：

- **单单元格容纳**：所有数组元素都精确地渲染到一个单元格中，保持布局的紧凑性和可预测性。
- **自定义分隔符控制**：可以指定任意分隔符字符串——逗号、分号、连字符、竖线、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外代码来预处理数据；格式规则位于 Smart Marker 标签内。
- **更整洁的报表**：数组数据不再将相邻的模板内容推入不同的行或列。
- **通用的数据类型**：适用于字符串、数字、日期以及可以使用分隔符连接的任何其他数据类型。
- **向后兼容性**：当省略这些属性时，将保留原有的展开行为，因此现有模板可以继续正常工作而无需更改。

## **如何使用此功能**

### **Smart Marker 语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对传递，在标准 Smart Marker 的圆括号内指定。通用语法如下：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

标记由以下部分组成：

- `&=DataSource.ArrayProperty` — 标准 Smart Marker，引用绑定数据源上的数组属性。
- `arrayasSingle=true` — 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 才会触发单单元格行为。
- `extraDelimiter=", "` — 定义数组元素之间的分隔符。该值为字符串字面量；可以为空、单个字符或多字符字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如用于换行分隔输出的 `\n`）。如果数组为空，则结果单元格将保留空白。

{{% /alert %}}

### **分步骤工作流程**

以下工作流程描述了如何使用 Smart Markers 将数组渲染到单个单元格中。

1. **准备数据源**：创建一个公开返回数组的属性的类（或数据结构）。该属性可以返回 `string[]`、`int[]` 或任何其他受支持的数组类型。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加标题行，并放置一个 Smart Marker 单元格，该单元格引用带有 `arrayasSingle` 和 `extraDelimiter` 属性的数组属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到其上，并使用 `setDataSource` 方法绑定您的数据源。
4. **处理标记**：调用 `workbookDesigner.process()` 方法来展开 Smart Markers 并将真实数据填充到工作簿中。
5. **保存结果**：将生成的工作簿保存为 XLSX 或任何其他受支持的文件格式。

### **代码示例 1 — 基本字符串数组渲染**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **代码示例 2 — 使用自定义分隔符的数字数组**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **代码示例 3 — 比较默认行为与 ArrayAsSingle 行为**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // 第 1 部分：默认智能标记 - 值水平分布在各个单元格中
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // 第 2 部分：使用 arrayasSingle 和 extraDelimiter 的新单单元格渲染
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // 绑定数据源并处理智能标记
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // 保存生成的工作簿
    workbook.save("output_comparison.xlsx");
}

main();
```

### **注意事项与最佳实践**

在使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请牢记以下几点：

- `extraDelimiter` 值被视为字符串字面量；请转义模板处理器可能解释的任何特殊字符。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。只有 `true` 才会触发单单元格行为；任何其他值都将回退到默认的展开行为。
- 如果数组为空或为 null，则单元格将保留为空（或者根据数据类型包含空白字符串）。
- 该功能适用于对象数据源以及可将列拆分为数组的 `DataSet` 和 `DataTable` 数据源。
- 对于换行分隔的输出，您可以使用 `\n` 作为分隔符值。
- 请将 Smart Marker 放置在宽度足以显示结果合并字符串的单元格中；否则，根据格式的不同，内容可能会在视觉上溢出到相邻的单元格中。



{{< app/cells/assistant language="javascript" >}}