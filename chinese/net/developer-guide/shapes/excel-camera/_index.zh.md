---
title: Aspose.Cells for .Net 中的 Excel 照相机
linktitle: Aspose.Cells for .Net 中的 Excel 照相机
description: 了解如何使用 Aspose.Cells for .Net 中的 Excel 照相机创建链接到单元格区域的动态图片，该图片会随源数据变化而刷新，并保留源区域的所有格式。
keywords: Aspose.Cells, .NET, Excel 照相机, 动态图片, 链接图片, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /zh/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一种工作表对象，可呈现单元格区域的实时图像，并像普通图片一样悬浮于绘图层上。Aspose.Cells 支持两种创建模式：一种是源数据发生变化时自动刷新的动态图片，另一种是捕获单元格区域的一次性快照的静态图片。本文将介绍这两种方法，帮助您选择适合自身布局的方式。

## 什么是 Excel 照相机？
Excel 照相机本质上是一个锚定于工作表绘图层中特定行和列的图片对象。与常规插入的图片不同，照相机通过 A1 样式公式（例如 `"A1:F10"`）链接到源区域。该区域中的任何单元格发生变化时，照相机的图像都会自动刷新，以反映新内容。照相机会保留源区域的全部格式，包括边框、背景颜色、字体和数字格式，因此单元格中显示的所有内容也会呈现在照相机图像中。因此，照相机尤其适用于仪表板、摘要、侧面板和报表布局，可用于预览工作表其他区域的内容，而无需滚动或重复数据。使用时需注意两点：保存工作簿前必须调用 `UpdateSelectedValue()`，且输出文件应采用 HTML 或 PDF 格式，因为这些格式依赖嵌入的图像数据，而不是实时重新计算。

## 方法 1 — 添加动态照相机图片
动态照相机是最常见的方法，也是与 Excel 内置照相机工具最接近的实现方式。其工作原理是添加一个不包含初始图像内容的图片，然后为该图片指定引用源区域的 `Formula`。指定公式后，调用 `UpdateSelectedValue()` 会刷新嵌入的图像数据，使其与所映射的单元格保持同步。照相机并非通过专用类实现，而是完全基于标准 `Picture` 类型构建。
主要 API 如下：
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 添加锚定于指定行和列的图片。为 `stream` 参数传入 `null` 会创建一个空图片，作为动态照相机的占位符。该方法返回新图片的索引。
- `worksheet.Pictures[index]` — 通过索引器从集合中获取特定的 `Picture`。
- `Picture.Formula` — 一个字符串属性（get/set），保存照相机所映射的源区域的 A1 样式引用，例如 `"A1:F10"`。
- `Picture.UpdateSelectedValue()` — 一个 void 方法，根据 `Formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
输出为 HTML 或 PDF 时，必须在保存前调用 `UpdateSelectedValue()`；否则，导出的文件将不包含图片数据，照相机在渲染结果中也会显示为空白。
以下代码创建一个工作簿，添加一个锚定在第 10 行第 6 列的空图片，通过 `Formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。
{{% /alert %}}

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// 动态相机：添加一张空图片，通过公式将其链接到 A1:F10，然后刷新
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## 方法 2 — 添加静态照相机图片
静态照相机本质上是单元格区域的一次性渲染预览。它不维护实时链接，而是将区域渲染为图像字节，将这些字节封装在 `MemoryStream` 中，然后将其作为常规图片添加。图像内容在创建时即已固定，源单元格发生变化时也不会自动刷新。
主要 API 如下：
- `Cells.CreateRange(string address)` — 根据 `"A1:F10"` 之类的 A1 样式地址构建 `Range` 对象。
- `Range.ToImage(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传入 `null` 将使用默认渲染选项；此外，还提供其他重载，以便更精细地控制输出。
- `new MemoryStream(byte[] buffer)` — 将渲染后的图像字节封装在 `MemoryStream` 中，以便传递给 `PictureCollection.Add`。
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 添加锚定于指定行和列的图片，此时传入渲染生成的 `MemoryStream`。
以下代码创建一个工作簿，为 `A1:F10` 构建 `Range`，通过 `Range.ToImage(null)` 将其渲染为图像字节，将这些字节封装在 `MemoryStream` 中，添加锚定在第 10 行第 6 列的图片，然后保存工作簿。

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// 静态相机：构建范围，渲染为字节，包装在 MemoryStream 中，然后添加为图片
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## 动态照相机与静态照相机的选择
- **动态照相机：** 每次重新计算时都会更新；调用 `UpdateSelectedValue()` 后支持导出为 HTML 和 PDF；在文件的整个生命周期内保持实时链接行为。
- **静态照相机：** 一次性渲染且永不更新，适用于在构建时嵌入固定视觉快照而非数据的实时镜像的场景。
Aspose.Cells 同时支持基于 `Picture.Formula` 和 `UpdateSelectedValue()` 构建的动态自动刷新照相机，以及基于 `Range.ToImage` 和 `MemoryStream` 构建、仅渲染一次的静态照相机。当输出需要与源单元格保持同步时，请选择动态方法；当只需要在构建时生成固定视觉快照时，请选择静态方法。

## 相关文章
- [在 Aspose.Cells for .Net 中将迷你图转换为图像和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)
- [将图像插入单元格](/cells/zh/net/inserting-an-image-into-a-cell/)
- [在 Aspose.Cells for .Net 中将筛选字段添加到数据透视表](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .Net 中将样式应用到数据透视表](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}