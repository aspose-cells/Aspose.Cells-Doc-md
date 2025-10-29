---
title: Преобразование листа в изображение и листа в изображение по страницам с помощью JavaScript через C++
linktitle: Преобразование листа в изображение и Лист в изображение по странице
type: docs
weight: 80
url: /ru/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Этот документ предназначен для предоставления разработчикам подробного понимания процесса преобразования листа в файл изображений и листов с несколькими страницами — в отдельные файлы изображений для каждой страницы.

Иногда может потребоваться представить рабочие листы в виде изображений, например, для использования их в приложениях или веб-страницах. Возможно, вам понадобится вставить изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вам нужно отобразить рабочий лист в виде изображения. Aspose.Cells поддерживает преобразование рабочих листов в файлы изображений Microsoft Excel. Также Aspose.Cells поддерживает преобразование рабочей книги в несколько файлов изображений, по одному на страницу.

Вы можете использовать автоматизацию Office для достижения этой цели, но у автоматизации Office есть свои недостатки. Существует несколько причин и проблем, например, безопасность, стабильность, масштабируемость/скорость, цена и функции. Короче говоря, есть много причин, но основная заключается в том, что сама компания Microsoft настоятельно рекомендует отказаться от автоматизации Office.
{{% /alert %}}

## **Используя Aspose.Cells for JavaScript через C++, чтобы преобразовать лист в файл изображения**

В этой статье объясняется, как создать консольное приложение, преобразовать лист в изображение и осуществить конвертацию листа в один образ для каждого листа с помощью API Aspose.Cells.

Вам нужно импортировать несколько ценных классов, связанных с функциями рендеринга, таких как [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/) и так далее. Класс [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) представляет лист, для которого создаются изображения, и содержит перегруженный метод [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-), который может напрямую преобразовать лист в файлы изображений со всеми установленными атрибутами или параметрами. Он может возвращать объект изображения, а также сохранять файл изображения на диск/поток. Поддерживается несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF и другие.

В этой статье объясняется, как:

- Преобразовать рабочий лист в изображение
- Преобразовать каждую страницу в рабочем листе в изображение

Это задача показывает, как использовать Aspose.Cells для преобразования рабочего листа из шаблонной рабочей книги в файл изображения.

### **Установка проекта**

1. Сначала [скачайте Aspose.Cells for JavaScript через C++](https://downloads.aspose.com/cells/javascript-cpp).
1. Установите его на ваш компьютер для разработки. Все компоненты [Aspose](http://www.aspose.com/), при установке, работают в режиме оценки. Режим оценки не имеет ограничения по времени, он только вставляет водяные знаки в сгенерированные документы. Теперь запустите ваше окружение для разработки и создайте новое консольное приложение. В этом примере используется консольное приложение на JavaScript, но вы можете использовать любую среду, которая интегрируется с JavaScript. Добавьте ссылку на Aspose.Cells в созданный проект.

### **Преобразовать рабочий лист в файл изображения**

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook.xlsx** (1 рабочий лист). Затем преобразуйте рабочий лист шаблона в файл изображения под названием SheetImage.jpg.

Ниже приведен используемый компонентом код для выполнения этой задачи. Он преобразует Sheet1 в **Testbook.xlsx** в файл изображения, чтобы показать, насколько легко осуществляется это преобразование.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## **Используя Aspose.Cells for JavaScript через C++ для преобразования листа в файл изображения по страницам**

В этом примере показано, как использовать Aspose.Cells для преобразования листа из шаблонной книги, которая содержит несколько страниц, в один файл изображения на каждой странице.

### **Конвертация листа в изображение по страницам**

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook2.xlsx** (1 рабочий лист).

Теперь преобразуйте рабочий лист шаблона Sheet1 в файлы изображений (по одному файлу на страницу). Поскольку я уже создал консольное приложение для выполнения этой задачи, я пропущу шаги создания этого консольного приложения и перейду непосредственно к шагам преобразования рабочего листа.

Следующий код используется компонентом для выполнения задачи. Он конвертирует Sheet1 из Testbook2.xlsx в файлы изображений по страницам.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
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
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
