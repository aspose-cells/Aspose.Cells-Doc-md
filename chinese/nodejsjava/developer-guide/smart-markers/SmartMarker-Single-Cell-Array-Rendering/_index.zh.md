---
title: 智能标记单单元格数组呈现 | Aspose.Cells for Node.js via Java
description: 了解如何使用 Aspose.Cells for Node.js via Java 中的 arrayassingle 和 arraydelimiter 智能标记属性，将数组数据呈现到单个单元格中。
linktitle: 智能标记单单元格数组呈现 | Aspose.Cells for Node.js via Java
url: /zh/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 智能标记, arrayassingle, arraydelimiter, 单单元格数组, 数组呈现, 模板
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
借助智能标记，Aspose.Cells 可以将数组数据源呈现到一个单元格中。`arrayassingle` 属性会关闭默认的逐元素展开行为，而 `arraydelimiter` 属性用于指定连接各元素时使用的分隔符——默认为逗号，也可以是您指定的任意单个字符或带引号的多字符字符串。
{{% /alert %}}

## **简介**

Aspose.Cells 中的智能标记是一项基于模板的功能，可使用 `&=DataSource.Field` 等标记表达式动态填充电子表格数据。标记放置在设计器工作簿中；当 `WorkbookDesigner` 处理模板时，这些标记会被替换为来自所提供数据源的值。
默认情况下，当智能标记引用数组字段（例如，绑定到包含四个值的数组的 `&=Product.Tags`）时，引擎会展开数组，并将每个元素放入各自的单元格中，使值沿标记下方的列纵向分布。虽然此行为在许多场景中很方便，但有时您希望将整个数组呈现到一个单元格中，将各元素连接起来并以所选分隔符分隔。
`arrayassingle` 和 `arraydelimiter` 属性正是为满足此需求而设计的。它们以 `name:value` 形式写在智能标记的括号内，使您既能让报表布局保持紧凑、可预测，又能原生处理数组数据源。

## **为什么需要此功能**

### **默认数组展开行为**

当智能标记引用数组字段时，Aspose.Cells 默认会将数组展开到多个单元格中。例如，对于包含四个值的数组，`&=Product.Tags` 之类的标记会将每个值放入标记下方的独立单元格中，从而推动其他模板内容向外扩展，并可能破坏精心设计的报表布局。

### **使用场景的限制**

默认展开行为在许多实际场景中并不适合：
- **汇总类报表**，需要每条记录仅占一行的紧凑布局。
- **标记、标签或关键字列表**，需要在单个单元格中显示为逗号分隔或竖线分隔的值。
- **筛选条件块或状态指示符**，需要将多个值集中显示在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 呈现、邮件合并），每个单元格都应包含一个整合后的值，而不是展开后的区域。
- **跨平台兼容性**，某些使用方无法接受数组扩散到多个单元格中。

### **它所填补的空白**

如果缺少内置机制，开发者将不得不在 JavaScript 中预处理数据，在绑定到 `WorkbookDesigner` 之前先将数组连接为带分隔符的字符串。这会造成逻辑重复、使数据模型复杂化，并增加出错的可能性。`arrayassingle` 和 `arraydelimiter` 属性通过在智能标记自身内部以声明方式处理格式，消除了这种变通方案。

## **功能优势**

在智能标记中使用 `arrayassingle` 和 `arraydelimiter` 属性可获得以下优势：
- **单单元格容纳**：所有数组元素均呈现到同一个单元格中，使布局保持紧凑且可预测。
- **自定义分隔符控制**：可指定所需的分隔符——默认逗号、分号、连字符、竖线，或类似 `" | "` 的带引号多字符字符串。
- **模板驱动的格式设置**：无需额外代码预处理数据；格式规则直接写在智能标记标签内。
- **更整洁的报表**：数组数据不再将相邻模板内容推入其他行或列。
- ** versatile data types**：适用于以 JSON 行形式提供的字符串数组，包括以字符串形式呈现的数值。
- **向后兼容性**：省略这些属性时，将保留原有的展开行为，因此现有模板无需更改即可继续使用。

## **如何使用此功能**

### **智能标记语法**

`arrayassingle` 和 `arraydelimiter` 属性在标准智能标记的括号内使用 Aspose.Cells 的 `name:value` 属性语法。其通用语法为：

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

该标记由以下部分组成：
- `&=DataSource.ArrayField` — 引用绑定数据源中数组字段的标准智能标记。
- `arrayassingle:true` — 指示引擎将整个数组呈现到一个单元格中，而不是展开各个元素。
- `arraydelimiter:;` — 可选；定义数组元素之间使用的分隔符。省略时使用逗号。

{{% alert color="warning" %}}
请以 `name:value` 形式写入属性（使用冒号，而不是等号），并使用逗号分隔多个属性，**逗号后不要加空格**。逗号后的空格会使解析出的值偏移一个字符——`(arrayassingle:true, arraydelimiter:;)` 将错误地使用 `:;` 而不是 `;` 进行连接。
{{% /alert %}}

### **分隔符形式**

- 单个字符直接跟在冒号后：`arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 多字符分隔符使用双引号括起来：`arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **分步工作流**

以下工作流介绍了如何使用智能标记将数组呈现到一个单元格中。
1. **准备数据源**：将每条记录组织为 JSON 对象，其字段包含一个数组，例如 `{"Tags": ["C#", "Aspose"]}`。在此平台上，传递给 `setDataSource` 的普通 JavaScript 对象和数组无法绑定——JSON 行才是受支持的表格形式。
2. **创建设计器工作簿**：创建新的 `Workbook`，添加一个表头行，并放置一个引用数组字段的智能标记单元格，为其添加 `arrayassingle` 属性（需要自定义分隔符时再添加 `arraydelimiter`）。
3. **实例化 WorkbookDesigner**：基于该工作簿创建 `WorkbookDesigner`，并通过 `setJsonDataSource` 附加 JSON 行。
4. **处理标记**：调用 `workbookDesigner.process()` 方法展开智能标记，并使用实际数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组呈现**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

该示例会输出整个数组连接后的值。四个标签值位于同一个单元格中，并使用默认逗号分隔：

```
C#,Aspose,SmartMarker,Excel
```

### **代码示例 2 — 使用自定义分隔符呈现数值**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

以 JSON 字符串形式提供分数后，连接后的输出会保留纯数字文本：

```
95-88-76-100-67
```

{{% alert color="note" %}}
通过 Java 引擎传递的 JSON 数值会作为双精度数值到达，因此 `[95, 88]` 将连接为 `95.0-88.0`。如果希望连接后的单元格中显示精确的整数文本，请在 JSON 行中为数值加引号。
{{% /alert %}}

### **代码示例 3 — 比较默认呈现与单单元格呈现**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

默认标记会沿 B 列向下为每个元素填充一个单元格，而 `arrayassingle` 标记会将同一数组合并到 C 列的单个单元格中：

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注意事项与最佳实践**

使用 `arrayassingle` 和 `arraydelimiter` 属性时，请注意以下事项：
- 属性值采用 `name:value` 形式。`arrayassingle=true` 这样的等号形式无法识别，并会静默回退到默认的展开行为。
- 使用逗号分隔属性且不要加空格；逗号后的空格会使分隔符值偏移一个字符（请参阅上面的警告）。
- `arraydelimiter` 的值可以是直接写在冒号后的单个字符，也可以是使用双引号括起来的多字符字符串。
- 省略 `arraydelimiter` 时，各元素将使用逗号连接。
- 通过 `setJsonDataSource` 的行对象提供数组字段；在此平台上，传递给 `setDataSource` 的普通 JavaScript 对象和数组无法绑定。
- 通过 Java 引擎传递的 JSON 数值会作为双精度数值到达（`95` 连接后为 `95.0`）；当需要精确的整数文本时，请在 JSON 行中为数值加引号。
- 将智能标记放在宽度足以显示生成的连接字符串的单元格中；否则，根据所用格式，内容可能会显示到相邻单元格中。

## 相关文章
- [在 Aspose.Cells for Node.js via Java 中向数据透视表添加筛选字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via Java 中为数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/nodejs-java/change-page-field-layout/)
- [在 Aspose.Cells for Node.js via Java 中将迷你图转换为图片和 HTML](/cells/zh/nodejs-java/convert-sparkline-to-image-and-html/)
- [将 Excel 转换为 OFD 格式](/cells/zh/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}