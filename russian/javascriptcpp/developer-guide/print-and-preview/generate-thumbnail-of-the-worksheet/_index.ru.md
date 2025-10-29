---
title: Создание миниатюры листа с помощью JavaScript через C++
linktitle: Генерация миниатюры листа
type: docs
weight: 110
url: /ru/javascript-cpp/generate-thumbnail-of-the-worksheet/
description: Узнайте, как создавать миниатюрное изображение из листа с помощью Aspose.Cells for JavaScript на C++. Создавайте небольшие изображения для предварительного просмотра в документах и презентациях.
---

{{% alert color="primary" %}} 

Генерация миниатюр листов может быть полезна. Миниатюра - это небольшое изображение, которое можно вставить в документ Word или презентацию PowerPoint, чтобы показать предварительный просмотр содержимого листа. Ее также можно добавить на веб-страницу с ссылкой для загрузки оригинального документа и использовать во многих других целях.

{{% /alert %}} 

Aspose.Cells for JavaScript на C++ позволяет выводить листы в файловые изображения, что делает создание миниатюр простым. Ниже приведён пример кода, показывающий, как выводить листы в файлы изображений.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Generate Worksheet Thumbnail Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Thumbnail</button>
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

            // Instantiate and open an Excel file from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Set the vertical and horizontal resolution
            imgOptions.verticalResolution = 200;
            imgOptions.horizontalResolution = 200;

            // One page per sheet is enabled
            imgOptions.onePagePerSheet = true;

            // Set desired thumbnail dimensions (converted to a property assignment)
            imgOptions.desiredSize = [600, 600, true];

            // Get the first worksheet
            const sheet = book.worksheets.get(0);

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateThumbnailOfWorksheet.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Thumbnail Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Thumbnail generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
