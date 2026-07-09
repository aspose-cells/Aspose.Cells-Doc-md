---
title: 在 Aspose.Cells for Python via Java 中将迷你图转换为图片和 HTML
linktitle: Convert Sparkline to Image and HTML
description: 学习如何将 Aspose.Cells 迷你图渲染为独立的图片以便嵌入单元格，以及使用 HtmlSaveOptions 将包含迷你图的工作表导出为 HTML。
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, 渲染迷你图, 将迷你图转换为图片, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是放置在工作表单元格中的微型图表。Aspose.Cells 允许您将每个迷你图提取为独立的图片（以便嵌入到另一个单元格或外部报告中），还可以将整个包含迷你图的工作表导出为 HTML，以便在浏览器中分发。本文中使用的 `Cell.embedded_image` 属性在 **Aspose.Cells 26.5 及更高版本**中可用。
{{% /alert %}}

## **简介**

迷你图是一种在工作表内直接可视化趋势的紧凑方式。虽然 Excel 用户可以在原位查看它们，但在许多实际场景中，需要将迷你图从单元格中"取出"——例如，作为静态图片嵌入到不同的单元格中、附加到自动发送的电子邮件中，或者作为发布到 Web 的 HTML 报告的一部分进行渲染。

Aspose.Cells 支持这两种操作。`Sparkline.to_image` 方法可将单个迷你图渲染到流中，得到的字节可以赋值给 `Cell.embedded_image`，从而使图片存储在工作簿的单个单元格内。另外，`HtmlSaveOptions` 允许您将整个工作簿（包括所有迷你图）转换为独立的 HTML 文件。本文将逐步介绍这两种工作流程。

## **工作流程 1 — 将迷你图渲染为图片并嵌入到单元格中**

在此工作流程中，您将构建一个包含小型源值区域的工作表，为该区域附加三个不同的迷你图组（折线、柱形和堆叠/胜负），将每组渲染为 PNG，并将这些 PNG 字节作为嵌入图片写入相邻的单元格。最终结果是一个单独的 `.xlsx` 文件，其中既包含实时迷你图，也包含其渲染后的图片副本。

### **分步说明**

1. 定义一个工作目录并确保该目录在磁盘上存在。
2. 创建一个新的 `Workbook` 并获取第一个 `Worksheet` 的引用。
3. 使用五个示例数值（例如，每日销售额或温度读数）填充单元格 `A1` 至 `E1`。
4. 通过调用 `worksheet.sparkline_groups.add(...)` 向工作表添加三个 `SparklineGroup` 对象：
   - 一个锚定在 `F1`、数据区域为 `A1:E1` 的 `SparklineType.LINE` 组。
   - 一个锚定在 `G1`、数据区域为 `A1:E1` 的 `SparklineType.COLUMN` 组。
   - 一个锚定在 `H1`、数据区域为 `A1:E1` 的 `SparklineType.STACKED`（胜负）组。
5. 构建一个 `ImageOrPrintOptions` 实例，并将其 `image_type` 设置为 `ImageType.PNG`，以便将每个迷你图渲染为透明 PNG。
6. 对于三个组中的每一个，使用 `group.sparklines[0].to_image(byte_array_output_stream, image_options)` 渲染其单个迷你图，将 `ByteArrayOutputStream` 转换为 `byte[]`（或将 `to_byte_array()` 读取为 Python `bytes`），然后将字节分别赋值给 `worksheet.cells["F2"].embedded_image`、`worksheet.cells["G2"].embedded_image` 和 `worksheet.cells["H2"].embedded_image`。
7. 将工作簿另存为 `output_with_sparklines.xlsx`。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# 创建一个新工作簿并访问第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 在单元格 A1:E1 中填充示例数据
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# 添加锚定在 F1（第 5 列，第 0 行）的折线迷你图组
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# 添加锚定在 G1（第 6 列，第 0 行）的柱形迷你图组
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# 添加锚定在 H1（第 7 列，第 0 行）的盈亏（堆叠）迷你图组
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# 为 PNG 输出配置图像选项
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# 将折线迷你图转换为图像并嵌入到单元格 F2 中
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# 将柱形迷你图转换为图像并嵌入到单元格 G2 中
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# 将盈亏迷你图转换为图像并嵌入到单元格 H2 中
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# 将工作簿保存到磁盘
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

上述代码生成的工作簿中，每个迷你图的视觉表示以两种形式重复存在：锚定在第 1 行的实时原生迷你图，以及直接嵌入到第 2 行相邻单元格中的静态 PNG 图片。由于图片存储在文件内部，因此工作簿仍是一个独立的工件，可以通过电子邮件发送或存档，而不会破坏嵌入图片的引用。将每个迷你图组渲染为 PNG 后，将 `ByteArrayOutputStream` 转换为 `byte[]`（或使用 `to_byte_array()` 获取 Python `bytes` 对象），然后将该数组赋值给目标单元格的 `embedded_image` 属性——此赋值操作就是将图片作为单元格存储内容的一部分。

{{% alert color="primary" %}}
由于每个迷你图组都锚定在单个单元格上，您可以通过索引器 `group.sparklines[0]` 来访问它，而无需使用 `for` 循环进行枚举。这使得渲染代码保持简洁，并符合典型的"每个锚定单元格对应一个迷你图"的模式。通过 `Cell.embedded_image` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流程 2 — 将包含迷你图的工作表导出为 HTML**

一旦工作簿中包含实时迷你图（以及可选的嵌入图片副本），就可以通过将工作表另存为 HTML 来将其发布到 Web。`HtmlSaveOptions` 类提供了控制此导出所需的设置项；在此工作流程中，您将重用工作流程 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为一个简洁的单页 HTML 文档。

### **分步说明**

1. 确保工作流程 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录的磁盘上可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `export_active_worksheet_only` 属性设置为 `True`，这样生成的 HTML 文件将仅包含活动工作表，而不是整个工作簿。
4. 调用 `workbook.save("sparklines.html", html_options)` 将 HTML 输出写入磁盘。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

上述代码将工作流程 1 中包含迷你图的工作簿转换为一个可移植的 HTML 文件。迷你图在生成的 HTML 中保留为内联 SVG 或 PNG 渲染形式（具体取决于导出模式），因此最终用户可以在任何现代浏览器中查看趋势，而无需安装 Excel。通过将 `export_active_worksheet_only` 设置为 `True`，可以避免意外发布隐藏的工作表或辅助数据——仅导出用户当前可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类提供了其他一些用于微调输出的属性，例如 `export_hidden_worksheet`、`export_images_as_base64` 和 `encoding`。可根据部署目标的需要进行调整。
{{% /alert %}}

## **API 摘要**

上述工作流程依赖于一组协同工作的 Aspose.Cells API。

- `SparklineGroup` 以及集合访问器 `worksheet.sparkline_groups` 用于声明每个迷你图组的类型（折线、柱形、堆叠）、数据区域和锚定单元格。在本文中，每个组都锚定在单个单元格上，因此通过 `worksheet.sparkline_groups[i]` 访问该组。
- `Sparkline` 以及索引器 `group.sparklines[0]` 返回组内的单个迷你图。由于示例中每个组仅包含一个迷你图，因此不需要 `for` 循环。
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` 是将迷你图渲染到所提供的 `OutputStream`（例如 `ByteArrayOutputStream`）中的渲染方法。该方法返回 `void`；您需要在调用后从流中读取字节。
- `Cell.embedded_image` 是一个 `byte[]` 属性，用于在单个单元格中存储图片。它在 **Aspose.Cells 26.5 及更高版本**中可用，是将 `to_image` 渲染的迷你图回写到同一工作簿中的推荐方式。
- `HtmlSaveOptions.export_active_worksheet_only`（`bool` 类型）将 HTML 导出限制为活动工作表。在生成单页报告时，它是 `HtmlSaveOptions` 上最常用的属性之一。
- `ImageOrPrintOptions.image_type` 位于 `com.aspose.cells.drawing` 命名空间中，用于选择使用 `to_image` 进行渲染以及将工作表打印为图片时所使用的图片格式（例如 `ImageType.PNG`）。

## **相关文章**

- [Aspose.Cells for Python via Java 中的迷你图](/cells/zh/python-java/sparkline/)
- [将图片插入到单元格中](/cells/zh/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}