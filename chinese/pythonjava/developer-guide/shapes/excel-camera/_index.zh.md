---
title: Aspose.Cells for Python via Java 中的 Excel 照相机
linktitle: Aspose.Cells for Python via Java 中的 Excel 照相机
description: 了解如何在 Aspose.Cells for Python via Java 中使用 Excel 照相机，创建一个链接到单元格区域的动态图片，该图片会随源数据刷新并保留所有源格式。
keywords: Aspose.Cells, Python via Java, Excel 照相机, 动态图片, 链接图片, Picture.formula, updateSelectedValue, createRange, toImage, byte[] 数组
type: docs
weight: 90
url: /zh/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是工作表对象，用于呈现某个单元格区域的实时图像，并像普通图片一样浮动在绘图层上。Aspose.Cells for Python via Java 支持两种创建模式，一种是源数据更改时自动刷新的动态图片，另一种是捕获区域一次性快照的静态图片。本文将介绍这两种方法，以便您选择适合自己布局的方案。

## 什么是 Excel 照相机？
Excel 照相机本质上是锚定在工作表绘图层上特定行和列的图片对象。与常规插入的图片不同，照相机通过类似 `"A1:F10"` 的 A1 样式公式链接到源区域。只要该区域内的任何单元格发生更改，照相机的图像就会自动刷新以反映新内容。照相机保留源区域的完整格式，包括边框、背景颜色、字体和数字格式，因此单元格内可见的所有内容都会显示在照相机图像中。这使得照相机特别适用于仪表板、摘要、侧边栏和报告布局等场景，您希望在不滚动或重复数据的情况下预览远程区域。有两个注意事项：必须在保存工作簿之前调用 `updateSelectedValue()`，并且文件将以 HTML 或 PDF 格式导出，因为这些格式依赖于嵌入的图像数据而非实时重算。

## 方法 1 — 添加动态照相机图片
动态照相机是最常用的方法，最接近 Excel 内置的照相机工具。其工作原理是先添加一个不包含初始图像内容的图片，然后为其分配引用源区域的公式。分配公式后，调用 `updateSelectedValue()` 会刷新嵌入的图像数据，使其与所镜像的单元格保持同步。照相机并非通过专用类实现，而是完全构建在标准的 `Picture` 类型之上。
关键 API 如下：
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — 在给定的行和列处添加一个图片。为 `stream` 参数传递 `None` 会创建一个空图片，作为动态照相机的占位符。该方法返回新图片的索引。
- `worksheet.getPictures().get(index)` — 用于从集合中检索特定 `Picture` 的访问器。
- `Picture.getFormula()` / `Picture.setFormula()` — 获取或设置照相机所镜像源区域的 A1 样式引用，例如 `"A1:F10"`。
- `Picture.updateSelectedValue()` — 一个无返回值的方法，用于根据公式引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存之前调用 `updateSelectedValue()`；否则导出文件将不包含图片数据，照相机在渲染输出中会显示为空白。
{{% /alert %}}

以下代码创建一个工作簿，在第 10 行第 6 列处添加一个空图片，通过 `setFormula` 方法将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，并保存工作簿。

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# 动态相机：添加一个空图片，通过公式链接到 A1:F10，然后刷新
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## 方法 2 — 添加静态照相机图片
静态照相机本质上是单元格区域的一次性渲染预览。您无需维护实时链接，而是将区域一次性渲染为图像字节，将这些字节包装为 `byte[]` 数组，然后作为常规图片添加。图像内容在创建时被固定，当源单元格更改时不会自动刷新。
关键 API 如下：
- `Cells.createRange(String address)` — 从 A1 样式地址（如 `"A1:F10"`）构建一个 `Range` 对象。
- `Range.toImage(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传递 `None` 将使用默认渲染选项；存在重载以提供更精细的输出控制。
- `byte[] array(byte[] buffer)` — 将渲染的图像字节包装为 `byte[]` 数组，可传入 `PictureCollection.add`。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — 在给定的行和列处添加图片，这次传入由渲染生成的 `byte[]` 数组。
以下代码创建一个工作簿，为 `A1:F10` 构建一个 `Range`，通过 `Range.toImage(None)` 将其渲染为图像字节，将字节包装为 `byte[]` 数组，在第 10 行第 6 列处添加图片，并保存工作簿。

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# 静态相机：构建 Range，渲染为字节，包装在 ByteArrayInputStream 中，作为图片添加
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## 在动态与静态之间做出选择
- **动态照相机：** 在每次重新计算时更新，在调用 `updateSelectedValue()` 后支持 HTML 和 PDF 导出，并在文件生命周期内保持实时链接行为。
- **静态照相机：** 一次性渲染，永远不会更新，适用于希望在构建时嵌入固定的视觉快照而非数据的实时镜像。
Aspose.Cells for Python via Java 同时支持基于 `setFormula` 加 `updateSelectedValue()` 构建的动态自动刷新照相机，以及基于 `toImage` 加 `byte[]` 数组构建的静态一次性照相机。当输出需要与源单元格保持同步时，请选择动态方法；当仅需在构建时获取固定视觉快照时，请选择静态方法。

{{< app/cells/assistant language="python" >}}