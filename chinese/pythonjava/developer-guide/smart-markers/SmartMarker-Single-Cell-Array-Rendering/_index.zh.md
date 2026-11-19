---
title: SmartMarker 单单元格数组呈现 | Aspose.Cells for Python via Java
linktitle: SmartMarker 单单元格数组呈现 | Aspose.Cells for Python via Java
description: 了解如何使用 Aspose.Cells for Python via Java 中的 arrayassingle 和 arraydelimiter 智能标记属性，将数组数据呈现到单个单元格中。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 智能标记, arrayassingle, arraydelimiter, 单单元格数组, 数组呈现, 模板
type: docs
weight: 195
url: /zh/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 可通过智能标记将数组数据源呈现到单个单元格中。`arrayassingle` 属性会关闭默认的逐元素展开行为，而 `arraydelimiter` 属性用于指定拼接元素之间的分隔符：默认为逗号，也可指定任意单个字符或带引号的多字符字符串。
{{% /alert %}}

## **简介**
Aspose.Cells 中的智能标记是一项基于模板的功能，可使用 `&=DataSource.Field` 等标记表达式动态填充电子表格数据。该标记位于设计器工作簿中；当模板由 `WorkbookDesigner` 处理时，标记会被替换为所提供数据源中的相应值。
默认情况下，当智能标记引用数组字段（例如，绑定到包含四个值的列表的 `&=Product.Tags`）时，引擎会展开数组，并将每个元素放入单独的单元格，使值沿标记所在列向下排列。尽管这种行为在许多场景下都很方便，但有时您需要将整个数组呈现到一个单元格中，拼接所有元素，并使用所选分隔符将其分隔。
`arrayassingle` 和 `arraydelimiter` 属性以 `name:value` 形式写在智能标记的括号内，正是为满足这一需求而设计的。它们使您能够原生处理数组数据源，同时保持报表布局紧凑且可预测。

## **为什么需要此功能**

### **默认的数组展开行为**
当智能标记引用数组字段时，Aspose.Cells 默认会将数组扩展到多个单元格。例如，对于包含四个值的列表，`&=Product.Tags` 这样的标记会将每个值放入标记下方的各个单元格中，使其他模板内容向下移位，甚至可能破坏精心设计的报表布局。

### **用例限制**
在许多实际场景中，默认的展开行为并不理想：
- **摘要类报表**：需要采用每条记录一行的紧凑布局。
- **标记、标签或关键字列表**：需要在单个单元格中显示以逗号或管道符分隔的值。
- **筛选标签或状态指示器**：需要将多个值集中显示在同一位置，以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并）：要求每个单元格仅包含一个合并后的值，而不是扩展后的区域。
- **跨平台兼容性**：某些使用方无法处理数组内容扩展到多个单元格的情况。

### **它所填补的空白**
如果没有内置机制，开发者将不得不在 Python 中预处理数据，即在将列表绑定到工作簿设计器之前，先将列表拼接为带分隔符的字符串。这会重复实现处理逻辑、使数据模型更加复杂，并增加出错的可能性。`arrayassingle` 和 `arraydelimiter` 属性通过在智能标记本身中以声明方式进行格式化，消除了这种变通做法。

## **功能优势**
在智能标记中使用 `arrayassingle` 和 `arraydelimiter` 属性可获得以下优势：
- **内容集中于单个单元格**：所有数组元素均呈现于同一个单元格中，使布局紧凑且可预测。
- **灵活控制分隔符**：可指定所需分隔符，例如默认逗号、分号、连字符、管道符，或 `" | "` 这样的带引号多字符字符串。
- **基于模板的格式设置**：无需额外的代码来预处理数据；格式规则直接写在智能标记中。
- **更整洁的报表**：数组数据不再将相邻的模板内容挤到其他行或列。
- **支持多种数据类型**：适用于以 JSON 行形式提供的字符串数组，包括以字符串形式呈现的数值。
- **向后兼容性**：省略这些属性时，将保留原有的展开行为，因此现有模板无需更改即可继续使用。

## **如何使用此功能**

### **智能标记语法**
`arrayassingle` 和 `arraydelimiter` 属性在标准智能标记的括号内采用 Aspose.Cells 的 `name:value` 属性语法。一般语法如下：

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

该标记由以下部分组成：
- `&=DataSource.ArrayField` — 引用已绑定数据源中数组字段的标准智能标记。
- `arrayassingle:true` — 指示引擎将整个数组呈现到一个单元格中，而不是逐元素展开。
- `arraydelimiter:;` — 可选；指定数组元素之间的分隔符。省略时使用逗号。

{{% alert color="warning" %}}
请使用 `name:value` 形式编写属性（使用冒号，而不是等号），并用逗号分隔多个属性，**且逗号后不要留空格**。逗号后的空格会使解析得到的分隔符值偏移一个字符，因此 `(arrayassingle:true, arraydelimiter:;)` 会错误地使用 `:;` 而不是 `;` 进行拼接。
{{% /alert %}}

### **分隔符形式**
- 单个字符直接写在冒号后：`arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 多字符分隔符使用双引号括起：`arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **分步工作流**
以下工作流说明如何使用智能标记将数组呈现到一个单元格中。
1. **准备数据源**：将每条记录组织为 JSON 对象，其中一个字段保存数组，例如 `{"Tags": ["C#", "Aspose"]}`。在此平台上，传递给 `setDataSource` 的普通 Python 类实例和字典不会绑定；JSON 行是受支持的表格数据形式。
2. **创建设计器工作簿**：创建一个新的 `Workbook` 作为设计器工作簿，添加表头行，并放置一个包含智能标记的单元格，该标记引用数组字段且带有 `arrayassingle` 属性（需要自定义分隔符时还应带有 `arraydelimiter`）。
3. **实例化 WorkbookDesigner**：基于该工作簿创建 `WorkbookDesigner` 实例，并通过 `setJsonDataSource` 附加 JSON 行数据。
4. **处理标记**：调用 `WorkbookDesigner.process()` 方法展开智能标记，并使用实际数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组呈现**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

该示例打印整个数组合并后的值。四个标签值会放入一个单元格中，并使用默认逗号分隔：

```
C#,Aspose,SmartMarker,Excel
```

### **代码示例 2 — 使用自定义分隔符呈现数值**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

当分数以 JSON 字符串提供时，合并后的输出会保留纯数字：

```
95-88-76-100-67
```

{{% alert color="note" %}}
通过 Java 引擎传递的 JSON 数值会被解析为双精度浮点数，因此 `[95, 88]` 会合并为 `95.0-88.0`。如果希望合并后的单元格中显示确切的整数文本，请在 JSON 行中用引号括起数值。
{{% /alert %}}

### **代码示例 3 — 比较默认呈现与单单元格呈现**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

默认标记会沿 B 列向下为每个元素填充一个单元格，而 `arrayassingle` 标记会将同一数组合并到 C 列的一个单元格中：

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注意事项和最佳实践**
使用 `arrayassingle` 和 `arraydelimiter` 属性时，请注意以下要点：
- 属性值使用 `name:value` 形式。像 `arrayassingle=true` 这样的等号形式无法识别，并且会静默回退到默认展开行为。
- 使用逗号分隔属性，且逗号后不要留空格；逗号后的空格会使分隔符值偏移一个字符（请参阅上述警告）。
- `arraydelimiter` 的值可以是直接写在冒号后的单个字符，也可以是用双引号括起的多字符字符串。
- 省略 `arraydelimiter` 时，各元素将使用逗号连接。
- 数组字段必须通过 `setJsonDataSource` 的行对象提供；在此平台上，传递给 `setDataSource` 的普通 Python 对象和字典不会绑定。
- 通过 Java 引擎传递的 JSON 数值会被解析为双精度浮点数（`95` 合并后为 `95.0`）；当需要确切的整数文本时，请在 JSON 行中用引号括起数值。
- 将智能标记放在宽度足以显示最终拼接字符串的单元格中；否则，根据格式设置，内容可能会在视觉上溢出到相邻单元格。

## 相关文章

- [在 Aspose.Cells for Python via Java 中向数据透视表添加筛选字段](/cells/zh/python-java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Python via Java 中为数据透视表应用样式](/cells/zh/python-java/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/python-java/change-page-field-layout/)
- [在 Aspose.Cells for Python via Java 中将迷你图转换为图像和 HTML](/cells/zh/python-java/convert-sparkline-to-image-and-html/)
- [将 Excel 转换为 OFD 格式](/cells/zh/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}