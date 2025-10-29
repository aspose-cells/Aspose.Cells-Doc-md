---
title: Шрифт темы заголовков и тела
linktitle: Шрифт темы заголовков и тела
description: Aspose.Cells — это библиотека на JavaScript через C++ для работы с файлами таблиц. Поддерживает установку шрифтов тематики заголовков и основного текста в документах Excel, позволяя пользователям настраивать внешний вид и стиль документа. В этой статье рассказывается о том, как использовать библиотеку Aspose.Cells для работы с шрифтами тематики заголовков и основного текста в документах Excel.
keywords: Aspose.Cells, документ Excel, заголовок, основной текст, шрифт темы, внешний вид, стиль, JavaScript через C++
type: docs
weight: 120
url: /ru/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

По умолчанию шрифт автоматически изменится при изменении региональных настроек.

Если стандартный шрифт изменен, также изменится высота строк и ширина столбцов, и это может нарушить макет страницы.

Что вызвало изменение шрифта по умолчанию?

Если задан тематический шрифт Excel, Excel автоматически переключается между различными шрифтами в зависимости от текущей языковой среды.

{{% /alert %}}

## **Тематический шрифт заголовков и основного текста в Excel**

В Excel выберите вкладку Главная, откройте список шрифтов, вы увидите "Тематические шрифты" с двумя шрифтами: Calibri Light (Заголовки) и Calibri (Основной текст) в верхней части с настройками региона для Англии.

**![Тематические шрифты](Theme-Fonts.png)**

Если выбран тематический шрифт, название шрифт отображается по-разному в разных регионах. Если не хотите, чтобы шрифт автоматически менялся в разных регионах, не выбирайте два тематических шрифта.

## **Изменение шрифта заголовков и основного текста программно**
С помощью Script Aspose.Cells for Java через C++ мы можем проверить, является ли шрифт по умолчанию шрифтом темы или установить шрифт темы с помощью метода [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-).

Следующий пример кода демонстрирует, как управлять шрифтом темы.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Динамическое получение локального шрифта темы программно**
Иногда наши серверы и компьютеры пользователей не находятся в одном регионе. Как мы можем получить тот же шрифт, который пользователи хотят для обработки файлов?

Перед загрузкой файла с помощью метода [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-) нам необходимо установить системные региональные настройки.

В следующем примере кода показано, как получить локальный тематический шрифт.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
