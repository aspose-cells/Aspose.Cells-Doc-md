---
title: 在 Aspose.Cells for Python via .NET 中将迷你图转换为图像和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 了解如何在 Python via .NET 中使用 Aspose.Cells 将迷你图渲染为独立图像以嵌入单元格，并通过 HtmlSaveOptions 将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, Python via .NET, 迷你图, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图像, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格内的小型图表。Aspose.Cells 允许您将每个迷你图提取为独立图像（用于嵌入到其他单元格或外部报告中），也可以将整个包含迷你图的工作表导出为 HTML，以便通过浏览器进行分发。本文使用的 `cell.embedded_image` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是一种在工作表内直接可视化趋势的紧凑方式。虽然 Excel 用户可以在原位查看迷你图，但在许多实际场景中需要将迷你图移出单元格——例如，作为静态图片嵌入到其他单元格中、附加到自动发送的电子邮件中，或作为发布到 Web 的 HTML 报告的一部分进行渲染。

Aspose.Cells 支持上述两种操作。`sparkline.to_image` 方法可将单个迷你图渲染到一个流中，然后将生成的字节赋值给 `cell.embedded_image`，以便将图片存储在工作簿的单个单元格内。此外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将端到端地讲解这两种工作流程。

## **工作流程 1 — 将迷你图渲染为图像并嵌入到单元格中**

在此工作流程中，您将构建一个包含小段源数值区域的工作表，向该区域附加三种不同的迷你图组（Line、Column 和 Stacked/Win-Loss），将每个组渲染为 PNG，并将这些 PNG 字节作为嵌入图片写入相邻的单元格。最终结果是一个 `.xlsx` 文件，其中既包含实时迷你图，也包含它们渲染后的图片版本。

### **分步说明**

1. 定义工作目录并确保其在磁盘上存在。
2. 创建一个新的 `Workbook`，并获取第一个 `Worksheet` 的引用。
3. 使用五个示例数值（例如，每日销售额或温度读数）填充单元格 `A1` 至 `E1`。
4. 通过调用 `worksheet.sparkline_groups.add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 锚定在 `F1`、数据区域为 `A1:E1` 的 `SparklineType.LINE` 组。
   - 锚定在 `G1`、数据区域为 `A1:E1` 的 `SparklineType.COLUMN` 组。
   - 锚定在 `H1`、数据区域为 `A1:E1` 的 `SparklineType.STACKED`（盈亏）组。
5. 构建一个 `ImageOrPrintOptions` 实例，并将其 `image_type` 设置为 `ImageType.PNG`，以便将每个迷你图渲染为透明 PNG。
6. 对于三个组中的每一个，使用 `group.sparklines[0].to_image(memory_stream, image_options)` 渲染其单个迷你图，将 `BytesIO` 流转换为 `bytes` 对象，并将该数组分别赋值给 `worksheet.cells["F2"].embedded_image`、`worksheet.cells["G2"].embedded_image` 和 `worksheet.cells["H2"].embedded_image`。
7. 将工作簿另存为 `output_with_sparklines.xlsx`。

```python
import aspose.cells as ac

# 创建一个新的工作簿并访问第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 在 A1:E1 单元格中填充示例数据
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# 在 F1（列 5，行 0）添加一个折线迷你图组
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# 在 G1（列 6，行 0）添加一个柱形迷你图组
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# 在 H1（列 7，行 0）添加一个盈亏（堆叠）迷你图组
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# 配置 PNG 输出的图像选项
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# 将折线迷你图转换为图像并嵌入到 F2 单元格
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# 将柱形迷你图转换为图像并嵌入到 G2 单元格
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# 将盈亏迷你图转换为图像并嵌入到 H2 单元格
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# 将工作簿保存到磁盘
workbook.save("output_with_sparklines.xlsx")
```

上述代码会生成一个工作簿，其中每个迷你图的视觉表示以两种形式重复存在：锚定在第 1 行的实时原生迷你图，以及直接嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于图片直接存储在文件本身内，因此工作簿始终是一个独立的工件，可以通过电子邮件发送或归档，而不会破坏嵌入的图片引用。将每个迷你图组渲染为 PNG，将 `BytesIO` 流转换为 `bytes` 对象，并将字节赋值给目标单元格的 `embedded_image` 属性——正是该赋值操作使图片成为单元格存储内容的一部分。

{{% alert color="primary" %}}
由于每个迷你图组都锚定到单个单元格，您可以通过索引器 `group.sparklines[0]` 来访问它，而无需使用 `for` 循环进行枚举。这使得渲染代码保持简洁，并与典型的"每个锚定单元格一个迷你图"的模式相匹配。通过 `cell.embedded_image` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流程 2 — 将迷你图工作表导出为 HTML**

一旦工作簿中包含实时迷你图（以及可选的嵌入图片版本），就可以通过将工作簿另存为 HTML 来将整个工作表发布到 Web。`HtmlSaveOptions` 类公开了控制此导出所需的设置项；在本工作流程中，您将复用工作流程 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为一个干净的单页 HTML 文档。

### **分步说明**

1. 确保工作流程 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录中的磁盘上可用。
2. 将该文件加载到一个新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `export_active_worksheet_only` 属性设置为 `True`，以便生成的 HTML 文件仅包含活动工作表，而不是整个工作簿。
4. 调用 `workbook.save("sparklines.html", html_options)` 将 HTML 输出写入磁盘。

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

上述代码将工作流程 1 中包含迷你图的工作簿转换为便携式 HTML 文件。迷你图在生成的 HTML 中以内联 SVG 或 PNG 渲染的形式保留（取决于导出模式），因此最终用户无需安装 Excel 即可在任何现代浏览器中查看趋势。通过将 `export_active_worksheet_only` 设置为 `True`，您可以避免意外发布隐藏的工作表或辅助数据——仅导出当前对用户可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类还提供了其他用于微调输出的属性，例如 `export_hidden_worksheet`、`export_images_as_base64` 和 `encoding`。可根据您的部署目标进行调整。
{{% /alert %}}

## **API 摘要**

上述工作流程依赖于一组协同工作的 Aspose.Cells API。

- `SparklineGroup` 和集合访问器 `worksheet.sparkline_groups` 用于声明每个迷你图组的类型（Line、Column、Stacked）、数据区域和锚定单元格。在本文中，每个组都锚定到单个单元格，因此通过 `worksheet.sparkline_groups[i]` 来访问该组。
- `Sparkline` 和索引器 `group.sparklines[0]` 返回组内的单个迷你图。由于示例中的每个组恰好包含一个迷你图，因此不需要 `for` 循环。
- `sparkline.to_image(Stream, ImageOrPrintOptions)` 是渲染方法，它将迷你图的图片写入提供的流中。该方法返回 `None`；您需要在调用之后从流中读取字节。
- `cell.embedded_image` 是一个 `bytes` 属性，用于在单个单元格内存储图片。它在 **Aspose.Cells 26.5 及更高版本**中可用，是将以 `to_image` 渲染的迷你图回写到同一工作簿的推荐方式。
- `html_save_options.export_active_worksheet_only`（一个 `bool`）将 HTML 导出限制为活动工作表。在生成单页报告时，它是 `HtmlSaveOptions` 上最常用的属性之一。
- `image_or_print_options.image_type` 位于 `aspose.cells.drawing` 命名空间中，用于选择使用 `to_image` 进行渲染时以及将工作表打印为图像时所使用的图片格式（例如 `ImageType.PNG`）。

## **相关文章**

- [Aspose.Cells for Python via .NET 中的迷你图](/cells/zh/python-net/sparkline/)
- [在单元格中插入图像](/cells/zh/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker 单单元格数组渲染 | Aspose.Cells for Python via .NET](/cells/zh/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}