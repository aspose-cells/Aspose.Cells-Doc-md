---
title: Excel Camera in Aspose.Cells for .NET
linktitle: Excel Camera
description: Learn how to use Excel Camera in Aspose.Cells for .NET to create a dynamic picture linked to a cell range that refreshes with the source data and preserves all source formatting.
keywords: Aspose.Cells, .NET, Excel Camera, dynamic picture, linked picture, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /zh/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一个工作表对象，用于呈现单元格区域的实时图像，并像普通图片一样悬浮在绘图层上。Aspose.Cells 支持两种创建模式：一种是动态图片，当源数据更改时自动刷新；另一种是静态图片，捕获区域的一次性快照。本文将介绍这两种方法，以便您选择适合自己布局的方式。

## What Is Excel Camera?
Excel 照相机本质上是一个锚定在工作表绘图层上特定行和列的图片对象。与普通插入的图片不同，照相机通过类似 `"A1:F10"` 的 A1 样式公式链接到源区域。每当该区域内任何单元格发生变化时，照相机的图像会自动刷新以反映新内容。照相机保留源区域的完整格式 — 边框、背景颜色、字体和数字格式 — 因此单元格内所有可见的内容也会出现在照相机的图像中。这使得照相机特别适用于仪表板、摘要、侧边栏和报告布局等场景，您希望在不必滚动或重复数据的情况下预览远程区域。两个注意事项适用：保存工作簿前必须调用 `UpdateSelectedValue()`，并且文件将导出为 HTML 或 PDF，因为这些格式依赖于嵌入的图像数据而不是实时重新计算。

## Method 1 — Add a Dynamic Camera Picture
动态照相机是最常用的方法，也是最接近 Excel 内置照相机工具的方式。它的工作原理是添加一个没有初始图像内容的图片，然后为其分配一个引用源区域的 `Formula`。分配公式后，调用 `UpdateSelectedValue()` 刷新嵌入的图像数据，使其与其镜像的单元格保持同步。照相机不是通过专用类实现的 — 它完全构建在标准 `Picture` 类型之上。
关键 API 如下：
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 在给定行和列处添加一个图片。将 `null` 传递给 `stream` 参数会创建一个空图片，作为动态照相机的占位符。该方法返回新图片的索引。
- `worksheet.Pictures[index]` — 索引器访问，用于从集合中检索特定的 `Picture`。
- `Picture.Formula` — 一个字符串属性（get/set），用于保存照相机镜像的源区域的 A1 样式引用，例如 `"A1:F10"`。
- `Picture.UpdateSelectedValue()` — 一个 void 方法，用于从 `Formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存前调用 `UpdateSelectedValue()`；否则导出的文件将不包含图片数据，照相机在渲染输出中将显示为空白。
{{% /alert %}}

以下代码创建一个工作簿，添加一个锚定在第 10 行第 6 列的空图片，通过 `Formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，并保存工作簿。

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Method 2 — Add a Static Camera Picture
静态照相机本质上是对单元格区域的一次性渲染预览。它不维护实时链接，而是将区域一次性渲染为图像字节，将这些字节包装在 `MemoryStream` 中，并将其作为常规图片添加。图像内容在创建时即固定，当源单元格更改时不会自动刷新。
关键 API 如下：
- `Cells.CreateRange(string address)` — 从 A1 样式地址（如 `"A1:F10"`）构建 `Range` 对象。
- `Range.ToImage(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传递 `null` 使用默认渲染选项；也存在重载以更精细地控制输出。
- `new MemoryStream(byte[] buffer)` — 将渲染的图像字节包装在 `MemoryStream` 中，可以提供给 `PictureCollection.Add`。
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 在给定行和列处添加图片，这次传递由渲染产生的 `MemoryStream`。
以下代码创建一个工作簿，为 `A1:F10` 构建一个 `Range`，通过 `Range.ToImage(null)` 将其渲染为图像字节，将字节包装在 `MemoryStream` 中，添加锚定在第 10 行第 6 列的图片，并保存工作簿。

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choosing Between Dynamic and Static
- **动态照相机：** 在每次重新计算时更新，在调用 `UpdateSelectedValue()` 后支持 HTML 和 PDF 导出，并在文件生命周期内保持实时链接行为。
- **静态照相机：** 一次性渲染，永远不会更新，当您希望在构建时嵌入固定的视觉快照而不是数据的实时镜像时非常有用。
Aspose.Cells 同时支持基于 `Picture.Formula` 加 `UpdateSelectedValue()` 构建的动态自动刷新照相机和基于 `Range.ToImage` 加 `MemoryStream` 构建的静态一次性照相机。当您的输出需要与源单元格保持同步时选择动态方法，当您仅需要在构建时获得固定视觉快照时选择静态方法。

## Related Articles
- [在 Aspose.Cells for .NET 中将迷你图转换为图像和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)
- [向单元格中插入图像](/cells/zh/net/inserting-an-image-into-a-cell/)
- [在 Aspose.Cells for .NET 中向数据透视表添加筛选字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .NET 中对数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表中的页面字段布局](/cells/zh/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}