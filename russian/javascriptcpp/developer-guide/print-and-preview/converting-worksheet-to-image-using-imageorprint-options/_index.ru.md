---
title: Преобразование листа в изображение с помощью ImageOrPrint Options и JavaScript через C++
linktitle: Преобразование Листа в изображение с использованием параметров ImageOrPrint
type: docs
weight: 90
url: /ru/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Узнайте, как преобразовать лист в файл изображения и применить различные параметры изображений и печати с помощью Aspose.Cells for JavaScript через C++.   
---

{{% alert color="primary" %}}  
Этот документ разработан для подробного понимания того, как преобразовать лист в файл изображения и применить различные параметры изображения и печати для изображения, такие как разрешение, сжатие TIFF, формат изображения и качество страницы.  
{{% /alert %}}  

## **Сохранение листов в изображения - различные подходы**  

Иногда вам может понадобиться представить ваши рабочие листы в виде изображения. Вам может потребоваться вставлять изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вам нужен рабочий лист, отображенный как изображение, чтобы вы могли использовать его в другом месте. Aspose.Cells поддерживает конвертацию рабочих листов в файлы изображений. Также Aspose.Cells поддерживает установку различных параметров, таких как формат изображения, разрешение (вертикальное и горизонтальное), качество изображения и другие параметры изображения и печати.  

Возможно, вы попробуете автоматизацию Office, но у Office Automation есть свои недостатки. Есть несколько причин и проблем: безопасность, стабильность, масштабируемость и скорость, цена и функциональность. В общем, существует множество причин, главная из которых — что Microsoft настоятельно рекомендует не использовать автоматизацию Office через сторонние программы.  

В этой статье показано, как создать консольное приложение в Visual Studio. NET, выполнить преобразование листа в изображение с использованием различных параметров изображения и печати с помощью нескольких простых строк кода с использованием API Aspose.Cells.  

Класс [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) представляет лист, для которого необходимо рендерить изображения, и имеет перегруженный метод [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-), который может напрямую преобразовать лист в файлы изображений, указав желаемые атрибуты или параметры. Этот метод возвращает объект, который можно сохранить в виде файла изображения на диск или в поток. Поддерживаются различные форматы изображений, например BMP, PNG, GIF, JPEG, TIFF, EMF и другие.  

## **Использование Aspose.Cells для преобразования листа в изображение с использованием параметров ImageOrPrint.**  

### **Создание шаблонной книги в Microsoft Excel**  

Я создал новую книгу в MS Excel и добавил некоторые данные на первый лист. Теперь я преобразую лист шаблона файла "Лист1" в файл изображения "SheetImage.tiff" и применю различные параметры изображения, такие как горизонтальное и вертикальное разрешение, сжатие Tiff и т. Д.  

### **Загрузите и установите Aspose.Cells**  

Сначала вам нужно [скачать](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript через C++. Установите его на ваш компьютер для разработки. Все компоненты [Aspose](http://www.aspose.com/), при установке, работают в режиме оценки. Режим оценки не имеет ограничения по времени, он только вставляет водяные знаки в сгенерированные документы.  

### **Создайте проект**  

Запустите выбранную вами среду разработки (например, Visual Studio). Создайте новое консольное приложение.  

### **Добавьте ссылки**  

В этом проекте будет использоваться Aspose.Cells. Поэтому необходимо добавить ссылку на компонент Aspose.Cells в ваш проект. Например, добавьте ссылку на ….\Program Files\Aspose\Aspose.Cells for JavaScript через C++\Bin\Aspose.Cells.node  

### **Преобразовать лист в файл изображения**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **Опции конвертации**  

Можно сохранить конкретные страницы в изображение. Следующий код преобразует первый и второй рабочие листы в книге в изображения JPG.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **Конвертация изображения с помощью WorkbookRender**  

TIFF изображение может содержать более одного кадра. Вы можете сохранить всю книгу как один TIFF-файл с несколькими кадрами или страницами:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
