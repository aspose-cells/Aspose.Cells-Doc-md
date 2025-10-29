---
title: Конвертация листа в изображение — удаление пробелов вокруг данных с помощью JavaScript через C++
linktitle: Преобразование электронной таблицы в изображение  удалите пустое пространство вокруг данных
type: docs
weight: 40
url: /ru/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Узнайте, как преобразовать листы Microsoft Excel в изображения и удалить лишний whitespace вокруг данных с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Иногда вам может потребоваться представить изображения электронных таблиц в приложениях или веб-страницах. Например, вам может потребоваться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или в другой документ. По сути, вы хотите отобразить электронную таблицу в качестве изображения, чтобы ее можно было вставить в другие приложения. Aspose.Cells позволяет преобразовывать электронные таблицы Microsoft Excel в изображения.

{{% /alert %}}

## **Удалите пустое пространство вокруг данных**

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) API преобразует электронную таблицу в файл изображения с любыми указанными атрибутами, например, формат изображения, пагинированные листы и т.д. Поддерживается несколько форматов изображений, включая BMP, GIF, JPG, TIFF и EMF.

Когда вы используете функцию преобразования листа в изображение, выходное изображение по умолчанию имеет пустое пространство, то есть рамку вокруг нее. Вы можете удалить это, установив верхние, нижние, левые и правые поля макета страницы для исходного листа электронной таблицы на 0 и задав соответствующие [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) атрибуты.

Следующий фрагмент кода удаляет пустое пространство вокруг данных на выходном изображении.

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
