---
title: 智能标记单单元格数组渲染 | Aspose.Cells Python via Java
linktitle: 智能标记单单元格数组渲染 | Aspose.Cells Python
description: 了解如何使用 Aspose.Cells for Python via Java 中的 ArrayAsSingle 和 ExtraDelimiter 属性，通过智能标记将数组数据渲染到单个单元格中。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 智能标记, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组渲染, 模板
type: docs
weight: 195
url: /zh/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过智能标记将数组数据渲染到单个单元格中。通过结合使用 `ArrayAsSingle` 属性和 `ExtraDelimiter` 属性，开发人员可以控制数组元素在单个单元格中的分隔方式，从而为报表和模板提供灵活的格式化功能。

{{% /alert %}}

## **介绍**

Aspose.Cells 中的智能标记是一项强大的基于模板的功能，允许您使用标记表达式（如 `&=DataSource.Field`）动态填充电子表格数据。标记放置在设计器工作簿中，当模板由 `WorkbookDesigner` 处理时，标记将被替换为来自所提供数据源的值。

默认情况下，当智能标记引用数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放置到相邻的单独单元格中 —— 可以在行中水平展开，也可以在列中垂直展开。虽然这种行为在许多场景中很方便，但在某些情况下，您可能希望将整个数组渲染到一个单元格中，并将元素连接起来，用您选择的分隔符分隔。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性在智能标记标签内一起使用，正好可以满足这一需求。它们允许您保持报表布局紧凑且可预测，同时仍能直接处理数组数据源。

## **为什么需要此功能**

### **默认数组展开行为**

当智能标记引用数组属性时，Aspose.Cells 默认会跨多个单元格展开数组。例如，针对包含四个值的 `string[]`，一个像 `&=Product.Tags` 这样的标记会将每个值放入其各自的单元格中，将其他模板内容向外推移，可能会破坏精心设计的报表布局。

### **用例局限性**

在许多实际场景中，默认的展开行为并不理想：

- **摘要式报表**，需要每条记录占用一行的紧凑布局。
- **标签、标记或关键字列表**，需要在单个单元格中以逗号分隔或竖线分隔的形式显示。
- **筛选标签或状态指示器**，将多个值分组显示在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并），每个单元格需要单个合并值，而不是展开的单元格区域。
- **跨平台兼容性**，某些使用者无法容忍跨多个单元格的数组。

### **它填补的空白**

如果没有内置机制，开发人员将被迫在 Python 中预处理数据 —— 在将数组绑定到工作簿设计器之前将数组合并为带分隔符的字符串。这会导致逻辑重复、使数据模型复杂化并增加出错几率。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在智能标记内以声明方式处理格式，消除了这种变通方法。

## **功能优势**

在智能标记中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性提供了多项优势：

- **单单元格包含**：所有数组元素都精确渲染到一个单元格中，保持布局紧凑且可预测。
- **自定义分隔符控制**：可以指定您喜欢的任何分隔符字符串 —— 逗号、分号、连字符、竖线、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外的代码来预处理数据；格式化规则位于智能标记标签内。
- **更简洁的报表**：数组数据不再将相邻的模板内容推入不同的行或列。
- **多用途的数据类型**：适用于字符串、数字、日期以及任何可以用分隔符连接的其他数据类型。
- **向后兼容性**：当省略这些属性时，将保留原始的展开行为，因此现有模板可以继续正常工作而无需更改。

## **如何使用此功能**

### **智能标记语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对传递到标准智能标记的圆括号中。一般语法如下：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

该标记由以下部分组成：

- `&=DataSource.ArrayProperty` —— 标准智能标记，引用绑定数据源上的数组属性。
- `arrayasSingle=true` —— 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 才会触发单单元格行为。
- `extraDelimiter=", "` —— 定义数组元素之间放置的分隔符。该值是字符串字面量；它可以为空、单个字符或多字符字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如用于换行分隔输出的 `\n`）。如果数组为空，则生成的单元格将留空。

{{% /alert %}}

### **分步工作流程**

以下工作流程描述了如何使用智能标记将数组渲染到单个单元格中。

1. **准备数据源**：创建一个公开返回数组的属性的类（或数据结构）。该属性可以返回 `string[]`、`int[]` 或任何其他支持的数组类型。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加表头行，并放置一个引用数组属性的智能标记单元格，并使用 `arrayasSingle` 和 `extraDelimiter` 属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到它上面，并使用 `set_data_source` 方法绑定您的数据源。
4. **处理标记**：调用 `WorkbookDesigner.process()` 方法来展开智能标记并用真实数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或任何其他支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组渲染**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **代码示例 2 — 带自定义分隔符的数字数组**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# 定义 Student 类
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **代码示例 3 — 比较默认行为与 ArrayAsSingle 行为**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# 将数据源定义为字典（相当于 Order 类）
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# 第 1 节：默认智能标记 - 值水平分布在单元格中
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# 第 2 节：使用 arrayasSingle 和 extraDelimiter 进行新的单单元格渲染
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# 绑定数据源并处理智能标记
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# 保存生成的工作簿
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **注意事项与最佳实践**

使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请牢记以下几点：

- `extraDelimiter` 值被视为字符串字面量；请转义您的模板处理器可能解释的任何特殊字符。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。只有 `true` 会触发单单元格行为；任何其他值都会回退到默认的展开行为。
- 如果数组为空或为 null，则单元格保持为空（或者根据数据类型包含空白字符串）。
- 此功能适用于对象数据源以及可以将列拆分为数组的 `DataSet` 和 `DataTable` 数据源。
- 对于换行分隔的输出，您可以使用 `\n` 或平台的换行常量作为分隔符值。
- 将智能标记放置在具有足够宽度的单元格中，以显示生成的连接字符串；否则，根据格式的不同，内容可能会视觉上溢出到相邻的单元格中。

## **相关文章**

- [智能标记](/cells/zh/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}