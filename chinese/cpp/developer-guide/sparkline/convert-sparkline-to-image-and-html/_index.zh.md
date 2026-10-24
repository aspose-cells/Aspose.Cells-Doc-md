---
title: 在 Aspose.Cells for C++ 中将迷你图转换为图像和 HTML
linktitle: 在 Aspose.Cells for C++ 中将迷你图转换为图像和 HTML
description: 了解如何将 Aspose.Cells 中的迷你图呈现为可嵌入单元格的独立图像，以及如何使用 HtmlSaveOptions 将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, C++, 迷你图, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图像, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是置于工作表单元格内的微型图表。Aspose.Cells 允许您将每个迷你图提取为独立图像（用于嵌入另一个单元格或外部报表），也可将整个包含迷你图的工作表导出为 HTML，以便在浏览器中分发。本文使用的 `Cell.EmbeddedImage` 属性在 **Aspose.Cells 26.5 及更高版本**中提供。
{{% /alert %}}

## **简介**
迷你图是一种直接在工作表单元格中呈现趋势的紧凑方式。Excel 用户可以在原位查看迷你图，但许多实际应用场景需要将迷你图移出单元格，例如将其作为静态图片嵌入另一个单元格、附加到自动发送的电子邮件中，或作为 HTML 报表的一部分呈现并发布到网络上。
Aspose.Cells 同时支持这两种操作。`Sparkline.ToImage` 方法将单个迷你图呈现为 `Vector<uint8_t>` 字节数组，生成的字节可赋给 `Cell.EmbeddedImage`，从而将图片存储在工作簿的单个单元格中。另外，`HtmlSaveOptions` 可将整个工作簿（包括迷你图）转换为自包含的 HTML 文件。本文将完整介绍这两种工作流。

## **工作流 1 — 将迷你图呈现为图像并嵌入单元格**
在此工作流中，您将构建一个包含少量源数据值的工作表，并将三个不同的迷你图组（Line、Column 和 Stacked/胜负）关联到该数据区域。随后，将每个组呈现为 PNG，再将这些 PNG 字节写入相邻单元格，作为嵌入图片保存。最终生成一个 `.xlsx` 文件，其中同时包含原生迷你图及其呈现后的静态图片副本。

### **分步说明**
1. 定义工作目录，并确保该目录存在于磁盘上。
2. 创建新的 `Workbook`，并获取第一个 `Worksheet` 的引用。
3. 使用五个示例数值填充 `A1` 到 `E1` 单元格（例如每日销售额或温度读数）。
4. 调用 `worksheet.SparklineGroups.Add(...)`，向工作表添加三个 `SparklineGroup` 对象：
   - 一个锚定于 `F1`、数据区域为 `A1:E1` 的 `SparklineType.Line` 组。
   - 一个锚定于 `G1`、数据区域为 `A1:E1` 的 `SparklineType.Column` 组。
   - 一个锚定于 `H1`、数据区域为 `A1:E1` 的 `SparklineType.Stacked`（胜负）组。
5. 创建 `ImageOrPrintOptions` 实例，并将其 `ImageType` 设置为 `ImageType.Png`，使每个迷你图呈现为透明 PNG。
6. 将工作簿另存为 `output_with_sparklines.xlsx`。

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

上述代码生成的工作簿将每个迷你图的视觉表示以两种形式呈现：一种是锚定在第 1 行的原生迷你图，另一种是直接嵌入第 2 行相邻单元格中的静态 PNG 图片。由于图片存储在文件内部，工作簿仍是单一的自包含文件，可以通过电子邮件发送或归档，而不会破坏嵌入图片引用。调用 `Sparkline.ToImage(ImageOrPrintOptions)` 可将每个迷你图组呈现为 PNG，该方法直接以 `Vector<uint8_t>` 形式返回图片字节。然后，将字节数组赋给目标单元格的 `EmbeddedImage` 属性；此赋值操作会使图片成为该单元格所存储内容的一部分。

{{% alert color="primary" %}}
由于每个迷你图组都锚定在一个单元格中，因此可通过索引器 `group.Sparklines[0]` 访问迷你图，而无需使用 `foreach` 进行枚举。这样可以简化呈现代码，并符合常见的“每个锚定单元格对应一个迷你图”模式。通过 `Cell.EmbeddedImage` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流 2 — 将迷你图工作表导出为 HTML**
工作簿中包含原生迷你图（以及可选的嵌入图片副本）后，即可通过另存为 HTML 将整个工作表发布到网络上。`HtmlSaveOptions` 类提供了控制导出所需的各项选项；在此工作流中，您将复用工作流 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为简洁的单页 HTML 文档。

### **分步说明**
1. 确保工作流 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录中可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `ExportActiveWorksheetOnly` 属性设置为 `true`，使生成的 HTML 文件仅包含活动工作表而非整个工作簿。
4. 调用 `workbook.Save("sparklines.html", htmlOptions)`，将 HTML 输出写入磁盘。

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

上述代码将工作流 1 生成的包含迷你图的工作簿转换为便于分发的 HTML 文件。迷你图会根据导出模式以内嵌 SVG 或 PNG 图像的形式保留在生成的 HTML 中，因此最终用户无需安装 Excel，即可在任意现代浏览器中查看趋势。将 `ExportActiveWorksheetOnly` 设置为 `true` 可避免意外发布隐藏的工作表或辅助数据，只会导出当前对用户可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类还提供其他可用于微调输出的属性，例如 `ExportHiddenWorksheet`、`ExportImagesAsBase64` 和 `Encoding`。请根据部署目标调整这些属性。
{{% /alert %}}

## **API 摘要**
上述工作流依赖一组相互配合的 Aspose.Cells API。
- `SparklineGroup` 和集合访问器 `worksheet.SparklineGroups` 用于声明各迷你图组的类型（Line、Column、Stacked）、数据区域和锚定单元格。本文中的每个组均锚定到一个单元格，因此可通过 `worksheet.SparklineGroups[i]` 访问相应的组。
- `Sparkline` 和索引器 `group.Sparklines[0]` 返回组内的单个迷你图。由于示例中的每个组恰好包含一个迷你图，因此无需使用 `foreach` 循环。
- `Sparkline.ToImage(ImageOrPrintOptions)` 是呈现迷你图的方法，直接以 `Vector<uint8_t>` 字节数组形式返回迷你图的图片。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（`bool` 类型）仅将活动工作表导出为 HTML。生成单页报表时，这是 `HtmlSaveOptions` 上最常用的属性之一。
- `ImageOrPrintOptions.ImageType` 位于 `Aspose.Cells.Drawing` namespace 中，用于选择图片格式（例如 `ImageType.Png`）。该格式适用于使用 `ToImage` 进行呈现以及将工作表打印为图像。

## **相关文章**
- [将图像插入单元格](/cells/zh/cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="cpp" >}}