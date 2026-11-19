---
title: Smart Markers 在页眉和页脚中 | Aspose.Cells for Java
linktitle: 页眉和页脚智能标记 | Aspose.Cells
description: 使用双尖括号语法和 WorkbookDesigner.setEnableHeaderFooterMarkers 开关，配合 getter-bean 列表或 JSON 数据源，在页眉和页脚中放置 Smart Marker 占位符，并通过数据 URI 绑定图片，适用于 Aspose.Cells for Java。
keywords: Aspose.Cells for Java, Smart Markers, 页眉, 页脚, 页眉页脚 markers, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, getter bean, JSON 数据源, 数据绑定, 图片, data URI, Java
type: docs
weight: 196
url: /zh/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
页眉和页脚通常包含报告元数据，例如报告标题、报告期间、作者和部门。当这些信息已存在于用于填充工作簿的数据源中时，手动重复输入会产生不必要的冗余。
经典 Smart Marker 语法 `&=Source.Field` 会处理工作表主体单元格中的占位符。如果您通过 `PageSetup.setHeader` 或 `PageSetup.setFooter` 将经典 marker 放入页眉或页脚中，它仍会保持为纯文本，因为页眉和页脚字符串不属于 `WorkbookDesigner.process()` 所扫描的工作表单元格网格。
从 **Aspose.Cells for Java 26.11** 版本开始，`WorkbookDesigner` 的页眉/页脚 marker 选项默认为 `false`。调用 `designer.setEnableHeaderFooterMarkers(true)` 后再调用 `designer.process()`，即可解析写在页眉和页脚字符串中的 `<<Source.Field>>` 格式占位符。页眉和页脚占位符与主体 marker 使用相同的数据源。
每个页眉和页脚包含三个可寻址区域：
- 区域 `0` 为左半部分。
- 区域 `1` 为中间部分。
- 区域 `2` 为右半部分。
使用 `PageSetup.setHeader(int section, String value)` 和 `PageSetup.setFooter(int section, String value)` 设置这些区域。处理完成后，使用 `PageSetup.getHeader(int section)` 和 `PageSetup.getFooter(int section)` 获取已填充的文本。

{{% alert color="primary" %}}
占位符（例如 `<<Source.Field>>`）将字段值以文本形式插入到区域字符串中。图片通过 `(picture)` 后缀和 data-URI 值进行绑定。
{{% /alert %}}

## **通过 getter-bean 列表启用页眉/页脚 Markers**
在 **Aspose.Cells for Java 26.11** 中，使用以下步骤通过 getter-bean 列表解析页眉和页脚占位符：
1. 创建一个 `Workbook` 并获取索引为 `0` 的首个 `Worksheet`，例如通过 `workbook.getWorksheets().get(0)`。
2. 使用 `PageSetup.setHeader` 和 `PageSetup.setFooter` 将 `<<Source.Field>>` 占位符写入所需的页眉和页脚区域。
3. 定义一个公有（PUBLIC）的小型 bean 类，为每个占位符字段提供 getter 方法（例如 `getName()`），并选择与占位符中使用的源前缀相匹配的源名称。例如，名为 `node` 的源支持 `<<node.Name>>` 类型的占位符。此平台验证两条绑定规则：拥有公有字段的 bean 不绑定任何内容（引擎读取的是 getter，而非字段），以及包私有（PACKAGE-PRIVATE）类也不绑定任何内容 —— 反射机制仅识别公有类，而非公有的 bean 会导致 `process()` 抛出 NullPointerException。
4. 为该工作簿创建 `WorkbookDesigner` 实例。
5. 在处理前调用 `designer.setEnableHeaderFooterMarkers(true)`。
6. 使用 `designer.setDataSource("node", table)` 将列表及其源名称附加到设计器。
7. 调用 `designer.process()`。
8. 处理完成后，页眉和页脚文本中将不再存在占位符。使用 `PageSetup.getHeader` 和 `PageSetup.getFooter` 获取已填充完成的区域字符串。

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **使用 JSON 数据源**
当报告数据已以 JSON 格式提供时，可以使用 JSON 替代 getter-bean 列表。调用 `WorkbookDesigner.setJsonDataSource(String name, String json)` 即可附加数据源。
`name` 参数为占位符所使用的源名称。例如，名称 `node` 支持 `<<node.Company>>` 和 `<<node.Title>>` 类型的占位符。
将行数据直接传递给 `setJsonDataSource`：
- 支持一个行数组，例如包含一个或多个行对象的 JSON 数组。
- 也可直接传递单个行对象。
- 不要将行数据包装在具有命名顶层键的对象中，例如 `{"rows":[...]}`。这种包装形式并非本工作流预期的行优先输入结构。
同一 JSON 数据源可在一次 `designer.process()` 调用中同时填充两种 marker 类型：它可解析工作表主体单元格中的经典 `&=` marker，以及页眉和页脚区域中的双尖括号 `<<>>` 占位符。您仍需为页眉和页脚占位符启用 `EnableHeaderFooterMarkers` 才能解析它们。

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **开关行为与多行源语义**
`EnableHeaderFooterMarkers` 设置默认为 `false`，该开关仅控制页眉和页脚中的 `<<Source.Field>>` 占位符。当开关关闭时，`designer.process()` 仍可解析主体中的经典 `&=` marker，但页眉或页脚中的 `<<Source.Field>>` 占位符将保持为纯文本。
页眉或页脚区域是一整个字符串，而非重复区域。如果数据源包含多行数据，则首行数据的值将用于填充页眉和页脚。一旦解析完成，该值将成为普通页眉或页脚文本。在调用 `workbook.save(...)` 后，这些值依然保留在工作簿中，后续重新加载工作簿时仍会显示。
以下示例使用同一多行 bean 列表创建两个工作簿，以对比开关禁用和启用两种情况的行为差异。`plainDesigner` 保留占位符不变，而 `enabledDesigner` 使用首行数据进行解析。

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **将图片绑定到页眉或页脚**
`(picture)` 后缀用于将图片绑定到页眉或页脚区域。写入 `<<node.logo(picture)>>` 以指定图片位置，并将字段值作为 data URI 提供——即前缀 `data:image/png;base64,` 后跟图片字节的 Base64 编码文本。若仅提供裸 Base64 字符串而不带 `data:` 前缀，则无法嵌入图片。
调用 `designer.process()` 后：
1. 占位符将被替换为标准页眉/页脚图片代码 `&G`。由于该 marker 变为区域字符串中的代码，它可以嵌入更长文本中，例如 `Logo: <<node.logo(picture)>>`。
2. 图片字节将作为媒体部件嵌入到该工作表的页眉/页脚绘图层中，因此图片会随页眉或页脚一同打印。

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

打印时，Excel 将 `&G` 解释为页眉渲染指令；此时 `logo.png` 字节已嵌入 `HeaderFooterPicture.xlsx`，图片将在原占位符位置打印出来。
如需使用页眉和页脚 Smart Markers，请通过 `PageSetup.setHeader` 和 `PageSetup.setFooter` 将 `<<Source.Field>>` 占位符写入页眉或页脚的左、中、右三个区域。在调用 `designer.process()` 前，对 `WorkbookDesigner` 实例调用 `designer.setEnableHeaderFooterMarkers(true)`，并通过 `designer.setDataSource(name, list)`（传入 getter-bean 列表）或 `designer.setJsonDataSource(name, json)` 提供数据值。使用 `PageSetup.getHeader` 和 `PageSetup.getFooter` 获取已填充完成的区域内容。同一数据源可在一次处理过程中同时填充主体 markers 和页眉/页脚占位符。添加 `(picture)` 后缀并配合 data-URI 值即可将图片绑定到指定区域。

## 相关文章
- [SmartMarker 单元格数组渲染](/cells/zh/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}