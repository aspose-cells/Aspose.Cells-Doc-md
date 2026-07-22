---
title: SmartMarker 单单元格数组渲染 | Aspose.Cells for Python via .NET
linktitle: SmartMarker 单单元格数组渲染 | Aspose.Cells
description: 学习如何使用 Aspose.Cells for Python via .NET 中 Smart Markers 的 ArrayAsSingle 和 ExtraDelimiter 属性将数组数据渲染到单个单元格中。
keywords: Aspose.Cells, Python via .NET 库, 电子表格, Smart Markers, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组渲染, 模板
type: docs
weight: 195
url: /zh/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过 Smart Markers 将数组数据渲染到单个单元格中。通过同时使用 `ArrayAsSingle` 属性和 `ExtraDelimiter` 属性，开发人员可以控制数组元素在单个单元格中的分隔方式，从而为报表和模板提供灵活的格式化功能。

{{% /alert %}}

## **简介**

Aspose.Cells 中的 Smart Markers 是一项强大的、基于模板的功能，允许您使用标记表达式（如 `&=DataSource.Field`）动态填充电子表格数据。标记放置在设计器工作簿中，当模板由 `WorkbookDesigner` 处理时，标记会被替换为来自所提供数据源的值。

默认情况下，当 Smart Marker 引用一个数组属性（例如，`&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放置到相邻的单独单元格中——可以是水平横跨一行，也可以是垂直沿一列向下。虽然这种行为在许多场景下很方便，但在某些情况下，您可能更倾向于将整个数组渲染到单个单元格中，元素之间使用您选择的分隔符进行连接和分隔。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性一起在 Smart Marker 标签内使用，正是为了满足这一需求。它们允许您保持报表布局紧凑且可预测，同时仍然能够原生处理数组数据源。

## **为何需要此功能**

### **默认数组展开行为**

当 Smart Marker 引用一个数组属性时，Aspose.Cells 默认会跨多个单元格展开数组。例如，对于包含四个值的 `string[]` 数组，使用 `&=Product.Tags` 这样的标记会将每个值放入各自的单元格中，从而推动其他模板内容向外移动，并可能破坏精心设计的报表布局。

### **用例限制**

在许多实际场景中，默认的展开行为是不符合需求的：

- **摘要式报表**，需要每个记录占用一行的紧凑布局。
- **标签、标识或关键词列表**，需要以逗号分隔或竖线分隔的值显示在单个单元格中。
- **筛选标签或状态指示器**，将多个值分组显示在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并），期望每个单元格包含一个合并后的值，而不是展开的区域。
- **跨平台兼容性**，某些使用者无法接受数组溢出到多个单元格的情况。

### **它填补的空白**

如果没有内置机制，开发人员将不得不在 Python 中预处理数据——在将数组绑定到工作簿设计器之前将其连接为带分隔符的字符串。这会导致逻辑重复、使数据模型复杂化，并增加出错的可能性。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在 Smart Marker 内部以声明方式处理格式化问题，从而消除了这种变通方法。

## **功能优势**

在 Smart Markers 中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性可提供以下优势：

- **单单元格容纳**：所有数组元素都渲染到恰好一个单元格中，使布局保持紧凑和可预测。
- **自定义分隔符控制**：可以指定任意分隔符字符串——逗号、分号、连字符、竖线、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外的代码来预处理数据；格式化规则驻留在 Smart Marker 标签中。
- **更整洁的报表**：数组数据不再将相邻的模板内容推入不同的行或列。
- **多用途数据类型**：适用于字符串、数字、日期以及任何可以使用分隔符连接的其他数据类型。
- **向后兼容性**：当省略这些属性时，将保留原有的展开行为，因此现有模板可以继续正常使用而无需修改。

## **如何使用此功能**

### **Smart Marker 语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对传递，位于标准 Smart Marker 的圆括号内。通用语法为：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

该标记由以下部分组成：

- `&=DataSource.ArrayProperty` — 引用绑定数据源上数组属性的标准 Smart Marker。
- `arrayasSingle=true` — 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 会触发单单元格行为。
- `extraDelimiter=", "` — 定义数组元素之间放置的分隔符。该值是一个字符串字面量；可以为空、单个字符或多个字符的字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如 `\n` 表示换行分隔输出）。如果数组为空，则结果单元格将留空。

{{% /alert %}}

### **分步工作流**

以下工作流描述了如何使用 Smart Markers 将数组渲染到单个单元格中。

1. **准备数据源**：创建一个公开返回数组的属性的类（或数据结构）。该属性可以返回 `list[str]`、`list[int]` 或任何其他受支持的数组类型。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加标题行，并放置一个 Smart Marker 单元格，该单元格引用带有 `arrayasSingle` 和 `extraDelimiter` 属性的数组属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到该对象，并使用 `set_data_source` 方法绑定您的数据源。
4. **处理标记**：调用 `WorkbookDesigner.process()` 方法展开 Smart Markers 并使用真实数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或任何其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组渲染**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **代码示例 2 — 带自定义分隔符的数字数组**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **代码示例 3 — 比较默认行为与 ArrayAsSingle 行为**

```python
class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# 第 1 节：默认智能标记 - 值水平跨单元格分布
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# 第 2 节：使用 arrayasSingle 和 extraDelimiter 进行新的单单元格渲染
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# 绑定数据源并处理智能标记
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# 保存生成的工作簿
workbook.save("output_comparison.xlsx")
```

### **注意事项与最佳实践**

在使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请牢记以下几点：

- `extraDelimiter` 的值被视为字符串字面量；对模板处理器可能解释的特殊字符进行转义。
- `arrayasSingle` 属性接受布尔值（`True` / `False`）。只有 `True` 会触发单单元格行为；任何其他值将回退到默认的展开行为。
- 如果数组为空或为 null，则该单元格将留空（或者根据数据类型包含一个空字符串）。
- 该功能适用于对象数据源，也适用于可以将列拆分为数组的 `DataSet` 和 `DataTable` 数据源。
- 对于换行分隔输出，您可以使用 `\n` 或 `os.linesep` 作为分隔符值。
- 将 Smart Marker 放置在具有足够宽度的单元格中，以显示连接后的字符串；否则，根据格式的不同，内容可能会在视觉上溢出到相邻的单元格。

## **相关文章**

- [Smart Markers](/cells/zh/python-net/smart-markers/)
- [合并与取消合并单元格](/cells/zh/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}