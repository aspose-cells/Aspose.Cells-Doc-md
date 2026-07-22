---
title: 在 Aspose.Cells for Java 中将迷你图转换为图像和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 学习如何使用 HtmlSaveOptions 将 Aspose.Cells 迷你图渲染为独立图像以嵌入单元格，以及将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, Java, 迷你图, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图像, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格内的小型图表。Aspose.Cells 允许您将每个迷你图提取为独立图像（以便嵌入到另一个单元格或外部报告中），还可以将整个包含迷你图的工作表导出为 HTML，以便在浏览器中分发。本文中使用的 `Cell.EmbeddedImage` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是一种直接在单元格内可视化趋势的紧凑方式。虽然 Excel 用户可以在工作表中直接看到它们，但许多实际场景需要迷你图"离开"单元格 —— 例如，作为静态图片嵌入到其他单元格中、附加到自动发送的电子邮件中，或作为发布到 Web 的 HTML 报告的一部分进行渲染。

Aspose.Cells 同时支持这两种操作。`Sparkline.toImage` 方法可将单个迷你图渲染到流中，生成的字节可以通过 `setEmbeddedImage` 赋值给 `Cell.EmbeddedImage`，从而将图片存储在工作簿的单个单元格内。另外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将逐步介绍这两种工作流程。

## **工作流程 1 — 将迷你图渲染为图像并嵌入到单元格中**

在此工作流程中，您将构建一个包含少量源值的工作表，将三个不同的迷你图组（折线、柱形和堆叠/盈亏）附加到该区域，将每组渲染为 PNG，并将这些 PNG 字节作为嵌入图片写入相邻单元格。最终结果是单个 `.xlsx` 文件，其中既包含活动的迷你图，也包含它们渲染后的图片副本。

### **分步说明**

1. 定义工作目录并确保它在磁盘上存在。
2. 创建一个新的 `Workbook` 并获取第一个 `Worksheet` 的引用。
3. 在单元格 `A1` 到 `E1` 中填充五个示例数值（例如，每日销售额或温度读数）。
4. 通过调用 `worksheet.getSparklineGroups().add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 锚定在 `F1` 的 `SparklineType.LINE` 组，数据区域为 `A1:E1`。
   - 锚定在 `G1` 的 `SparklineType.COLUMN` 组，数据区域为 `A1:E1`。
   - 锚定在 `H1` 的 `SparklineType.STACKED`（盈亏）组，数据区域为 `A1:E1`。
5. 构建一个 `ImageOrPrintOptions` 实例，并调用 `setImageType(ImageType.PNG)`，以便每个迷你图都渲染为透明 PNG。
6. 对于三个组中的每一个，使用 `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)` 渲染其单个迷你图，将 `ByteArrayOutputStream` 转换为 `byte[]`，然后分别通过 `worksheet.getCells().get("F2").setEmbeddedImage(...)`、`worksheet.getCells().get("G2").setEmbeddedImage(...)` 和 `worksheet.getCells().get("H2").setEmbeddedImage(...)` 分配该数组。
7. 调用 `workbook.save("output_with_sparklines.xlsx")` 将工作簿保存到磁盘。

```java
import com.aspose.cells.*;
import java.io.*;

// 创建一个新的工作簿并访问第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// 在单元格 A1:E1 中填充示例数据
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 添加一个锚定在 F1（列 5，行 0）的折线迷你图组
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// 添加一个锚定在 G1（列 6，行 0）的柱形迷你图组
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// 添加一个锚定在 H1（列 7，行 0）的盈亏（堆叠）迷你图组
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// 配置 PNG 输出的图像选项
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// 将折线迷你图转换为图像并嵌入到单元格 F2 中
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// 将柱形迷你图转换为图像并嵌入到单元格 G2 中
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// 将盈亏迷你图转换为图像并嵌入到单元格 H2 中
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// 将工作簿保存到磁盘
workbook.save("output_with_sparklines.xlsx");
```

上述代码生成的工作簿中，每个迷你图的可视化表示以两种形式重复：位于第 1 行的原始活动迷你图，以及直接嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于图片直接保存在文件内，因此工作簿仍然是一个独立的自包含工件，可以通过电子邮件发送或归档，而不会破坏嵌入的图片引用。将每个迷你图组渲染为 PNG，把 `ByteArrayOutputStream` 转换为 `byte[]`，并通过 `setEmbeddedImage(byte[])` 将数组分配给目标单元格的 `EmbeddedImage` 属性 —— 该赋值正是使图片成为单元格存储内容一部分的操作。

{{% alert color="primary" %}}
由于每个迷你图组都锚定到单个单元格，因此您可以通过索引器 `group.getSparklines().get(0)` 来访问它，而无需使用 `for` 循环进行枚举。这使得渲染代码保持简洁，并符合典型的"每个锚定单元格对应一个迷你图"的模式。通过 `setEmbeddedImage` 将图片字节存储到 `Cell.EmbeddedImage` 需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流程 2 — 将包含迷你图的工作表导出为 HTML**

一旦工作簿中包含活动的迷你图（以及可选的嵌入图片副本），就可以通过将工作表保存为 HTML 来将其发布到 Web。`HtmlSaveOptions` 类公开了控制此导出所需的选项；在此工作流程中，您将重用工作流程 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为简洁的单页 HTML 文档。

### **分步说明**

1. 确保工作流程 1 生成的 `output_with_sparklines.xlsx` 文件在您的工作目录中可用。
2. 将该文件加载到一个新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions` 并调用 `setExportActiveWorksheetOnly(true)`，以便生成的 HTML 文件仅包含活动工作表而非整个工作簿。
4. 调用 `workbook.save("sparklines.html", htmlOptions)` 将 HTML 输出写入磁盘。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上述代码将工作流程 1 中生成的包含迷你图的工作簿转换为可移植的 HTML 文件。迷你图在生成的 HTML 中保留为内联 SVG 或 PNG 渲染（取决于导出模式），因此最终用户可以在任何现代浏览器中查看趋势，而无需安装 Excel。通过 `setExportActiveWorksheetOnly(true)` 将 `ExportActiveWorksheetOnly` 设置为 `true`，可以避免意外发布隐藏工作表或辅助数据 —— 仅导出用户当前可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类提供了其他用于微调输出的属性，例如 `ExportHiddenWorksheet`、`ExportImagesAsBase64` 和 `Encoding`。根据您的部署目标需要进行调整。
{{% /alert %}}

## **API 摘要**

上述工作流程依赖于少量协同工作的 Aspose.Cells API。

- `SparklineGroup` 和集合访问器 `worksheet.getSparklineGroups()` 用于声明每个迷你图组的类型（折线、柱形、堆叠）、数据区域和锚定单元格。在本文中，每个组都锚定到单个单元格，因此通过 `worksheet.getSparklineGroups().get(i)` 访问该组。
- `Sparkline` 和索引器 `group.getSparklines().get(0)` 返回组内的单个迷你图。由于示例中每个组恰好包含一个迷你图，因此不需要 `for` 循环。
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` 是将迷你图的图片写入所提供的 `Stream` 中的渲染方法。该方法返回 `void`；调用后您可以从流中读取字节。
- `Cell.EmbeddedImage` 是一个 `byte[]` 属性（通过 `cell.setEmbeddedImage(byte[])` 分配），用于在单个单元格内存储图片。它在 **Aspose.Cells 26.5 及更高版本**中可用，并且是将通过 `toImage` 渲染的迷你图往返返回到同一工作簿中的推荐方式。
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` 将 HTML 导出限制为活动工作表。在生成单页报告时，它是最常用的 `HtmlSaveOptions` 属性之一。
- `ImageOrPrintOptions.setImageType(ImageType)` 位于 `com.aspose.cells.drawing` 包中，用于选择使用 `toImage` 渲染时以及将工作表打印为图像时所使用的图片格式（例如 `ImageType.PNG`）。

## **相关文章**

- [Aspose.Cells for Java 中的迷你图](/cells/zh/java/sparkline/)
- [将图像插入到单元格中](/cells/zh/java/inserting-an-image-into-a-cell/)
- [SmartMarker 单单元格数组渲染 | Aspose.Cells Java](/cells/zh/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}