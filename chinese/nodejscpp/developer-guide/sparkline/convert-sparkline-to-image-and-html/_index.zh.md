---
title: 在 Aspose.Cells for Node.js via C++ 中将迷你图转换为图片和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 学习如何使用 Aspose.Cells 将迷你图渲染为独立图片以嵌入到单元格中，并使用 HtmlSaveOptions 将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, Node.js via C++, 迷你图, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图片, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格内的小型图表。Aspose.Cells 允许您将每个迷你图提取为独立图片（用于嵌入到其他单元格或外部报告中），也可以将整个包含迷你图的工作表导出为 HTML，以便在浏览器中分发。本文使用的 `cell.embeddedImage` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是一种在工作表中直接可视化趋势的紧凑方式。虽然 Excel 用户可以在原位查看它们，但许多实际场景要求迷你图离开单元格——例如，嵌入到其他单元格中作为静态图片、附加到自动发送的电子邮件中，或作为发布到 Web 的 HTML 报告的一部分进行渲染。

Aspose.Cells 支持这两种操作。`Sparkline.toImage` 方法可将单个迷你图渲染到流中，生成的字节可以分配给 `cell.embeddedImage`，从而使图片存储在工作簿的单个单元格内。另外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将逐步介绍这两种工作流程。

## **工作流程 1 — 将迷你图渲染为图片并嵌入到单元格中**

在此工作流程中，您将构建一个工作表，其中包含一个小型源值区域，为该区域附加三个不同的迷你图组（折线、柱形和堆叠/胜负），将每组渲染为 PNG，并将这些 PNG 字节作为嵌入图片写入相邻的单元格。最终结果是一个 `.xlsx` 文件，其中同时包含实时迷你图及其渲染的图片对应物。

### **分步说明**

1. 定义工作目录并确保它存在于磁盘上。
2. 创建一个新的 `Workbook` 并获取对第一个 `Worksheet` 的引用。
3. 在单元格 `A1` 至 `E1` 中填充五个示例数值（例如，每天的销售额或温度读数）。
4. 通过调用 `worksheet.sparklineGroups.add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 锚定在 `F1`、数据区域为 `A1:E1` 的 `SparklineType.Line` 组。
   - 锚定在 `G1`、数据区域为 `A1:E1` 的 `SparklineType.Column` 组。
   - 锚定在 `H1`、数据区域为 `A1:E1` 的 `SparklineType.Stacked`（胜负）组。
5. 构建一个 `ImageOrPrintOptions` 实例，并将其 `ImageType` 设置为 `ImageType.Png`，以便将每个迷你图渲染为透明 PNG。
6. 对于三个组中的每一个，使用 `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)` 渲染其单个迷你图，将流转换为 `Buffer`（或 `Uint8Array`），并将这些字节分别分配给 `worksheet.cells["F2"].embeddedImage`、`worksheet.cells["G2"].embeddedImage` 和 `worksheet.cells["H2"].embeddedImage`。
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

// 在 F1（第 5 列，第 0 行）添加一个折线迷你图组
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// 在 G1（第 6 列，第 0 行）添加一个柱形迷你图组
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// 在 H1（第 7 列，第 0 行）添加一个盈亏（堆叠）迷你图组
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// 为 PNG 输出配置图像选项
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// 将折线迷你图转换为图像并嵌入到单元格 F2 中
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// 将柱形迷你图转换为图像并嵌入到单元格 G2 中
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// 将盈亏迷你图转换为图像并嵌入到单元格 H2 中
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// 将工作簿保存到磁盘
workbook.save("output_with_sparklines.xlsx");
```

上述代码生成的工作簿中，每个迷你图的可视化表示以两种形式重复：锚定在第 1 行的实时原生迷你图，以及嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于图片存储在文件内部，因此工作簿仍然是一个独立的自包含文件，可以通过电子邮件发送或存档，而不会破坏嵌入的图片引用。将每个迷你图组渲染为 PNG，将流转换为 `Buffer`，并将数组分配给目标单元格的 `embeddedImage` 属性——此分配操作使图片成为该单元格存储内容的一部分。

{{% alert color="primary" %}}
由于每个迷你图组都锚定到单个单元格，因此您可以通过索引器 `group.sparklines[0]` 访问它，而无需使用 `forEach` 进行枚举。这使得渲染代码保持简洁，并符合典型的"一个锚定单元格对应一个迷你图"模式。通过 `cell.embeddedImage` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流程 2 — 将包含迷你图的工作表导出为 HTML**

一旦工作簿包含实时迷你图（以及可选的嵌入图片对应物），就可以通过将工作表另存为 HTML 来将整个工作表发布到 Web。`HtmlSaveOptions` 类公开了控制此导出所需的选项；在此工作流程中，您将重用工作流程 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为干净的单页 HTML 文档。

### **分步说明**

1. 确保工作流程 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录的磁盘上可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions` 并将其 `exportActiveWorksheetOnly` 属性设置为 `true`，以便生成的 HTML 文件仅包含活动工作表，而不是整个工作簿。
4. 调用 `workbook.save("sparklines.html", htmlOptions)` 将 HTML 输出写入磁盘。

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上述代码将工作流程 1 中生成的包含迷你图的工作簿转换为可移植的 HTML 文件。迷你图将作为内联 SVG 或 PNG 渲染保留在生成的 HTML 中（具体取决于导出模式），因此最终用户可以在任何现代浏览器中查看趋势，而无需安装 Excel。通过将 `exportActiveWorksheetOnly` 设置为 `true`，可以避免意外发布隐藏的工作表或辅助数据——仅导出用户当前可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类提供了其他用于微调输出的属性，例如 `exportHiddenWorksheet`、`exportImagesAsBase64` 和 `encoding`。根据您的部署目标进行相应的调整。
{{% /alert %}}

## **API 摘要**

上述工作流程依赖于一小组协同工作的 Aspose.Cells API。

- `SparklineGroup` 和集合访问器 `worksheet.sparklineGroups` 用于声明每个迷你图组的类型（折线、柱形、堆叠）、数据区域和锚定单元格。在本文中，每个组都锚定到单个单元格，因此通过 `worksheet.sparklineGroups[i]` 访问该组。
- `Sparkline` 和索引器 `group.sparklines[0]` 返回组内的单个迷你图。由于示例中每个组恰好包含一个迷你图，因此不需要 `forEach` 循环。
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` 是将迷你图图片写入所提供的 `Stream` 的渲染方法。该方法返回 `void`；您可以在调用之后从流中读取字节。
- `cell.embeddedImage` 是一个 `Buffer`（或 `Uint8Array`）属性，用于在单个单元格内存储图片。它在 **Aspose.Cells 26.5 及更高版本**中可用，是用于将通过 `toImage` 渲染的迷你图回写到同一工作簿的推荐方式。
- `htmlSaveOptions.exportActiveWorksheetOnly`（一个 `bool`）将 HTML 导出限制为活动工作表。它是生成单页报告时 `HtmlSaveOptions` 上最常用的属性之一。
- `imageOrPrintOptions.imageType` 位于 `Aspose.Cells.Drawing` 命名空间中，用于选择使用 `toImage` 渲染以及将工作表打印为图片时使用的图片格式（例如 `ImageType.Png`）。

## **相关文章**

- [Aspose.Cells for Aspose.Cells for Node.js via C++ 中的迷你图](/cells/zh/nodejs-cpp/sparkline/)
- [在单元格中插入图片](/cells/zh/nodejs-cpp/inserting-an-image-into-a-cell/)
- [SmartMarker 单单元格数组渲染 | Aspose.Cells Node.js via C++](/cells/zh/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}