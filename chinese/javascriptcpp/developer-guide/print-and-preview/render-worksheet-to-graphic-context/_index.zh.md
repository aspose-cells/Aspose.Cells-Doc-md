---
title: 使用JavaScript通过C++将工作表渲染到图形上下文
linktitle: 将工作表呈现到图形上下文
type: docs
weight: 300
url: /zh/javascript-cpp/render-worksheet-to-graphic-context/
description: 学习如何使用C++的Aspose.Cells for JavaScript将工作表渲染到图形上下文，包括渲染到图像文件、屏幕和打印机。
---

{{% alert color="primary" %}}

Aspose.Cells 现可将工作表渲染为图形上下文。图形上下文可以是任何物理或虚拟的媒介，例如图像文件、屏幕或打印机。请使用以下两种方法之一将工作表渲染为图形上下文。

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

以下代码演示如何使用 Aspose.Cells 将工作表渲染到图形上下文。一旦执行，它会打印整个工作表，并用蓝色填充剩余空白区域，保存为 **OutputImage_out_.png** 文件。你可以使用任何源 Excel 文件尝试这段代码，也请阅读代码中的注释以便更好理解。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
