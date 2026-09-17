---
title: Aspose.Cells for Node.js via C++ 中的 Excel 照相机
linktitle: Aspose.Cells for Node.js via C++ 中的 Excel 照相机
description: 了解如何在 Aspose.Cells for Node.js via C++ 中使用 Excel 照相机，创建一个链接到单元格区域的动态图片，该图片会随源数据刷新并保留所有源格式。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel 照相机, 动态图片, 链接图片, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /zh/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一个工作表对象，用于呈现单元格区域的实时图像，并像普通图片一样悬浮在绘图图层上。Aspose.Cells 支持两种创建模式：一种是在源数据发生变化时自动刷新的动态图片，另一种是捕获区域一次性快照的静态图片。本文将介绍这两种方法，以便您选择适合自身布局的方法。

## Excel 照相机是什么？
Excel 照相机本质上是一个图片对象，锚定在工作表绘图图层中的特定行和列上。与常规插入的图片不同，照相机通过 A1 样式的公式（例如 `"A1:F10"`）链接到源区域。每当区域内的任何单元格发生变化时，照相机的图像都会自动刷新以反映新内容。照相机保留源区域的完整格式，包括边框、背景色、字体和数字格式，因此单元格中所有可见内容也会显示在照相机图像中。这使照相机非常适用于仪表板、摘要、侧边面板和报告布局，使您无需滚动或重复数据即可查看其他区域的可见预览。需要注意两点：保存工作簿前必须调用 `updateSelectedValue()`，并且文件将导出为 HTML 或 PDF，因为这些格式依赖嵌入的图像数据，而不是实时重新计算。

## 方法一 — 添加动态照相机图片
动态照相机是最常用的方法，也是最接近 Excel 内置照相机工具的方法。其工作原理是先添加一个不含初始图像内容的图片，然后为其分配引用源区域的 `Formula`。分配公式后，调用 `updateSelectedValue()` 刷新嵌入的图像数据，使其与所镜像的单元格保持一致。照相机并非通过专用类实现，而是完全基于标准 `Picture` 类型构建。
关键 API 如下：
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — 将图片锚定在指定的行和列。为 `stream` 参数传递 `null` 会创建一个空图片，作为动态照相机的占位符。该方法返回新图片的索引。
- `pictures.get(index)` — 通过索引从集合中获取特定的 `Picture`。
- `Picture.formula` — 一个字符串属性（get/set），用于保存照相机所镜像源区域的 A1 样式引用，例如 `"A1:F10"`。
- `Picture.updateSelectedValue()` — 无返回值的方法，用于根据 `formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存前调用 `updateSelectedValue()`；否则，导出的文件将不包含图片数据，照相机在渲染输出中将显示为空白。
{{% /alert %}}

以下代码创建一个工作簿，添加一个锚定在第 10 行第 6 列的空图片，通过 `Formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 动态相机：添加一个空图片，通过公式链接到 A1:F10，然后刷新
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## 方法二 — 添加静态照相机图片
静态照相机本质上是对单元格区域执行一次性渲染得到的预览。它不维护实时链接，而是将区域一次性渲染为图像字节，再将这些字节封装到 `Buffer` 中，并作为普通图片添加。此后，图像内容在创建时即已固定，源单元格发生变化时不会自动刷新。
关键 API 如下：
- `Cells.createRange(address)` — 从 A1 样式地址（例如 `"A1:F10"`）构建一个 `Range` 对象。
- `Range.toImage(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传递 `null` 将使用默认渲染选项；还提供重载，以便更精细地控制输出。
- `new Buffer(byte[] buffer)` — 将渲染的图像字节封装到可供 `getPictures().add` 使用的 `Buffer` 中。
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — 将图片锚定在指定的行和列，此时传入渲染生成的 `Buffer`。
以下代码创建一个工作簿，为 `A1:F10` 构建一个 `Range`，通过 `range.toImage(null)` 将其渲染为图像字节，将这些字节封装在 `Buffer` 中，添加一个锚定在第 10 行第 6 列的图片，然后保存工作簿。

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 静态相机：构建 Range，渲染为字节，包装在 MemoryStream 中，作为图片添加
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## 在动态和静态之间进行选择
- **动态照相机：** 在每次重新计算时更新，调用 `updateSelectedValue()` 后支持 HTML 和 PDF 导出，并在文件的整个生命周期内保留实时链接行为。
- **静态照相机：** 执行一次性渲染且永不更新，适用于希望嵌入构建时生成的固定视觉快照，而不是数据的实时镜像的情况。
Aspose.Cells 同时支持基于 `Picture.formula` 和 `updateSelectedValue()` 构建的动态自动刷新照相机，以及基于 `Range.toImage` 和 `Buffer` 构建的静态一次性照相机。当输出需要与源单元格保持同步时，选择动态方法；仅需在构建时生成固定视觉快照时，选择静态方法。

{{< app/cells/assistant language="nodejs-cpp" >}}