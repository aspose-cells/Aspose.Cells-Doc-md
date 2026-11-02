---
title: Aspose.Cells for JavaScript via C++ 中的 Excel 照相机
linktitle: Aspose.Cells for JavaScript via C++ 中的 Excel 照相机
description: 了解如何使用 Aspose.Cells for JavaScript via C++ 中的 Excel 照相机，创建与单元格区域链接的动态图片，该图片会随源数据刷新，并保留源区域的所有格式。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Excel 照相机, 动态图片, 链接图片, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /zh/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 照相机是一种工作表对象，可呈现单元格区域的实时图像，并像普通图片一样悬浮在绘图层上。Aspose.Cells 支持两种创建模式：一种是源数据发生变化时自动刷新的动态图片，另一种是捕获单元格区域单次快照的静态图片。本文将介绍这两种方法，帮助您选择适合自身布局的方式。

## 什么是 Excel 照相机？
Excel 照相机本质上是一个图片对象，锚定于工作表绘图层上的特定行和列。与常规插入的图片不同，照相机通过 `"A1:F10"` 等 A1 样式公式与源区域建立链接。该区域内的任何单元格发生变化时，照相机的图像都会自动刷新，以反映新内容。照相机会保留源区域的全部格式，包括边框、背景颜色、字体和数字格式，因此单元格中显示的所有内容也会呈现在照相机图像中。因此，在仪表板、摘要、侧面板和报表布局中，您可以利用照相机预览远处单元格区域，而无需滚动或重复数据。使用时需要注意两点：保存工作簿前必须调用 `updateSelectedValue()`，并且文件将导出为 HTML 或 PDF，因为这些格式依赖嵌入的图像数据，而不是实时重新计算。

## 方法 1 — 添加动态照相机图片
动态照相机是最常用的方法，与 Excel 内置的照相机工具最为接近。它通过添加一个不含初始图像内容的图片，然后为其分配引用源区域的 `formula` 来实现。分配公式后，调用 `updateSelectedValue()` 会刷新嵌入的图像数据，使其与映射的单元格保持同步。照相机并非通过专用类实现，而是完全基于标准 `Picture` 类型构建。
主要 API 包括：
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — 以指定的行和列作为左上角锚点添加图片。图像参数传入 `null` 时，会创建一个空图片，作为动态照相机的占位对象。该方法返回新图片的索引。
- `worksheet.getPictures().get(index)` — 从图片集合中获取指定的 `Picture`。
- `picture.formula` — 一个字符串属性，保存照相机所映射源区域的 A1 样式引用，例如 `"A1:F10"`。
- `picture.updateSelectedValue()` — 一个无返回值的方法，根据 `formula` 引用的单元格刷新嵌入的图像数据。

{{% alert color="primary" %}}
当输出格式为 HTML 或 PDF 时，必须在保存前调用 `updateSelectedValue()`；否则，导出的文件将不包含图片数据，照相机在渲染结果中也会显示为空白。
以下代码创建一个工作簿，添加一个锚定于第 10 行第 6 列的空图片，通过 `formula` 属性将其链接到源区域 `A1:F10`，刷新嵌入的图像数据，然后保存工作簿。
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // 动态摄像头：添加一张空图片，通过公式将其链接到 A1:F10，然后刷新
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## 方法 2 — 添加静态照相机图片
静态照相机本质上是单元格区域的一次性渲染预览。您无需维护实时链接，只需将区域一次性渲染为图像字节，将这些字节封装到 `Buffer` 中，然后将其作为常规图片添加。图像内容在创建时即被固定，源单元格发生变化后不会自动刷新。
主要 API 包括：
- `cells.createRange(address)` — 根据 `"A1:F10"` 等 A1 样式地址构建 `Range` 对象。
- `range.toImage(options)` — 将区域渲染为图像字节。传入 `null` 时使用默认渲染选项；此外，该方法还提供多个重载，以便更精细地控制输出。
- `Buffer.from(imageBytes)` — 将渲染后的图像字节封装到 `Buffer` 中，以便传递给 `worksheet.getPictures().add`。
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — 以指定的行和列作为左上角锚点添加图片，此次传入渲染生成的 `Buffer`。
以下代码创建一个工作簿，为 `A1:F10` 构建 `Range`，通过 `range.toImage(null)` 将其渲染为图像字节，将这些字节封装到 `Buffer` 中，添加锚定于第 10 行第 6 列的图片，然后保存工作簿。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // 静态摄像机：构建 Range，渲染为字节，使用 MemoryStream 包装，然后添加为图片
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## 动态照相机与静态照相机的选择
- **动态照相机：** 每次重新计算时都会更新；调用 `updateSelectedValue()` 后可导出为 HTML 和 PDF；并在文件的整个生命周期内保持实时链接特性。
- **静态照相机：** 一次性渲染且永不更新；如果您希望在构建时嵌入固定的视觉快照，而不是数据的实时镜像，则非常适合。
Aspose.Cells 既支持基于 `picture.formula` 和 `updateSelectedValue()` 构建的动态自动刷新照相机，也支持基于 `range.toImage` 和 `Buffer` 构建的静态单次渲染照相机。当输出需要与源单元格保持同步时，请选择动态方式；当您只需在构建时获取固定的视觉快照时，请选择静态方式。

## 相关文章
- [在 Aspose.Cells for JavaScript via C++ 中将迷你图转换为图像和 HTML](/cells/zh/javascript-cpp/convert-sparkline-to-image-and-html/)
- [在 Aspose.Cells for JavaScript via C++ 中向数据透视表添加筛选字段](/cells/zh/javascript-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for JavaScript via C++ 中对数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}