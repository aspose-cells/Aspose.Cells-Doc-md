---
title: 用JavaScript通过C++为工作表添加WordArt水印
linktitle: 管理文字艺术
type: docs
weight: 180
url: /zh/javascript-cpp/add-wordart-watermark-to-worksheet/
description: 学习如何使用Aspose.Cells for JavaScript via C++将WordArt作为背景水印添加到工作表中。
---

{{% alert color="primary" %}} 

使用WordArt为电子表格添加特殊文本效果，例如，将标题横跨文件顶部，装饰文本，并使文本适应预设形状，或将文本应用于Excel工作表作为背景水印。 WordArt成为您可以在电子表格中移动或定位以添加装饰的对象。

{{% /alert %}} 

以下示例显示如何添加文字艺术形状以设置工作表的背景水印。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [添加具有内置样式的艺术字文本](/cells/zh/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [锁定WordArt水印](/cells/zh/javascript-cpp/locking-wordart-watermark/)
- [将文本形状的文字设置为预设的WordArt样式](/cells/zh/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
