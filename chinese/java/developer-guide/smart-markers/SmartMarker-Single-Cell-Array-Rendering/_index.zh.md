---
title: "智能标记：单单元格数组呈现 | Aspose.Cells for Java"
description: 了解如何在 Aspose.Cells for Java 中使用 arrayassingle 和 arraydelimiter 智能标记属性，将数组数据呈现到单个单元格中。
linktitle: "智能标记：单单元格数组呈现 | Aspose.Cells"
url: /zh/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java 库, 电子表格, 智能标记, arrayassingle, arraydelimiter, 单单元格数组, 数组呈现, 模板
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 可以通过智能标记将数组数据源呈现到一个单元格中。`arrayassingle` 属性会关闭默认的逐元素展开行为，而 `arraydelimiter` 属性用于指定拼接元素之间的分隔符——默认是逗号，也可以是您指定的任意单个字符或用引号括起的多字符字符串。
{{% /alert %}}

## **简介**

Aspose.Cells 中的智能标记是一项基于模板的功能，可使用 `&=DataSource.Field` 等标记表达式动态填充电子表格数据。标记放置在设计器工作簿中；当模板由 `WorkbookDesigner` 处理时，标记将被替换为所提供数据源中的值。
默认情况下，当智能标记引用数组属性时（例如，绑定到包含四个值的 `String[]` 的 `&=Product.Tags`），引擎会展开数组，并将每个元素放入各自的单元格，使值沿标记下方的列纵向排列。尽管这种行为在许多场景中都很方便，但某些情况下，您可能更希望将整个数组呈现到一个单元格中，将各元素拼接起来并用所选分隔符分隔。
`arrayassingle` 和 `arraydelimiter` 属性以 `name:value` 形式写在智能标记的括号内，正好满足这一需求。它们使您可以在保持报表布局紧凑、可预测的同时，继续原生处理数组数据源。

## **为什么需要此功能**

### **默认数组展开行为**

当智能标记引用数组属性时，Aspose.Cells 默认将数组展开到多个单元格。例如，对于包含四个值的 `String[]`，诸如 `&=Product.Tags` 的标记会将每个值放入标记下方的各个单元格，从而推动其他模板内容向外移动，并可能破坏精心设计的报表布局。

### **用例限制**

默认展开行为在许多实际场景中并不理想：
- **摘要型报表**：需要紧凑的每条记录一行的布局。
- **标签、标注或关键字列表**：需要在单个单元格中显示为逗号分隔或竖线分隔的值。
- **筛选标记或状态指示符**：将多个值集中显示在一处，以提高可读性。
- **下游管道**（CSV 导出、PDF 呈现、邮件合并）：每个单元格都要求使用单个合并后的值，而不是扩展后的区域。
- **跨平台兼容性**：某些使用方无法接受数组跨越多个单元格。

### **此功能填补的空白**

如果缺少内置机制，开发人员将不得不在 Java 中预处理数据，即在将数组绑定到工作簿设计器之前，先将其拼接为带分隔符的字符串。这会重复实现逻辑、使数据模型复杂化，并增加出错的可能性。`arrayassingle` 和 `arraydelimiter` 属性直接在智能标记内部以声明方式处理格式，从而消除了这种变通做法。

## **功能优势**

在智能标记中使用 `arrayassingle` 和 `arraydelimiter` 属性可获得以下优势：
- **单单元格容纳**：所有数组元素都会呈现到恰好一个单元格中，使布局保持紧凑且可预测。
- **自定义分隔符控制**：可指定所需分隔符——默认逗号、分号、连字符、竖线，或用引号括起来的多字符字符串（如 `" | "`）。
- **模板驱动的格式设置**：无需额外的预处理代码；格式规则直接内置于智能标记中。
- **更整洁的报表**：数组数据不再把相邻的模板内容挤到其他行或列。
- **多样的数据类型**：适用于字符串数组，以及 JavaBean 数据源中以字符串形式呈现的数值。
- **向后兼容**：省略这些属性时，将保留原有的展开行为，因此现有模板无需更改即可继续工作。

## **如何使用此功能**

### **智能标记语法**

在标准智能标记的括号内，`arrayassingle` 和 `arraydelimiter` 属性采用 Aspose.Cells 的 `name:value` 属性语法。一般语法如下：

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

该标记由以下部分组成：
- `&=DataSource.ArrayProperty` — 引用绑定数据源中数组属性的标准智能标记。
- `arrayassingle:true` — 指示引擎将整个数组呈现到一个单元格，而不是展开各元素。
- `arraydelimiter:;` — 可选；定义数组元素之间使用的分隔符。省略时使用逗号。

{{% alert color="warning" %}}
请使用 `name:value` 形式（使用冒号，而不是等号）写入属性，并使用逗号分隔多个属性，且逗号后**不要留空格**。逗号后的空格会使解析到的值偏移一个字符——`(arrayassingle:true, arraydelimiter:;)` 会错误地使用 `:;` 作为拼接分隔符，而不是 `;`。
{{% /alert %}}

### **分隔符形式**

- 单字符紧跟在冒号后：`arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 多字符分隔符写在双引号内：`arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **分步工作流**

以下工作流介绍如何使用智能标记将数组呈现到一个单元格中。
1. **准备数据源**：创建一个 `public` JavaBean 类，其属性读取方法返回数组，例如 `String[] getTags()`，并绑定一组 JavaBean 对象的 `java.util.List`，使引擎每行读取一条记录。仅公共字段无法完成绑定——引擎读取的是 JavaBean 的属性读取方法。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加标题行，并放入一个引用数组属性且带有 `arrayassingle` 属性的智能标记单元格（需要自定义分隔符时再添加 `arraydelimiter`）。
3. **实例化 WorkbookDesigner**：围绕该工作簿创建 `WorkbookDesigner`，并使用 `setDataSource` 绑定列表。
4. **处理标记**：调用 `WorkbookDesigner.process()` 方法展开智能标记，并使用实际数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组呈现**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

此示例会输出整个数组合并后的值。四个标签值位于同一个单元格中，并使用默认逗号分隔：

```
C#,Aspose,SmartMarker,Excel
```

### **代码示例 2 — 使用自定义分隔符处理数值**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

当数组属性返回 `String[]` 时，数值与字符串的拼接方式完全相同：

```
95-88-76-100-67
```

{{% alert color="note" %}}
在 Java 中，请确保数组属性保持为 `String[]`。如果将基本类型 `int[]` 属性拼接到一个单元格中，呈现的将是数组对象的 `toString` 文本（例如 `[I@1a2b3c4d`），而不是数字，因为拼接操作作用于每个元素的字符串形式，而基本类型数组被视为单个不透明元素。
{{% /alert %}}

### **代码示例 3 — 比较默认呈现与单单元格呈现**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

默认标记会沿 B 列向下将每个元素填入一个单元格，而 `arrayassingle` 标记则将同一数组合并到 C 列的单个单元格中：

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注意事项和最佳实践**

使用 `arrayassingle` 和 `arraydelimiter` 属性时，请注意以下事项：
- 属性值采用 `name:value` 形式。`arrayassingle=true` 这样的等号形式无法识别，并会静默回退到默认展开行为。
- 使用逗号分隔属性且不要留空格；逗号后的空格会使分隔符值偏移一个字符（参见上面的警告）。
- `arraydelimiter` 的值可以是紧跟在冒号后直接写入的单个字符，也可以是用双引号括起来的多字符字符串。
- 省略 `arraydelimiter` 时，元素将用逗号拼接。
- 绑定包含数组属性读取方法的公共 JavaBean 对象的 `java.util.List`。仅使用单个 JavaBean 对象或公共字段会使标记无法解析。
- 将数组属性保持为 `String[]`；拼接基本类型 `int[]` 时会呈现其 `toString` 文本（参见上面的说明）。
- 将智能标记放在宽度足以显示最终拼接字符串的单元格中；否则，根据格式不同，内容可能会在视觉上溢出到相邻单元格。

## 相关文章
- [在 Aspose.Cells for Java 中向数据透视表添加筛选字段](/cells/zh/java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Java 中为数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/java/change-page-field-layout/)
- [在 Aspose.Cells for Java 中将迷你图转换为图像和 HTML](/cells/zh/java/convert-sparkline-to-image-and-html/)
- [将 Excel 转换为 OFD 格式](/cells/zh/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}