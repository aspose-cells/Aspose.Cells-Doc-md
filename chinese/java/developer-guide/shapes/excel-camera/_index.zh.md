---
title: Aspose.Cells for Java 中的 Excel 照相机
description: 了解如何在 Aspose.Cells for Java 中使用 Excel 照相机，创建一个链接到单元格区域的动态图片，该图片会随源数据刷新并保留所有源格式。
linktitle: Excel 照相机
keywords: Aspose.Cells, Java, Excel 照相机, 动态图片, 链接图片, Picture.Formula, updateSelectedValue, createRange, toImage, ByteArrayInputStream
type: docs
weight: 90
url: /zh/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一种工作表对象，它呈现某个单元格区域的实时图像，并像普通图片一样浮动在绘图层上。Aspose.Cells 支持两种创建模式：一种是会在源数据变化时自动刷新的动态图片，另一种是捕获区域一次性快照的静态图片。本文将逐步介绍这两种方法，以便您选择最符合版式需求的方式。

## 什么是 Excel 照相机？
Excel 照相机本质上是一个锚定在工作表绘图层上特定行与列的图片对象。与普通插入的图片不同，照相机通过类似 `"A1:F10"` 的 A1 样式公式链接到源区域。每当该区域内的任何单元格发生变化时，照相机的图像会自动刷新以反映新的内容。照相机保留源区域的完整格式，包括边框、背景颜色、字体和数字格式，因此单元格内可见的所有内容都会同步显示在照相机图像中。这使得照相机特别适用于仪表板、摘要、侧边栏和报表布局等场景，您可以在不滚动或重复数据的情况下显示远处区域的可见预览。有两个注意事项需要留意：在保存工作簿之前必须调用 `updateSelectedValue()`，并且文件将被导出为 HTML 或 PDF，因为这些格式依赖于嵌入的图像数据而非实时重算。

## 方法 1 — 添加动态照相机图片
动态照相机是最常用的方法，也是最接近 Excel 内置照相机工具的实现方式。它的工作方式是先添加一张没有初始图像内容的图片，然后为其分配一个引用源区域的 `Formula`。在分配公式后，调用 `updateSelectedValue()` 会刷新嵌入的图像数据，使其与所映射的单元格保持同步。照相机并非通过专门的类实现，而是完全基于标准的 `Picture` 类型构建。
关键 API 如下：
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 在指定的行和列位置添加图片。对 `stream` 参数传入 `null` 会创建一张空图片，作为动态照相机的占位符。方法返回新图片的索引。
- `worksheet.getPictures().get(index)` — 通过索引访问集合中的特定 `Picture`。
- `Picture.setFormula(String value)` — 设置照相机映射的源区域的 A1 样式引用，例如 `"A1:F10"`。
- `Picture.updateSelectedValue()` — 一个无返回值的方法，根据 `Formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存之前调用 `updateSelectedValue()`；否则导出文件将不包含图片数据，照相机在渲染输出中会显示为空白。
{{% /alert %}}

以下代码创建一个工作簿，在第 10 行第 6 列添加一张空图片，通过 `setFormula` 将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 动态照相机：添加一个空图片，通过公式将其链接到 A1:F10，然后刷新
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## 方法 2 — 添加静态照相机图片
静态照相机本质上是单元格区域一次性渲染的预览。它不会维持实时链接，而是先将区域渲染为图像字节，再将这些字节包装在 `ByteArrayInputStream` 中，作为普通图片添加。图像内容在创建时即固定下来，当源单元格变化时不会自动刷新。
关键 API 如下：
- `Cells.createRange(String address)` — 根据 A1 样式地址（例如 `"A1:F10"`）构建一个 `Range` 对象。
- `Range.toImage(ImageOrPrintOptions options)` — 将区域渲染为图像字节。传入 `null` 使用默认渲染选项；还提供重载以实现更精细的输出控制。
- `new ByteArrayInputStream(byte[] buffer)` — 将渲染的图像字节包装在 `ByteArrayInputStream` 中，可传入 `PictureCollection.add`。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 在指定的行和列位置添加图片，此时传入由渲染生成的 `ByteArrayInputStream`。
以下代码创建一个工作簿，为 `A1:F10` 构建一个 `Range`，通过 `Range.toImage(null)` 将其渲染为图像字节，将字节包装在 `ByteArrayInputStream` 中，在第 10 行第 6 列添加图片，然后保存工作簿。

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 静态相机：构建 Range，渲染为字节，包装在 ByteArrayInputStream 中，添加为图片
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## 在动态与静态之间选择
- **动态照相机：** 每次重算时都会更新，在调用 `updateSelectedValue()` 后支持 HTML 和 PDF 导出，并在文件的整个生命周期内保持实时链接行为。
- **静态照相机：** 一次性渲染，永不更新，适用于在构建时嵌入固定的视觉快照，而非数据的实时映射。
Aspose.Cells 同时支持基于 `Picture.Formula` 加 `updateSelectedValue()` 构建的自动刷新动态照相机，以及基于 `Range.toImage` 加 `ByteArrayInputStream` 构建的一次性静态照相机。当您的输出需要与源单元格保持同步时，请选择动态方案；当您仅在构建时需要固定的视觉快照时，请选择静态方案。

## Related Articles
- [Convert Sparkline to Image and HTML in Aspose.Cells for Java](/cells/zh/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}