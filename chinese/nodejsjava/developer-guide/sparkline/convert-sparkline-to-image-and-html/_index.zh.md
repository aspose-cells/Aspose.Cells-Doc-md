---
title: 在 Aspose.Cells for Node.js via Java 中将迷你图转换为图片和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 了解如何使用 HtmlSaveOptions 将 Aspose.Cells 迷你图渲染为独立图片以嵌入单元格，以及将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, Node.js via Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /zh/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格内的小型图表。Aspose.Cells 支持您将每个迷你图提取为独立图片（用于嵌入到其他单元格或外部报告中），也可以将整个包含迷你图的工作表导出为 HTML，以便在浏览器中进行分发。本文中使用的 `Cell.EmbeddedImage` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是在工作表内直接可视化趋势的一种紧凑方式。虽然 Excel 用户可以在原位查看迷你图，但许多实际场景需要将迷你图移出单元格 —— 例如，将其作为静态图片嵌入到不同的单元格中、附加到自动发送的电子邮件中，或者作为发布到 Web 的 HTML 报告的一部分进行渲染。

Aspose.Cells 同时支持这两种操作。`Sparkline.toImage` 方法可将单个迷你图渲染到流中，生成的字节可以赋值给 `Cell.EmbeddedImage`，从而使图片存储在工作簿的单个单元格内。另外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将端到端地介绍这两种工作流程。

## **工作流程 1 — 将迷你图渲染为图片并嵌入到单元格中**

在此工作流程中，您将构建一个工作表，其中包含一小段源数值区域，为该区域附加三个不同的迷你图组（折线、柱形和堆叠/胜负），将每个组渲染为 PNG，并将这些 PNG 字节作为嵌入图片写入相邻的单元格。最终结果是一个 `.xlsx` 文件，其中既包含实时迷你图，也包含它们渲染后的图片对应物。

### **分步说明**

1. 定义工作目录并确保该目录在磁盘上存在。
2. 创建一个新的 `Workbook` 并获取第一个 `Worksheet` 的引用。
3. 在单元格 `A1` 到 `E1` 中填充五个数值样本（例如，每日销售额或温度读数）。
4. 通过调用 `worksheet.sparklineGroups.add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 锚定在 `F1` 的 `SparklineType.Line` 组，数据区域为 `A1:E1`。
   - 锚定在 `G1` 的 `SparklineType.Column` 组，数据区域为 `A1:E1`。
   - 锚定在 `H1` 的 `SparklineType.Stacked`（胜负）组，数据区域为 `A1:E1`。
5. 构建一个 `ImageOrPrintOptions` 实例，并将其 `ImageType` 设置为 `ImageType.Png`，以便每个迷你图都被渲染为透明 PNG。
6. 对于三个组中的每一个，使用 `group.sparklines[0].toImage(outputStream, imageOptions)` 渲染其单个迷你图，将 `ByteArrayOutputStream` 转换为 `byte[]`，并将该字节数组分别赋值给 `worksheet.cells.get("F2").setEmbeddedImage(...)`、`worksheet.cells.get("G2").setEmbeddedImage(...)` 和 `worksheet.cells.get("H2").setEmbeddedImage(...)`。
7. 将工作簿另存为 `output_with_sparklines.xlsx`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 在单元格 A1:E1 中填充示例数据
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 添加一个锚定在 F1（第 5 列，第 0 行）的折线迷你图组
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// 添加一个锚定在 G1（第 6 列，第 0 行）的柱形迷你图组
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// 添加一个锚定在 H1（第 7 列，第 0 行）的涨跌（堆叠）迷你图组
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// 配置 PNG 输出的图像选项
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// 将折线迷你图转换为图像并嵌入到 F2 单元格
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// 将柱形迷你图转换为图像并嵌入到 G2 单元格
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// 将涨跌迷你图转换为图像并嵌入到 H2 单元格
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// 将工作簿保存到磁盘
workbook.save("output_with_sparklines.xlsx");
```

上述代码生成的工作簿中，每个迷你图的视觉表示以两种形式重复出现：锚定在第 1 行的实时原生迷你图，以及直接嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于图片直接存储在文件内部，工作簿仍然是单一的自包含产物，可以通过电子邮件发送或归档，而不会破坏嵌入的图片引用。将每个迷你图组渲染为 PNG，将 `ByteArrayOutputStream` 转换为 `byte[]`，然后将该数组赋值给目标单元格的 `setEmbeddedImage` 属性 —— 该赋值操作正是将图片作为单元格存储内容的一部分写入的关键。

{{% alert color="primary" %}}
由于每个迷你图组都锚定到单个单元格，您可以通过索引器 `group.sparklines[0]` 来访问它，而无需使用 `forEach` 进行枚举。这样可以让渲染代码保持简洁，并符合典型的"每个锚定单元格对应一个迷你图"的模式。通过 `Cell.EmbeddedImage` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流程 2 — 将包含迷你图的工作表导出为 HTML**

一旦工作簿包含实时迷你图（以及可选的嵌入图片对应物），整个工作表就可以通过另存为 HTML 来发布到 Web。`HtmlSaveOptions` 类提供了控制此导出所需的配置项；在此工作流程中，您将重用工作流程 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为一个简洁的单页 HTML 文档。

### **分步说明**

1. 确保工作流程 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录中可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `ExportActiveWorksheetOnly` 属性设置为 `true`，以便生成的 HTML 文件仅包含活动工作表而非整个工作簿。
4. 调用 `workbook.save("sparklines.html", htmlOptions)` 将 HTML 输出写入磁盘。

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上述代码将工作流程 1 中生成的包含迷你图的工作簿转换为可移植的 HTML 文件。迷你图会根据导出模式以内联 SVG 或 PNG 渲染的形式保留在生成的 HTML 中，因此最终用户可以在任何现代浏览器中查看趋势，而无需安装 Excel。通过将 `ExportActiveWorksheetOnly` 设置为 `true`，可以避免意外发布隐藏的工作表或辅助数据 —— 只有当前对用户可见的工作表会被导出。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类提供了其他属性用于微调输出，例如 `ExportHiddenWorksheet`、`ExportImagesAsBase64` 和 `Encoding`。可根据您的部署目标进行相应调整。
{{% /alert %}}

## **API 摘要**

上述工作流程依赖于一组协同工作的 Aspose.Cells API。

- `SparklineGroup` 以及集合访问器 `worksheet.sparklineGroups` 用于声明每个迷你图组的类型（Line、Column、Stacked）、数据区域和锚定单元格。在本文中，每个组都锚定到单个单元格，因此通过 `worksheet.sparklineGroups[i]` 来访问组。
- `Sparkline` 和索引器 `group.sparklines[0]` 返回组内的单个迷你图。由于示例中每个组仅包含一个迷你图，因此无需 `forEach` 循环。
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` 是渲染方法，它将迷你图的图片写入所提供的 `OutputStream`。该方法返回 `void`；调用后您可以从流中读取字节。
- `Cell.EmbeddedImage` 是一个 `byte[]` 属性，用于在单个单元格内存储图片。该属性在 **Aspose.Cells 26.5 及更高版本**中可用，是将 `toImage` 渲染的迷你图往返写回同一工作簿的推荐方式。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（一个 `boolean`）将 HTML 导出限制为活动工作表。在生成单页报告时，它是 `HtmlSaveOptions` 上最常用的属性之一。
- `ImageOrPrintOptions.ImageType` 位于 `com.aspose.cells.drawing` 命名空间中，用于选择使用 `toImage` 渲染时以及将工作表打印为图片时所使用的图片格式（例如 `ImageType.Png`）。

## **相关文章**

- [Aspose.Cells for Node.js via Java 中的迷你图](/cells/zh/nodejs-java/sparkline/)
- [将图片插入单元格](/cells/zh/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker 单单元格数组渲染 | Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}