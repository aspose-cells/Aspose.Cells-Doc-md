---
title: 用 JavaScript 通过 C++ 创建透明 Excel 工作表图片
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /zh/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 生成 Excel 工作表的透明图片。
---

{{% alert color="primary" %}}

有时，您需要将工作表的图像生成为透明图像。您希望将透明度应用于所有没有填充颜色的单元格。Aspose.Cells提供[**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--)属性以将透明度应用于工作表图像。当此属性为**false**时，没有填充颜色的单元格将以白色绘制，当为**true**时，没有填充颜色的单元格将以透明绘制。

{{% /alert %}}

在下面的工作表图片中，没有应用透明度。没有填充颜色的单元格绘制成了白色。

|**没有透明度的输出：单元格背景为白色**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

而在下面的工作表图片中，应用了透明度。没有填充颜色的单元格是透明的。

|**启用透明度输出**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

下面的示例代码从 Excel 工作表生成一个透明的图像。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Create Transparent Image Example</title>
    </head>
    <body>
        <h1>Create Transparent Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Create Transparent PNG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = wb.worksheets.get(0);

            // Apply different image or print options
            const imgOption = new ImageOrPrintOptions();
            imgOption.imageType = ImageType.Png;
            imgOption.horizontalResolution = 200;
            imgOption.verticalResolution = 200;
            imgOption.onePagePerSheet = true;

            // Apply transparency to the output image
            imgOption.transparent = true;

            // Create image after applying image or print options
            const sr = new SheetRender(sheet, imgOption);
            const outputData = await sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateTransparentImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image created successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
