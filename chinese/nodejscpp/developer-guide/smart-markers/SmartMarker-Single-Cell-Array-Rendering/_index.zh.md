---
title: SmartMarker 单单元格数组渲染 | Aspose.Cells for Node.js via C++
linktitle: SmartMarker 单单元格数组渲染 | Aspose.Cells
description: 学习如何使用 Aspose.Cells for Node.js via C++ 中的 Smart Markers，通过 ArrayAsSingle 和 ExtraDelimiter 属性将数组数据渲染到单个单元格中。
keywords: Aspose.Cells, Node.js library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
url: /zh/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过 Smart Markers 将数组数据渲染到单个单元格中。通过将 `ArrayAsSingle` 属性与 `ExtraDelimiter` 属性结合使用，开发人员可以控制数组元素在单个单元格中的分隔方式，从而为报表和模板提供灵活的格式化功能。

{{% /alert %}}

## **简介**

Aspose.Cells 中的 Smart Markers 是一项基于模板的强大功能，允许您使用标记表达式（例如 `&=DataSource.Field`）动态填充电子表格数据。标记放置在设计器工作簿中，当模板由 `WorkbookDesigner` 处理时，标记会被替换为来自所提供数据源的值。

默认情况下，当 Smart Marker 引用数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放入相邻的单独单元格中——可以水平跨行或垂直跨列。虽然这种行为在许多场景中都很方便，但在某些情况下，您可能希望将整个数组渲染到一个单元格中，元素之间使用您选择的分隔符进行连接和分隔。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性在 Smart Marker 标签内一起使用，恰好可以满足此需求。它们允许您在保持报表布局紧凑和可预测的同时，仍能原生处理数组数据源。

## **为什么需要此功能**

### **默认数组展开行为**

当 Smart Marker 引用数组属性时，Aspose.Cells 默认会将数组展开到多个单元格中。例如，针对包含四个值的 `string[]` 使用诸如 `&=Product.Tags` 之类的标记时，每个值将放置在各自的单元格中，将其他模板内容向外推，可能会破坏精心设计的报表布局。

### **使用场景的局限性**

在许多实际场景中，默认的展开行为并不理想：

- **摘要式报表**，需要每条记录一行的紧凑布局。
- **标签、标记或关键词列表**，需要在单个单元格中以逗号分隔或竖线分隔的值显示。
- **筛选标签或状态指示器**，将多个值分组显示在同一位置以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并），期望每个单元格包含单个合并值，而不是展开的区域。
- **跨平台兼容性**，某些使用者无法接受跨多个单元格的数组。

### **它填补的空白**

如果没有内置机制，开发人员将不得不在 JavaScript 中预处理数据——在将数组绑定到工作簿设计器之前将其连接为分隔符分隔的字符串。这会导致逻辑重复、数据模型复杂化，并增加出错的可能性。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在 Smart Marker 内部以声明方式处理格式化，消除了这种变通方法。

## **功能优势**

在 Smart Markers 中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性可带来多项优势：

- **单单元格包含**：所有数组元素都渲染到恰好一个单元格中，保持布局紧凑且可预测。
- **自定义分隔符控制**：指定任意分隔符字符串——逗号、分号、连字符、竖线、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外的代码来预处理数据；格式化规则位于 Smart Marker 标签内。
- **更整洁的报表**：数组数据不再将相邻的模板内容推入不同的行或列。
- **多用途数据类型**：适用于字符串、数字、日期以及任何可以使用分隔符连接的其他数据类型。
- **向后兼容性**：当省略这些属性时，将保留原始的展开行为，因此现有模板可继续正常工作而无需更改。

## **如何使用此功能**

### **Smart Marker 语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对在标准 Smart Marker 的括号内传递。通用语法为：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

标记由以下部分组成：

- `&=DataSource.ArrayProperty` — 标准 Smart Marker，引用绑定数据源上的数组属性。
- `arrayasSingle=true` — 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 才会触发单单元格行为。
- `extraDelimiter=", "` — 定义放置在数组元素之间的分隔符。该值为字符串字面量；可以为空、单个字符或多字符字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如 `\n` 表示换行分隔输出）。如果数组为空，则生成的单元格将保留空白。

{{% /alert %}}

### **分步工作流**

以下工作流描述了如何使用 Smart Markers 将数组渲染到单个单元格中。

1. **准备数据源**：创建一个公开返回数组的属性的类（或数据结构）。该属性可以返回 `string[]`、`int[]` 或任何其他受支持的数组类型。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加标题行，并放置一个 Smart Marker 单元格，该单元格使用 `arrayasSingle` 和 `extraDelimiter` 属性引用数组属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到其上，并使用 `setDataSource` 方法绑定您的数据源。
4. **处理标记**：调用 `workbookDesigner.process()` 方法以展开 Smart Markers 并将真实数据填充到工作簿中。
5. **保存结果**：将生成的工作簿以 XLSX 或任何其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组渲染**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **代码示例 2 — 使用自定义分隔符的数值数组**

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
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Section 1: Default Smart Marker - values spread horizontally across cells
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// Bind the data source and process Smart Markers
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// Save the resulting workbook
workbook.save("output_comparison.xlsx");
```

### **注意事项与最佳实践**

在使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请记住以下几点：

- `extraDelimiter` 值被视为字符串字面量；请转义模板处理器可能解释的任何特殊字符。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。只有 `true` 才会触发单单元格行为；任何其他值都将回退到默认的展开行为。
- 如果数组为空或 null，则单元格保留为空（或根据数据类型包含空字符串）。
- 此功能适用于对象数据源以及可以将列拆分为数组的 `DataSet` 和 `DataTable` 数据源。
- 对于换行分隔的输出，您可以使用 `\n` 或 `os.EOL` 作为分隔符值。
- 将 Smart Marker 放置在具有足够宽度的单元格中以显示生成的连接字符串；否则，内容可能会根据格式以视觉方式溢出到相邻单元格中。

## **相关文章**

- [合并与取消合并单元格](/cells/zh/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}