---
title: 用 JavaScript 通过 C++ 将图表转换为 SVG 格式的图像
linktitle: 将图表转换为SVG格式的图像
type: docs
weight: 240
url: /zh/javascript-cpp/converting-chart-to-image-in-svg-format/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 将图表转换为 SVG 格式图像。
---

{{% alert color="primary" %}}

可缩放矢量图形（SVG）是一种基于XML的二维图形格式，还支持交互和动画。SVG规范是由万维网联盟（W3C）自1999年以来制定的开放标准。

SVG图像及其行为是在XML文本文件中定义的。这意味着它们可以被搜索、索引、编写脚本和压缩。作为XML文件，SVG图像可以使用任何文本编辑器创建和编辑，但更常见的是使用绘图软件创建。

Aspose.Cells 可以将图表保存为 BMP、JPEG、PNG、GIF、SVG 等多种格式的图像。本文介绍了如何将图表保存为 SVG 格式。

{{% /alert %}}

以下示例代码解释了如何使用Aspose.Cells将图表转换为SVG格式图像。该代码加载源Microsoft Excel文件，然后将第一个工作表上找到的第一个图表保存为SVG。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Chart to SVG</title>
    </head>
    <body>
        <h1>Export First Chart to SVG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Set image or print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;

            // Export the chart to SVG format (returns image bytes)
            const imageData = chart.toImage(opts);

            // Create downloadable SVG blob
            const blob = new Blob([imageData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to SVG. Click the download link to download the SVG file.</p>';
        });
    </script>
</html>
```
