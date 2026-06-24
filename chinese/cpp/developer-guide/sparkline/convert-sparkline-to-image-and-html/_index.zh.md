---
title: 在 Aspose.Cells for C++ 中将迷你图转换为图像和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 了解如何使用 HtmlSaveOptions 将 Aspose.Cells 迷你图渲染为独立图像以嵌入到单元格中，以及将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, C++, 迷你图, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图像, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格内的小型图表。借助 Aspose.Cells，您可以将每个迷你图提取为独立图像（用于嵌入到其他单元格或外部报告中），也可以将整个包含迷你图的工作表导出为 HTML，以便通过浏览器进行分发。本文中使用的 `Cell.EmbeddedImage` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是一种在工作表内部直接可视化趋势的紧凑方式。虽然 Excel 用户可以在工作表中直接查看它们，但在许多实际场景中，需要将迷你图从单元格中提取出来——例如，将其作为静态图片嵌入到不同的单元格中、附加到自动发送的电子邮件中，或者作为发布到 Web 的 HTML 报告的一部分进行渲染。

Aspose.Cells 支持这两种操作。`Sparkline.ToImage` 方法可将单个迷你图渲染到流中，生成的字节可以赋值给 `Cell.EmbeddedImage`，以便将图片存储在工作簿的单个单元格内。另外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将逐步介绍这两种工作流。

## **工作流 1 — 将迷你图渲染为图像并嵌入到单元格中**

在此工作流中，您将构建一个包含少量源数值的工作表，为该区域附加三个不同的迷你图组（折线、柱形和堆叠/涨跌），将每个组渲染为 PNG，并将这些 PNG 字节写入相邻单元格作为嵌入图像。最终结果是一个 `.xlsx` 文件，其中同时包含实时迷你图及其渲染后的图片副本。

### **分步说明**

1. 定义一个工作目录并确保其存在于磁盘上。
2. 创建一个新的 `Workbook`，并获取对第一个 `Worksheet` 的引用。
3. 在单元格 `A1` 到 `E1` 中填充五个示例数值（例如，每日销售额或温度读数）。
4. 通过调用 `worksheet.SparklineGroups.Add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 一个 `SparklineType.Line` 组，锚定在 `F1`，数据区域为 `A1:E1`。
   - 一个 `SparklineType.Column` 组，锚定在 `G1`，数据区域为 `A1:E1`。
   - 一个 `SparklineType.Stacked`（涨跌）组，锚定在 `H1`，数据区域为 `A1:E1`。
5. 构建一个 `ImageOrPrintOptions` 实例，并将其 `ImageType` 设置为 `ImageType.Png`，以便将每个迷你图渲染为透明的 PNG。
6. 对于这三个组中的每一个，使用 `group.Sparklines[0].ToImage(memoryStream, imageOptions)` 渲染其单个迷你图，将 `MemoryStream` 转换为 `Vector<uint8_t>`，并将数组分别赋值给 `worksheet.Cells["F2"].EmbeddedImage`、`worksheet.Cells["G2"].EmbeddedImage` 和 `worksheet.Cells["H2"].EmbeddedImage`。
7. 将工作簿另存为 `output_with_sparklines.xlsx`。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

上述代码生成的工作簿中，每个迷你图的可视化表示都以两种形式重复出现：锚定在第 1 行的实时原生迷你图，以及直接嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于图片存储在文件本身内，因此工作簿仍然是一个独立的完整文件，可以通过电子邮件发送或归档而不会破坏嵌入的图像引用。将每个迷你图组渲染为 PNG，将 `MemoryStream` 转换为 `Vector<uint8_t>`，并将数组赋值给目标单元格的 `EmbeddedImage` 属性——正是该赋值使图片成为单元格存储内容的一部分。

{{% alert color="primary" %}}
由于每个迷你图组锚定到单个单元格，因此您可以通过索引器 `group.Sparklines[0]` 访问它，而无需使用 `foreach` 进行枚举。这使渲染代码保持简洁，并符合典型的"每个锚定单元格一个迷你图"模式。通过 `Cell.EmbeddedImage` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流 2 — 将包含迷你图的工作表导出为 HTML**

一旦工作簿包含实时迷你图（以及可选的嵌入图片副本），就可以通过将其另存为 HTML 来将整个工作表发布到 Web。`HtmlSaveOptions` 类提供了控制此导出所需的配置项；在本工作流中，您将重用工作流 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为一个干净的单页 HTML 文档。

### **分步说明**

1. 确保工作流 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录中可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `ExportActiveWorksheetOnly` 属性设置为 `true`，以便生成的 HTML 文件仅包含活动工作表，而不是整个工作簿。
4. 调用 `workbook.Save("sparklines.html", htmlOptions)` 将 HTML 输出写入磁盘。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

上述代码将工作流 1 中生成的包含迷你图的工作簿转换为一个可移植的 HTML 文件。迷你图会根据导出模式以内联 SVG 或 PNG 渲染形式保留在生成的 HTML 中，因此最终用户可以在任何现代浏览器中查看趋势，而无需安装 Excel。通过将 `ExportActiveWorksheetOnly` 设置为 `true`，可以避免意外发布隐藏工作表或辅助数据——只会导出用户当前可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类提供了其他用于微调输出的属性，例如 `ExportHiddenWorksheet`、`ExportImagesAsBase64` 和 `Encoding`。请根据您的部署目标进行相应调整。
{{% /alert %}}

## **API 摘要**

上述工作流依赖于一组协同工作的 Aspose.Cells API。

- `SparklineGroup` 和集合访问器 `worksheet.SparklineGroups` 用于声明每个迷你图组的类型（折线、柱形、堆叠）、数据区域和锚定单元格。在本文中，每个组都锚定到单个单元格，因此通过 `worksheet.SparklineGroups[i]` 访问组。
- `Sparkline` 和索引器 `group.Sparklines[0]` 返回组内的单个迷你图。由于示例中的每个组恰好包含一个迷你图，因此不需要 `foreach` 循环。
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` 是将迷你图图片写入所提供的 `Stream` 的渲染方法。该方法返回 `void`；您需要在调用之后从流中读取字节。
- `Cell.EmbeddedImage` 是一个 `Vector<uint8_t>` 属性，用于在单个单元格中存储图片。它在 **Aspose.Cells 26.5 及更高版本**中可用，是将通过 `ToImage` 渲染的迷你图往返到同一工作簿中的推荐方式。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（一个 `bool`）将 HTML 导出限制为活动工作表。它是生成单页报告时 `HtmlSaveOptions` 上最常用的属性之一。
- `ImageOrPrintOptions.ImageType` 位于 `Aspose.Cells.Drawing` 命名空间中，用于选择图片格式（例如 `ImageType.Png`），在通过 `ToImage` 渲染以及将工作表打印为图像时使用。

## **相关文章**

- [Aspose.Cells for Aspose.Cells for C++ 中的迷你图](/cells/zh/cpp/sparkline/)
- [在单元格中插入图像](/cells/zh/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker 单单元格数组渲染 | Aspose.Cells for C++](/cells/zh/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}