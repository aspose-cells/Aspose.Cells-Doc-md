---
title: Aspose.Cells for Node.js via Java 中的 Excel 照相机
linktitle: Aspose.Cells for Node.js via Java 中的 Excel 照相机
description: 了解如何在 Aspose.Cells for Node.js via Java 中使用 Excel 照相机，创建链接到单元格区域的动态图片，使其能够随源数据自动刷新并保留所有源格式
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel 照相机, 动态图片, 链接图片, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /zh/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一个工作表对象，用于呈现单元格区域的实时图像，并像普通图片一样浮动在绘图层上。Aspose.Cells 支持两种创建模式：一种是动态图片，每当源数据发生变化时自动刷新；另一种是静态图片，对区域进行一次性的快照捕获。本文将逐一介绍这两种方法，方便你根据实际布局选择合适的方案。

## 什么是 Excel 照相机？
Excel 照相机本质上是一个锚定在工作表绘图层中特定行和列的图片对象。与普通插入的图片不同，照相机通过类似 `"A1:F10"` 的 A1 样式公式链接到源区域。只要该区域内的任何单元格发生变化，照相机的图像就会自动刷新以反映新的内容。照相机保留源区域的完整格式——边框、背景颜色、字体和数字格式——因此单元格内所有可见的内容都会在照相机图像中呈现。这使得照相机特别适用于仪表板、摘要、侧边栏和报表布局等场景，让你无需滚动或重复数据即可远程预览区域的可见内容。有两点需要注意：你必须在保存工作簿之前调用 `updateSelectedValue()`，并且文件将被导出为 HTML 或 PDF 格式，因为这些格式依赖嵌入的图像数据而不是实时重算。

## 方法 1 — 添加动态照相机图片
动态照相机是最常用的方式，也是最接近 Excel 内置照相机工具的实现。它的工作原理是先添加一个没有初始图像内容的图片，然后为其分配一个引用源区域的 `Formula`。公式分配完成后，调用 `updateSelectedValue()` 即可刷新嵌入的图像数据，使其与所镜像的单元格保持同步。照相机并不是通过专门的类来实现的——它完全基于标准的 `Picture` 类型构建。
关键 API 如下：
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 在指定的行和列位置添加一个图片。为 `stream` 参数传入 `null` 会创建一个空图片，作为动态照相机的占位符。该方法返回新图片的索引。
- `worksheet.getPictures().get(index)` — 通过索引访问集合中指定的 `Picture`。
- `Picture.Formula` — 一个字符串属性（`getFormula()`/`setFormula()`），用于保存照相机所镜像源区域的 A1 样式引用，例如 `"A1:F10"`。
- `Picture.updateSelectedValue()` — 一个无返回值的方法，用于根据 `Formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存之前调用 `updateSelectedValue()`；否则导出的文件将不包含图片数据，照相机在渲染输出中将显示为空白。
{{% /alert %}}

下面的代码创建一个工作簿，在第 10 行第 6 列添加一个空图片，通过 `Formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 动态相机：添加一个空图片，通过公式将其链接到 A1:F10，然后刷新
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## 方法 2 — 添加静态照相机图片
静态照相机本质上是对单元格区域进行一次性的渲染预览。它并不保持实时链接，而是将区域渲染为图像字节一次，将这些字节包装进 `ByteArrayInputStream`，然后作为普通图片添加。图像内容在创建时即被固定，源单元格发生变化时不会自动刷新。
关键 API 如下：
- `Cells.createRange(String address)` — 根据 A1 样式地址（例如 `"A1:F10"`）构建一个 `Range` 对象。
- `Range.toImage(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传入 `null` 使用默认渲染选项；该方法还有重载可用于更精细地控制输出。
- `new ByteArrayInputStream(byte[] buffer)` — 将渲染出的图像字节包装到 `ByteArrayInputStream` 中，以便传入 `PictureCollection.add`。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 在指定的行和列位置添加图片，此时传入的是渲染产生的 `ByteArrayInputStream`。
下面的代码创建一个工作簿，为 `A1:F10` 构建一个 `Range`，通过 `range.toImage(null)` 将其渲染为图像字节，将字节包装进 `ByteArrayInputStream`，在第 10 行第 6 列添加图片，然后保存工作簿。

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 静态相机: 创建 Range, 渲染为字节, 包装在 ByteArrayInputStream 中, 添加为图片
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## 在动态与静态之间做出选择
- **动态照相机：** 每次重算时都会更新，在调用 `updateSelectedValue()` 之后支持 HTML 和 PDF 导出，并在文件整个生命周期内保持实时链接行为。
- **静态照相机：** 一次性渲染，永不更新，适用于在构建时嵌入固定的视觉快照，而不是实时镜像源数据。
Aspose.Cells 同时支持基于 `Picture.Formula` 加 `updateSelectedValue()` 构建的动态自动刷新照相机，以及基于 `Range.toImage` 加 `ByteArrayInputStream` 构建的静态一次性照相机。当你的输出需要与源单元格保持同步时选择动态方案；当仅需在构建时获得一个固定的视觉快照时选择静态方案。

{{< app/cells/assistant language="nodejs-java" >}}