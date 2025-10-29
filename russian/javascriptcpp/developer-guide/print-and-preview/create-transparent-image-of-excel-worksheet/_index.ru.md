---
title: Создать прозрачное изображение листа Excel с помощью JavaScript через C++
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ru/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: Узнайте, как создавать прозрачное изображение листа Excel с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображение вашего листа как прозрачное изображение. Вы хотите применить прозрачность ко всем ячейкам без цвета заливки. Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--) для применения прозрачности к изображению листа. Когда это свойство имеет значение **false**, то ячейки без цвета заливки рисуются белым цветом, а когда оно имеет значение **true**, то ячейки без цвета заливки рисуются прозрачными.

{{% /alert %}}

На следующем изображении листа прозрачность не была применена. Ячейки без цвета заливки рисуются белым цветом.

|**Вывод без прозрачности: фон ячейки белый**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Тогда как на следующем изображении листа прозрачность была применена. Ячейки без цвета заливки рисуются прозрачными.

|**Вывод со включенной прозрачностью**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Следующий образец кода генерирует прозрачное изображение из листа Excel.

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
