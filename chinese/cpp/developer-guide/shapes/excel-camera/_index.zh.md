---
title: Aspose.Cells for C++ 中的 Excel 相机
linktitle: Aspose.Cells for C++ 中的 Excel 相机
description: 了解如何在 Aspose.Cells for C++ 中使用 Excel 相机，创建与单元格区域链接的动态图片，该图片随源数据刷新并保留所有源格式。
keywords: Aspose.Cells, C++, Excel 相机, 动态图片, 链接图片, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /zh/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 相机是一个工作表对象，它呈现单元格区域的实时图像，并像普通图片一样浮动在绘图层上。Aspose.Cells 支持两种创建模式：一种是动态图片，每当源数据更改时自动刷新；另一种是静态图片，仅捕获区域的一次性快照。本文将介绍这两种方法，以便您可以根据布局选择适合的方案。

## 什么是 Excel 相机？
Excel 相机本质上是一个锚定在工作表绘图层上特定行和列的图片对象。与插入的常规图片不同，相机通过 A1 样式公式（如 `"A1:F10"`）链接到源区域。只要该区域内的任何单元格发生变化，相机的图像就会自动刷新以反映新内容。相机保留源区域的完整格式——边框、背景颜色、字体和数字格式——因此单元格内可见的所有内容也会出现在相机的图像中。这使得相机特别适用于仪表板、摘要、侧边面板和报表布局等场景，您可以在其中预览远程区域而无需滚动或重复数据。有两点需要注意：保存工作簿之前必须调用 `UpdateSelectedValue()`，并且文件将导出为 HTML 或 PDF，因为这些格式依赖于嵌入的图像数据而不是实时重新计算。

## 方法一 — 添加动态相机图片
动态相机是最常用的方法，与 Excel 内置的相机工具最为接近。它的工作原理是添加一个没有初始图像内容的图片，然后为其分配引用源区域的 `Formula`。分配公式后，调用 `UpdateSelectedValue()` 会刷新嵌入的图像数据，使其与所镜像的单元格保持同步。相机并非通过专用类实现——它完全构建在标准的 `Picture` 类型之上。
关键 API 如下：
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — 添加一个锚定在指定行和列的图片。传入空的 `Vector<uint8_t>()` 将创建一个空图片，作为动态相机的占位符。该方法返回新图片的索引。
- `worksheet.GetPictures().Get(int index)` — 按索引从集合中检索特定的 `Picture`。
- `Picture.SetFormula(U16String value)` — 设置相机所镜像的源区域的 A1 样式引用，例如 `U16String("A1:F10")`。
- `Picture.UpdateSelectedValue()` — 根据 `Formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出为 HTML 或 PDF 时，必须在保存之前调用 `UpdateSelectedValue()`；否则导出的文件将不包含图片数据，相机在渲染输出中将显示为空白。
{{% /alert %}}

以下代码创建一个工作簿，添加一个锚定在第 10 行第 6 列的空图片，通过 `Formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // 动态相机：添加一个空图片，通过公式将其链接到 A1:F10，然后刷新
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 方法二 — 添加静态相机图片
静态相机本质上是单元格区域的一次性渲染预览。它不维护实时链接，而是将区域渲染到 `Vector<uint8_t>` 字节缓冲区一次，并将该缓冲区直接传递给 `Pictures.Add(row, col, data)`。图像内容在创建时即固定，当源单元格更改时不会自动刷新。
关键 API 如下：
- `Cells.CreateRange(U16String address)` — 根据 A1 样式地址（如 `U16String("A1:F10")`）构建一个 `Range` 对象。
- `Range.ToImage(ImageOrPrintOptions options)` — 将区域渲染为 `Vector<uint8_t>` 字节缓冲区。传入 `nullptr` 使用默认渲染选项；也存在用于更精细控制输出的重载。
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — 添加锚定在指定行和列的图片，此时传入由 `Range.ToImage` 生成的字节缓冲区。
以下代码创建一个工作簿，为 `A1:F10` 构建一个 `Range`，通过 `Range.ToImage(nullptr)` 将其渲染为图像字节，添加锚定在第 10 行第 6 列的图片，然后保存工作簿。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // 静态相机：构建 Range，渲染为字节，作为图片添加
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 在动态和静态之间选择
- **动态相机：** 每次重新计算时都会更新，在调用 `UpdateSelectedValue()` 后支持 HTML 和 PDF 导出，并在文件整个生命周期内保持实时链接行为。
- **静态相机：** 一次性渲染，永不更新，当您需要在构建时嵌入固定的视觉快照而非数据的实时镜像时非常有用。
Aspose.Cells 同时支持基于 `Picture.Formula` 加 `UpdateSelectedValue()` 构建的自动刷新动态相机，以及基于 `Range.ToImage` 加 `Vector<uint8_t>` 构建的一次性静态相机。当您的输出需要与源单元格保持同步时选择动态方案；当您仅需要在构建时获得固定视觉快照时选择静态方案。

{{< app/cells/assistant language="cpp" >}}