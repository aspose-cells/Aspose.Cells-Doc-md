---
title: 指定如何在输出的PDF和图片中交叉字符串，用JavaScript via C++
linktitle: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 120
url: /zh/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: 学习如何通过指定交叉类型控制输出PDF/图片中的文本溢出，使用Aspose.Cells for JavaScript via C++。
---

## **可能的使用场景**

当单元格包含文本或字符串且其长度超过单元格宽度时，如果下一列的单元格为空或无内容，字符串会溢出。当你将 Excel 文件保存为 PDF/图片时，可以通过使用 [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype) 枚举值来控制此溢出，枚举值如下：

- **TextCrossType.Default**：显示文本，类似于 MS Excel，其取决于下一单元格。如果下一单元格为空，字符串将溢出或截断。

- **TextCrossType.CrossKeep**：像 MS Excel 导出PDF/图片时那样显示字符串。

- **TextCrossType.CrossOverride**：允许文本跨越其他单元格显示，并覆盖被跨越单元格中的文本。

- **TextCrossType.StrictInCell**: 仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/图像中如何跨越字符串**

以下示例代码加载示例Excel文件，并通过指定不同的 [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype) 来保存为PDF/图片格式。示例Excel文件和输出文件可以从以下链接下载：

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### 示例代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
