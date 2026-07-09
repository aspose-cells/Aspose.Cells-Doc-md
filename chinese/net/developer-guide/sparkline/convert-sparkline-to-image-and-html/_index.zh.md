---
title: 在 Aspose.Cells for .NET 中将迷你图转换为图像和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 了解如何使用 HtmlSaveOptions 将 Aspose.Cells 迷你图渲染为独立图像以嵌入单元格，以及将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, .NET, 迷你图, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图像, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格内的小型图表。Aspose.Cells 允许您将每个迷你图提取为独立图像（用于嵌入到另一个单元格或外部报表中），也可以将整个包含迷你图的工作表导出为 HTML 以便在浏览器中分发。本文中使用的 `Cell.EmbeddedImage` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是一种直接在工作表中可视化趋势的紧凑方式。虽然 Excel 用户可以在工作表中直接看到它们，但许多实际场景需要迷你图离开单元格 —— 例如，作为静态图片嵌入到不同的单元格中、附加到自动发送的电子邮件中，或作为发布到 Web 的 HTML 报表的一部分进行渲染。

Aspose.Cells 同时支持这两种操作。`Sparkline.ToImage` 方法将单个迷你图渲染到一个流中，生成的字节可以赋值给 `Cell.EmbeddedImage`，从而使图片存储在工作簿的单个单元格内。此外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将端到端地介绍这两种工作流程。

## **工作流程 1 — 将迷你图渲染为图像并嵌入单元格**

在此工作流程中，您将构建一个工作表，其中包含一小段源数据区域，向该区域附加三个不同的迷你图组（折线、柱形和堆叠/胜负），将每个组渲染为 PNG，并将这些 PNG 字节作为嵌入图像写入相邻的单元格。最终结果是一个 `.xlsx` 文件，其中同时包含实时迷你图及其渲染后的图片对应版本。

### **分步说明**

1. 定义一个工作目录，并确保该目录存在于磁盘上。
2. 创建一个新的 `Workbook`，并获取第一个 `Worksheet` 的引用。
3. 在单元格 `A1` 到 `E1` 中填充五个数值样本（例如，每日销售额或温度读数）。
4. 通过调用 `worksheet.SparklineGroups.Add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 一个锚定在 `F1` 的 `SparklineType.Line` 组，数据区域为 `A1:E1`。
   - 一个锚定在 `G1` 的 `SparklineType.Column` 组，数据区域为 `A1:E1`。
   - 一个锚定在 `H1` 的 `SparklineType.Stacked`（胜负）组，数据区域为 `A1:E1`。
5. 构建一个 `ImageOrPrintOptions` 实例，并将其 `ImageType` 设置为 `ImageType.Png`，以便将每个迷你图渲染为透明 PNG。
6. 对于这三个组中的每一个，使用 `group.Sparklines[0].ToImage(memoryStream, imageOptions)` 渲染其单个迷你图，将 `MemoryStream` 转换为 `byte[]`，然后将数组分别赋值给 `worksheet.Cells["F2"].EmbeddedImage`、`worksheet.Cells["G2"].EmbeddedImage` 和 `worksheet.Cells["H2"].EmbeddedImage`。
7. 将工作簿保存为 `output_with_sparklines.xlsx`。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// 创建一个新工作簿并访问第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 在单元格 A1:E1 中填充示例数据
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// 在 F1（第 5 列，第 0 行）添加一个折线迷你图组
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// 在 G1（第 6 列，第 0 行）添加一个柱形迷你图组
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// 在 H1（第 7 列，第 0 行）添加一个盈亏（堆叠）迷你图组
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// 为 PNG 输出配置图像选项
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// 将折线迷你图转换为图像并将其嵌入到单元格 F2 中
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// 将柱形迷你图转换为图像并将其嵌入到单元格 G2 中
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// 将盈亏迷你图转换为图像并将其嵌入到单元格 H2 中
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// 将工作簿保存到磁盘
workbook.Save("output_with_sparklines.xlsx");
```

上述代码生成的工作簿中，每个迷你图的可视化表示以两种形式重复存在：锚定在第 1 行的实时原生迷你图，以及直接嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于这些图片位于文件本身内，因此工作簿保持为单一的自包含文件，可以通过电子邮件发送或归档，而不会破坏嵌入图像的引用。将每个迷你图组渲染为 PNG，将 `MemoryStream` 转换为 `byte[]`，然后将数组赋值给目标单元格的 `EmbeddedImage` 属性 —— 正是这种赋值操作使图片成为单元格存储内容的一部分。

{{% alert color="primary" %}}
由于每个迷你图组都锚定到单个单元格，因此可以通过索引器 `group.Sparklines[0]` 访问它，而无需使用 `foreach` 进行枚举。这使渲染代码保持简洁，并符合典型的"每个锚定单元格对应一个迷你图"的模式。通过 `Cell.EmbeddedImage` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流程 2 — 将包含迷你图的工作表导出为 HTML**

一旦工作簿包含实时迷你图（以及可选的嵌入图片对应版本），就可以通过将其另存为 HTML 来将整个工作表发布到 Web。`HtmlSaveOptions` 类提供了控制此导出所需的设置；在此工作流程中，您将重用工作流程 1 中生成的 `output_with_sparklines.xlsx` 文件，并将其转换为一个干净的、单页的 HTML 文档。

### **分步说明**

1. 确保工作流程 1 中生成的 `output_with_sparklines.xlsx` 文件在工作目录中的磁盘上可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `ExportActiveWorksheetOnly` 属性设置为 `true`，以便生成的 HTML 文件仅包含活动工作表，而不是整个工作簿。
4. 调用 `workbook.Save("sparklines.html", htmlOptions)` 将 HTML 输出写入磁盘。

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

上述代码将工作流程 1 中生成的包含迷你图的工作簿转换为可移植的 HTML 文件。迷你图根据导出模式作为内联 SVG 或 PNG 渲染保留在生成的 HTML 中，因此最终用户无需安装 Excel 即可在任何现代浏览器中查看这些趋势。通过将 `ExportActiveWorksheetOnly` 设置为 `true`，可以避免意外发布隐藏的工作表或辅助数据 —— 仅导出当前对用户可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类提供了其他属性用于微调输出，例如 `ExportHiddenWorksheet`、`ExportImagesAsBase64` 和 `Encoding`。可根据您的部署目标调整这些属性。
{{% /alert %}}

## **API 摘要**

上述工作流程依赖于一组协同工作的 Aspose.Cells API。

- `SparklineGroup` 和集合访问器 `worksheet.SparklineGroups` 用于声明每个迷你图组的类型（Line、Column、Stacked）、数据区域和锚定单元格。在本文中，每个组都锚定到单个单元格，因此通过 `worksheet.SparklineGroups[i]` 访问该组。
- `Sparkline` 和索引器 `group.Sparklines[0]` 返回组内的单个迷你图。由于示例中的每个组恰好包含一个迷你图，因此无需 `foreach` 循环。
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` 是渲染方法，用于将迷你图的图片写入提供的 `Stream`。该方法返回 `void`；您可以在调用之后从流中读取字节。
- `Cell.EmbeddedImage` 是一个 `byte[]` 属性，用于在单个单元格内存储图片。它在 **Aspose.Cells 26.5 及更高版本**中可用，是将通过 `ToImage` 渲染的迷你图往返转换回同一工作簿的推荐方式。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（一个 `bool`）将 HTML 导出限制为活动工作表。在生成单页报表时，它是 `HtmlSaveOptions` 上最常用的属性之一。
- `ImageOrPrintOptions.ImageType` 位于 `Aspose.Cells.Drawing` 命名空间中，用于选择图片格式（例如 `ImageType.Png`），在使用 `ToImage` 进行渲染时以及将工作表打印为图像时都会用到。

## **相关文章**

- [Aspose.Cells for .NET 中的迷你图](/cells/zh/net/sparkline/)
- [将图像插入单元格](/cells/zh/net/inserting-an-image-into-a-cell/)
- [SmartMarker 单单元格数组渲染 | Aspose.Cells .NET](/cells/zh/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}