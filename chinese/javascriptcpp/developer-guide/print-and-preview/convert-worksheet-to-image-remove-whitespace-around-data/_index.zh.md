---
title: 将工作表转换为图像——用JavaScript via C++去除数据周围的空白区域
linktitle: 将工作表转换为图像  删除数据周围的空白
type: docs
weight: 40
url: /zh/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将Microsoft Excel工作表转换为图像，并去除数据周围的空白区域。 
---

{{% alert color="primary" %}}

有时，您需要在应用程序或网页中呈现工作表图像。例如，您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档中。基本上，您希望将工作表呈现为图像，以便将其粘贴到其他应用程序中。Aspose.Cells 允许您将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) API 可将工作表转换为带有任何指定属性（例如图像格式、分页工作表等）的图像文件。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

使用工作表转图像功能时，默认情况下输出图像具有周围的空白（即边框）。您可以通过将源工作表的顶部、底部、左侧和右侧的页面设置边距设置为 0，并相应地指定 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) 属性来删除这些空白。

以下代码片段删除输出图像中的数据周围的空白。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
