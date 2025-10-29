---
title: Преобразовать Excel в Pdf, изображение и другие форматы
linktitle: Преобразования рабочих книг
type: docs
weight: 65
url: /ru/javascript-cpp/convert-workbook-to-different-formats/
description: Преобразуйте файлы Excel в Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML и многое другое с помощью JavaScript через C++.
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает конвертацию между множеством форматов. Технически, конвертация означает загрузку книги в одном формате файла и сохранение ее в другом.
{{% /alert %}}

## **Конвертировать книгу Excel в PDF**
Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As PDF Example</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Преобразовать рабочую книгу Excel в JPG**
Aspose.Cells поддерживает конвертацию файлов Excel в JPG. Ниже показан пример кода, как сохранить книгу в JPG.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert Workbook to JPG Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JPG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JPG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert workbook to JPG image
            const outputData = workbook.save(SaveFormat.Jpeg);
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image1.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JPG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the download link to get the JPG image.</p>';
        });
    </script>
</html>
```

## **Преобразование рабочей книги Excel в изображение**
Aspose.Cells поддерживает конвертацию файлов Excel в изображения. Ниже приведён пример кода, как сохранить книгу как изображение.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Convert Workbook to Images</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Images</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="downloads"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            document.getElementById('result').innerHTML = '<p>Converting workbook to images...</p>';
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define desired image formats
            const formats = [
                { fmt: SaveFormat.Bmp, name: 'Image1.bmp', mime: 'image/bmp' },
                { fmt: SaveFormat.Jpeg, name: 'Image1.jpg', mime: 'image/jpeg' },
                { fmt: SaveFormat.Png, name: 'Image1.png', mime: 'image/png' },
                { fmt: SaveFormat.Emf, name: 'Image1.emf', mime: 'image/emf' },
                { fmt: SaveFormat.Gif, name: 'Image1.gif', mime: 'image/gif' }
            ];

            const downloadsDiv = document.getElementById('downloads');
            downloadsDiv.innerHTML = '';

            // Convert and create download links for each image format
            for (const f of formats) {
                const outputData = workbook.save(f.fmt);
                const blob = new Blob([outputData], { type: f.mime });
                const url = URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.download = f.name;
                a.textContent = 'Download ' + f.name;
                a.style.display = 'block';
                downloadsDiv.appendChild(a);
            }

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the links below to download the images.</p>';
        });
    </script>
</html>
```

## **Преобразование рабочей книги Excel в XPS**
Формат документа XPS состоит из структурированной разметки XML, которая определяет макет документа и визуальное оформление каждой страницы, а также правила отображения для распределения, архивирования, отображения, обработки и печати документов.

Язык разметки для XPS является подмножеством XAML, что позволяет ему включать элементы векторной графики в документы, используя XAML для разметки примитивов Windows Presentation Foundation (WPF). Используемые элементы описаны в терминах путей и других геометрических примитивов.

Файл XPS, на самом деле, является файлом UNICODE ZIP-архива с использованием упаковочных соглашений Open Packaging Conventions, содержащий файлы, из которых состоит документ. Эти включают XML-файл разметки для каждой страницы, текст, встроенные шрифты, растровые изображения, 2D векторную графику, а также информацию о цифровом управлении правами. Содержимое файла XPS можно изучить, просто открыв его в приложении, которое поддерживает ZIP-файлы.

Начиная с Aspose.Cells 6.0.0, поддерживается преобразование Microsoft Excel в XPS.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render to XPS</title>
    </head>
    <body>
        <h1>Render Worksheet / Workbook to XPS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkSheet" style="display: none; margin-right: 10px;">Download Sheet XPS</a>
            <a id="downloadLinkWorkbook" style="display: none;">Download Workbook XPS</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XpsSaveOptions, SheetSet } = AsposeCells;

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
            const downloadLinkSheet = document.getElementById('downloadLinkSheet');
            const downloadLinkWorkbook = document.getElementById('downloadLinkWorkbook');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Render the sheet to XPS
            const options = new XpsSaveOptions();
            const sheetSet = new SheetSet([sheet.index]);
            options.sheetSet = sheetSet;
            const outputDataSheet = workbook.save(SaveFormat.Xps, options);
            const blobSheet = new Blob([outputDataSheet], { type: 'application/vnd.ms-xps' });
            downloadLinkSheet.href = URL.createObjectURL(blobSheet);
            downloadLinkSheet.download = 'out_printingxps.out.xps';
            downloadLinkSheet.style.display = 'inline-block';
            downloadLinkSheet.textContent = 'Download Sheet XPS';

            // Export the whole workbook to XPS
            const outputDataWorkbook = workbook.save(SaveFormat.Xps, new XpsSaveOptions());
            const blobWorkbook = new Blob([outputDataWorkbook], { type: 'application/vnd.ms-xps' });
            downloadLinkWorkbook.href = URL.createObjectURL(blobWorkbook);
            downloadLinkWorkbook.download = 'out_whole_printingxps.out.xps';
            downloadLinkWorkbook.style.display = 'inline-block';
            downloadLinkWorkbook.textContent = 'Download Workbook XPS';

            resultDiv.innerHTML = '<p style="color: green;">XPS files generated. Use the links above to download the sheet and workbook XPS files.</p>';
        });
    </script>
</html>
```

## **Конвертация Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells поддерживает конвертацию файлов Excel в Ods, Sxc и Fods. Ниже показан пример, как конвертировать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As Multiple Formats Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Save As ODS / SXC / FODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Download</button>
        <div style="margin-top: 10px;">
            <a id="downloadLinkOds" style="display: none; margin-right: 10px;">Download ODS</a>
            <a id="downloadLinkSxc" style="display: none; margin-right: 10px;">Download SXC</a>
            <a id="downloadLinkFods" style="display: none; margin-right: 10px;">Download FODS</a>
        </div>
        <div id="result" style="margin-top: 10px;"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ods file
            const outputOds = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([outputOds]);
            const downloadLinkOds = document.getElementById('downloadLinkOds');
            downloadLinkOds.href = URL.createObjectURL(blobOds);
            downloadLinkOds.download = 'Out.ods';
            downloadLinkOds.style.display = 'inline-block';
            downloadLinkOds.textContent = 'Download ODS File';

            // Save as sxc file
            const outputSxc = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([outputSxc]);
            const downloadLinkSxc = document.getElementById('downloadLinkSxc');
            downloadLinkSxc.href = URL.createObjectURL(blobSxc);
            downloadLinkSxc.download = 'Out.sxc';
            downloadLinkSxc.style.display = 'inline-block';
            downloadLinkSxc.textContent = 'Download SXC File';

            // Save as fods file
            const outputFods = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([outputFods]);
            const downloadLinkFods = document.getElementById('downloadLinkFods');
            downloadLinkFods.href = URL.createObjectURL(blobFods);
            downloadLinkFods.download = 'Out.fods';
            downloadLinkFods.style.display = 'inline-block';
            downloadLinkFods.textContent = 'Download FODS File';

            result.innerHTML = '<p style="color: green;">Files converted successfully! Click the download links to get the converted files.</p>';
        });
    </script>
</html>
```

## **Преобразование книги Excel в файлы MHTML**
MHTML объединяет обычный HTML с внешними ресурсами (то есть контентом, который обычно ссылается, таким как изображения, анимации, звук и т. д.) в один файл. Они используются для электронных писем с расширением файла .mht.

Aspose.Cells поддерживает чтение и запись файлов MHTML.

В приведенном ниже примере кода показано, как сохранить книгу в формате MHTML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            window.asposeCellsReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!window.asposeCellsReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a workbook and open the uploaded XLSX file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify the HTML Saving Options
            const sv = new HtmlSaveOptions(SaveFormat.MHtml);

            // Save the MHT file (returns binary data)
            const outputData = workbook.save(SaveFormat.MHtml, sv);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `${file.name}.out.mht`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">MHT file generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Преобразование книги Excel в HTML**
API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions), чтобы дать возможность управлять несколькими аспектами итогового HTML.

Приведенный ниже пример кода демонстрирует, как сохранить рабочую книгу в файл HTML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

## **Установка параметров изображения для HTML**
Начиная с версии 8.0.2, Aspose.Cells предоставил [**imageOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#imageOptions--) для класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions), что позволяет разработчикам задавать предпочтения по изображениям при сохранении таблиц в HTML.

Ниже приведены подробности некоторых настроек изображения, которые могут быть применены,

- [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/): указывает тип изображения. Обратите внимание, что все формы, включая диаграммы, отображаются как изображения в выходном HTML.
- [**quality**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#quality--): Определяет качество изображения от 0 до 100, когда [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) указан как Jpeg.
- [**verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--): получает или задает вертикальное разрешение изображения в точках на дюйм.
- [**horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--): получает или задает горизонтальное разрешение изображения в точках на дюйм.
- [**TiffCompression**](https://reference.aspose.com/cells/javascript-cpp/tiffcompression/): получайте или задавайте тип сжатия изображений, когда [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) указан как Tiff.
- [**transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--): указывает, должен ли фон изображения быть прозрачным, когда указан формат изображения как Png.

## **Преобразование электронной таблицы Excel в Markdown**
API Aspose.Cells поддерживает экспорт таблиц в формат Markdown. Чтобы экспортировать активный лист в Markdown, передайте [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**MarkdownSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/markdownsaveoptions) для указания дополнительных настроек экспорта листа в Markdown.

Следующий пример кода демонстрирует экспорт активного листа в Markdown с помощью перечисления [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Пожалуйста, посмотрите сгенерированный [файл Markdown](md_sample.txt) как пример.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as Markdown</title>
    </head>
    <body>
        <h1>Save Excel as Markdown Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Markdown</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving as Markdown
            const outputData = workbook.save(SaveFormat.Markdown);
            const blob = new Blob([outputData], { type: 'text/markdown' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.md';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Markdown File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the Markdown file.</p>';
        });
    </script>
</html>
```

## **Конвертировать книгу Excel в JSON**
API Aspose.Cells поддерживает преобразование книги в Json (JavaScript Object Notation).

Следующий пример кода демонстрирует экспорт активного листа в Json с помощью перечисления [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Посмотрите код, чтобы увидеть преобразование [исходного файла](Book1.xlsx) в [выходной Json](Book1.Json).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Convert the workbook to JSON format
            const outputData = workbook.save(SaveFormat.Json);

            // Create a downloadable blob for the JSON result
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Преобразовать Excel в XML**
Aspose.Cells поддерживает преобразование книги Excel в XML документ электронной таблицы Excel 2003 и обычные данные XML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to XML Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Spreadsheet XML</a>
        <a id="downloadLink2" style="display: none;">Download Data XML</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XmlSaveOptions } = AsposeCells;

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

            // Save as Excel 2003 Spreadsheet XML
            const spreadsheetData = workbook.save(SaveFormat.Excel2003Xml);
            const blob1 = new Blob([spreadsheetData]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Spreadsheet.xml';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Spreadsheet XML';

            // Save as plain XML data with XmlSaveOptions
            const xmlSaveOptions = new XmlSaveOptions();
            const dataXml = workbook.save(SaveFormat.SpreadsheetML, xmlSaveOptions);
            const blob2 = new Blob([dataXml]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'data.xml';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Data XML';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Use the links above to download the generated XML files.</p>';
        });
    </script>
</html>
```

## **Преобразовать книгу Excel в TIFF**
Aspose.Cells поддерживает конвертацию книги в файл TIFF.

Ниже приведен фрагмент кода, показывающий, как преобразовать Excel в TIFF:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to TIFF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to TIFF format
            const outputData = workbook.save(SaveFormat.Tiff);
            const blob = new Blob([outputData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to TIFF successfully! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```

## **Преобразовать книгу Excel в DOCX**
API Aspose.Cells поддерживает преобразование таблиц в формат DOCX. Чтобы экспортировать книгу в DOCX, передайте [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**DocxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/docxsaveoptions) для указания дополнительных настроек экспорта листа в DOCX.

Следующий пример кода демонстрирует экспорт активного листа в DOCX с помощью перечисления [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Посмотрите сгенерированный [файл DOCX](Book1.docx) как пример.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as DOCX (Markdown/Docx conversion per original code)
            const outputData = workbook.save(SaveFormat.Docx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.docx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Docx File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the DOCX file.</p>';
        });
    </script>
</html>
```

## **Преобразовать книгу Excel в PPTX**
API Aspose.Cells поддерживает преобразование таблиц в формат PPTX. Чтобы экспортировать книгу в PPTX, передайте [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**PptxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pptxsaveoptions) для указания дополнительных настроек экспорта листа в PPTX.

Следующий пример кода демонстрирует экспорт активного листа в PPTX с помощью перечисления [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Посмотрите сгенерированный [файл PPTX](Book1.pptx) как пример.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save as PPTX Example</title>
    </head>
    <body>
        <h1>Save Excel as PPTX Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PPTX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as PPTX
            const outputData = workbook.save(SaveFormat.Pptx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/\.[^/.]+$/, "");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.pptx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted PPTX File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the PPTX file.</p>';
        });
    </script>
</html>
```

## **Преобразовать рабочую книгу Excel в EPUB**
API Aspose.Cells поддерживает преобразование таблиц в формат EPUB. Чтобы экспортировать книгу в EPUB, передайте [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) для указания дополнительных настроек экспорта листа в Epub.

Следующий пример кода демонстрирует экспорт активного листа в EPUB с помощью перечисления [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Converting To EPUB Files</title>
    </head>
    <body>
        <h1>Converting To EPUB Files</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EPUB</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in EPUB format
            const outputData = workbook.save(SaveFormat.Epub);

            const blob = new Blob([outputData], { type: 'application/epub+zip' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.epub';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EPUB File';

            result.innerHTML = '<p style="color: green;">File converted to EPUB successfully! Click the download link to get the EPUB file.</p>';
        });
    </script>
</html>
```

## **Преобразовать рабочую книгу Excel в AZW3**
API Aspose.Cells поддерживает преобразование таблиц в формат AZW3. Чтобы экспортировать книгу в AZW3, передайте [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) для указания дополнительных настроек экспорта листа в AZW3.

Следующий пример кода демонстрирует экспорт активного листа в AZW3 с помощью перечисления [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert to AZW3 Example</title>
    </head>
    <body>
        <h1>Convert Excel to AZW3 (EPUB) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to AZW3</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Load your sample excel file in a workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in AZW3 format
            const outputData = wb.save(SaveFormat.Azw3);
            const blob = new Blob([outputData]);

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.azw3';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download AZW3 File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the AZW3 file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Преобразование версии XLSB в XLSM](/cells/ru/javascript-cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ru/javascript-cpp/convert-excel-to-html/)
- [Изображение](/cells/ru/javascript-cpp/convert-excel-to-image/)
- [Json](/cells/ru/javascript-cpp/convert-workbook-to-json/)
- [Преобразование Excel-книги в Ods, Sxc и Fods (OpenOffice / LibreOffice calc).](/cells/ru/javascript-cpp/convert-excel-to-ods/)
- [Pdf](/cells/ru/javascript-cpp/convert-excel-workbook-to-pdf/)
- [Преобразование Excel в CSV, TSV и Txt](/cells/ru/javascript-cpp/convert-excel-to-csv-tsv-and-txt/)
- [Отслеживание прогресса конвертации документов](/cells/ru/javascript-cpp/track-document-conversion-progress/)
- [Преобразование CSV, TSV и TXT в Excel](/cells/ru/javascript-cpp/convert-csv-tsv-and-txt-to-excel/)
