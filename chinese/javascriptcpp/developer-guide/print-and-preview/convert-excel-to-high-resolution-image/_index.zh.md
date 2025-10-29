---
title: 使用JavaScript via C++将Excel转换为高分辨率图像
linktitle: 转换Excel到高分辨率图像
type: docs
weight: 100
url: /zh/javascript-cpp/convert-excel-to-high-resolution-image/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将Excel文件转换为高分辨率图像。
---

随着高分辨率屏幕的普及，默认在96 DPI下生成的图像往往模糊不清。为了确保在高分辨率屏幕上的清晰度，必须以更高的DPI生成图像。Aspose.Cells for JavaScript通过C++提供设置[**ImageOrPrintOptions.horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--)和[**ImageOrPrintOptions.verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--)的功能，让你可以从Excel文件中创建在高分辨率显示屏上看起来清晰的高质量图像。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Sheet to Image</title>
    </head>
    <body>
        <h1>Convert Worksheet to PNG Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Image</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create ImageOrPrintOptions and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 300;
            options.verticalResolution = 300;
            options.imageType = ImageType.Png;

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Create SheetRender instance
            const render = new SheetRender(sheet, options);

            // Generate image for the first page/index (0)
            const imageData = render.toImage(0);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
