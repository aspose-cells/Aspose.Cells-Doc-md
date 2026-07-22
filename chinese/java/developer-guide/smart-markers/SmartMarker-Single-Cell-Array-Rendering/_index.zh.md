---
title: 智能标记单单元格数组渲染 | Aspose.Cells Java
linktitle: 智能标记单单元格数组渲染 | Aspose.Cells
description: 了解如何通过 Smart Markers 中的 ArrayAsSingle 和 ExtraDelimiter 属性，使用 Aspose.Cells for Aspose.Cells for Java 将数组数据渲染到单个单元格中。
keywords: Aspose.Cells, Java 库, 电子表格, Smart Markers, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组渲染, 模板
type: docs
weight: 195
url: /zh/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持通过 Smart Markers 将数组数据渲染到单个单元格中。通过同时使用 `ArrayAsSingle` 属性和 `ExtraDelimiter` 属性，开发人员可以控制数组元素在单个单元格内的分隔方式，从而为报表和模板提供灵活的格式化选项。

{{% /alert %}}

## **简介**

Aspose.Cells 中的 Smart Markers 是一项基于模板的强大功能，允许您使用 `&=DataSource.Field` 等标记表达式动态填充电子表格数据。该标记放置在设计者工作簿中，当模板由 `WorkbookDesigner` 处理时，这些标记将被所提供数据源中的值替换。

默认情况下，当 Smart Marker 引用一个数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组并将每个元素放置到相邻的单独单元格中——可以横向排列在一行中，也可以纵向排列在一列中。虽然此行为在许多场景下都很方便，但在某些情况下，您可能更倾向于将整个数组渲染到单个单元格中，并将元素连接起来，以您选择的分隔符进行分隔。

`ArrayAsSingle` 和 `ExtraDelimiter` 属性在 Smart Marker 标签内一起使用，正好可以满足这一需求。它们使您能够保持报表布局的紧凑性和可预测性，同时仍能原生使用数组数据源。

## **为何需要此功能**

### **默认的数组展开行为**

当 Smart Marker 引用数组属性时，Aspose.Cells 默认会将数组展开到多个单元格中。例如，针对一个包含四个值的 `string[]`，使用诸如 `&=Product.Tags` 这样的标记，会将每个值分别放置到自己的单元格中，从而将其他模板内容向外推挤，并可能破坏精心设计的报表布局。

### **使用场景的限制**

在许多实际场景中，默认的展开行为是不可取的：

- **摘要式报表**：需要每条记录一行的紧凑布局。
- **标签、标注或关键词列表**：需要在单个单元格中以逗号分隔或竖线分隔的值的形式显示。
- **筛选标签或状态指示器**：将多个值集中显示在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 渲染、邮件合并）：期望每个单元格中只有一个合并后的值，而不是展开后的区域。
- **跨平台兼容性**：某些使用者无法接受跨多个单元格的数组。

### **它填补的空白**

如果没有内置机制，开发人员将不得不在 Java 中预处理数据——在将数组绑定到工作簿设计器之前，先将数组连接为带分隔符的字符串。这会导致逻辑重复、使数据模型复杂化，并增加出错的可能性。`ArrayAsSingle` 和 `ExtraDelimiter` 属性通过在 Smart Marker 内部以声明方式处理格式化问题，消除了这种变通方法的必要性。

## **功能优势**

在 Smart Markers 中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性具有以下几个优势：

- **单单元格包含**：所有数组元素都将渲染到恰好一个单元格中，保持布局紧凑且可预测。
- **自定义分隔符控制**：您可以指定任意分隔符字符串——逗号、分号、连字符、竖线、换行符或任何自定义文本。
- **模板驱动的格式化**：无需额外的代码来预处理数据；格式化规则存在于 Smart Marker 标签内部。
- **更清晰的报表**：数组数据不再将相邻的模板内容推到不同的行或列中。
- **多用途的数据类型**：适用于字符串、数字、日期以及任何可以使用分隔符连接的其他数据类型。
- **向后兼容性**：当省略这些属性时，将保留原始的展开行为，因此现有模板可以继续正常工作而无需修改。

## **如何使用此功能**

### **Smart Marker 语法**

`ArrayAsSingle` 和 `ExtraDelimiter` 属性作为键值对传递给标准 Smart Marker 的圆括号内。一般语法如下：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

该标记由以下部分组成：

- `&=DataSource.ArrayProperty` — 标准的 Smart Marker，引用绑定数据源上的数组属性。
- `arrayasSingle=true` — 指示引擎将整个数组渲染到单个单元格中。只有值 `true` 才会触发单单元格行为。
- `extraDelimiter=", "` — 定义放置在数组元素之间的分隔符。该值是一个字符串字面量；它可以为空、单个字符或多个字符的字符串。

{{% alert color="primary" %}}

`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（如 `\n` 表示换行分隔的输出）。如果数组为空，则结果单元格将留空。

{{% /alert %}}

### **分步工作流程**

以下工作流程描述了如何使用 Smart Markers 将数组渲染到单个单元格中。

1. **准备数据源**：创建一个类（或数据结构），该类公开一个返回数组的属性。该属性可以返回 `String[]`、`int[]` 或任何其他受支持的数组类型。
2. **创建设计者工作簿**：创建一个新的 `Workbook`，添加标题行，并放置一个引用数组属性的 Smart Marker 单元格，该属性带有 `arrayasSingle` 和 `extraDelimiter` 属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计者工作簿附加到该对象上，并使用 `setDataSource` 方法绑定您的数据源。
4. **处理标记**：调用 `WorkbookDesigner.process()` 方法以展开 Smart Markers 并将真实数据填充到工作簿中。
5. **保存结果**：将生成的工作簿以 XLSX 或任何其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组渲染**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **代码示例 2 — 使用自定义分隔符的数字数组**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **代码示例 3 — 对比默认行为与 ArrayAsSingle 行为**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **注意事项与最佳实践**

在使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请牢记以下几点：

- `extraDelimiter` 的值被视为字符串字面量；对模板处理器可能解释的特殊字符进行转义。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。只有 `true` 才会触发单单元格行为；任何其他值都会回退到默认的展开行为。
- 如果数组为空或为 null，则该单元格将留空（或者根据数据类型包含空白字符串）。
- 该功能适用于对象数据源，也适用于可以将列拆分为数组的 `DataSet` 和 `DataTable` 数据源。
- 对于换行分隔的输出，您可以使用 `\n` 或 `System.lineSeparator()` 作为分隔符值。
- 请将 Smart Marker 放置在具有足够宽度的单元格中以显示连接后的字符串；否则，根据格式的不同，内容可能会在视觉上溢出到相邻的单元格中。

## **相关文章**

- [Smart Markers](/cells/zh/java/smart-markers/)
- [合并和取消合并单元格](/cells/zh/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}