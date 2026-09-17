---
title: Aspose.Cells for Python via .NET 中的 Excel 照相机
linktitle: Aspose.Cells for Python via .NET 中的 Excel 照相机
description: 了解如何在 Aspose.Cells for Python via .NET 中使用 Excel 照相机，创建链接到单元格区域的动态图片，该图片会随源数据刷新并保留所有源格式。
keywords: Aspose.Cells, Python, Excel 照相机, 动态图片, 链接图片, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /zh/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一个工作表对象，它呈现单元格区域的实时图像，并像普通图片一样悬浮在绘图层上。Aspose.Cells 支持两种创建模式：一种是在源数据更改时自动刷新的动态图片，另一种是捕获区域一次性快照的静态图片。本文将介绍这两种方法，以便您可以选择最适合您布局的方案。

## 什么是 Excel 照相机？
Excel 照相机本质上是一个锚定在工作表绘图层上特定行和列的图片对象。与普通插入的图片不同，照相机通过 `"A1:F10"` 之类的 A1 引用样式公式链接到源区域。当该区域内的任何单元格发生变化时，照相机的图像会自动刷新以反映新内容。照相机保留源区域的完整格式——边框、背景颜色、字体和数字格式——因此单元格中可见的所有内容都会出现在照相机的图像中。这使得照相机特别适用于仪表板、摘要、侧边面板和报告布局，您希望在远程位置预览一个区域而无需滚动或重复数据。有两个注意事项：您必须在保存工作簿之前调用 `update_selected_value()`，并且文件将以 HTML 或 PDF 格式导出，因为这些格式依赖于嵌入的图像数据而不是实时重新计算。

## 方法 1 — 添加动态照相机图片
动态照相机是最常用的方法，也是最接近 Excel 内置照相机工具的方法。它的工作原理是添加一个没有初始图像内容的图片，然后为其分配一个引用源区域的 `formula`。分配公式后，调用 `update_selected_value()` 会刷新嵌入的图像数据，使其与所镜像的单元格保持同步。照相机不是通过专用类实现的——它完全基于标准的 `Picture` 类型构建。
关键 API 包括：
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 添加锚定在给定行和列的图片。将 `None` 传递给 `stream` 参数会创建一个空图片，作为动态照相机的占位符。该方法返回新图片的索引。
- `worksheet.pictures[index]` — 索引器访问，用于从集合中检索特定的 `Picture`。
- `picture.formula` — 一个字符串属性（get/set），保存照相机所镜像源区域的 A1 引用样式引用，例如 `"A1:F10"`。
- `picture.update_selected_value()` — 一个 void 方法，用于从 `formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存之前调用 `update_selected_value()`；否则导出的文件将不包含图片数据，照相机在渲染输出中将为空白。
{{% /alert %}}

以下代码创建一个工作簿，添加一个锚定在第 10 行第 6 列的空图片，通过 `formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Dynamic Camera: add an empty picture, link it via formula to A1:F10, then refresh
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## 方法 2 — 添加静态照相机图片
静态照相机本质上是单元格区域的一次性渲染预览。您无需维护实时链接，而是将区域渲染为图像字节一次，将这些字节包装在 `BytesIO` 中，然后将它们添加为常规图片。图像内容在创建时即固定，当源单元格更改时不会自动刷新。
关键 API 包括：
- `Cells.create_range(string address)` — 从 A1 引用样式地址（如 `"A1:F10"`）构建 `Range` 对象。
- `Range.to_image(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传递 `None` 使用默认渲染选项；存在重载以实现更精细的输出控制。
- `BytesIO(byte[] buffer)` — 将渲染的图像字节包装在 `BytesIO` 中，该 `BytesIO` 可馈入 `PictureCollection.add`。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 添加锚定在给定行和列的图片，这次传递渲染生成的 `BytesIO`。
以下代码创建一个工作簿，为 `A1:F10` 构建 `Range`，通过 `Range.to_image(null)` 将其渲染为图像字节，将字节包装在 `BytesIO` 中，添加锚定在第 10 行第 6 列的图片，然后保存工作簿。

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# 静态相机：构建 Range，渲染为字节，包装在 BytesIO 中，添加为图片
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## 在动态与静态之间选择
- **动态照相机：** 在每次重新计算时更新，在调用 `update_selected_value()` 后支持 HTML 和 PDF 导出，并在文件的整个生命周期内保留实时链接行为。
- **静态照相机：** 一次性渲染，从不更新，当您希望嵌入构建时的固定视觉快照而不是数据的实时镜像时非常有用。
Aspose.Cells 既支持基于 `picture.formula` 加 `update_selected_value()` 构建的自动刷新的动态照相机，也支持基于 `Range.to_image` 加 `BytesIO` 构建的一次性静态照相机。当您的输出需要与源单元格保持同步时，请选择动态方法；当您仅需要在构建时使用固定的视觉快照时，请选择静态方法。

{{< app/cells/assistant language="python-net" >}}