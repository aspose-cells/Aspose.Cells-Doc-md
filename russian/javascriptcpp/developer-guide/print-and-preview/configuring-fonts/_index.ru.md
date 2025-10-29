---
title: Настройка шрифтов для отображения электронных таблиц с помощью JavaScript через C++
linktitle: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Узнайте, как настроить шрифты для отображения электронных таблиц с помощью Aspose.Cells for JavaScript через C++. Убедитесь, что шрифты доступны для оптимальной точности конвертации.
---

## **Возможные сценарии использования**

API Aspose.Cells позволяют отображать таблицы в изображениях и конвертировать их в PDF и XPS форматы. Для максимальной точности конвертации необходимо, чтобы используемые в таблице шрифты были доступны в стандартной директории шрифтов операционной системы. Если необходимые шрифты отсутствуют, API попытается заменить их доступными шрифтами.

## **Выбор шрифтов**

Ниже приведен процесс, который API Aspose.Cells следует за кулисами.

1. API пытается найти шрифты на файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если API не может найти шрифты с точно таким же именем, он пытается использовать шрифт по умолчанию, указанный в свойстве [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) книги.
1. Если API не может найти шрифт, определенный в свойстве [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) книги, он пытается использовать шрифт, указанный в свойствах [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) или [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--).
1. Если API не может найти шрифт, определенный в свойствах [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) или [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--), он пытается использовать шрифт, указанный в свойстве [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--).
1. Если API не может найти шрифт, определенный в свойстве [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--), он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты на файловой системе, он визуализирует электронную таблицу с использованием шрифта Arial.

## **Установка пользовательских каталогов шрифтов**

API Aspose.Cells ищут нужные шрифты в стандартной директории шрифтов операционной системы. Если шрифты не найдены там, поиск продолжается по пользовательским (настроенным) каталогам. Класс [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) предоставляет несколько способов задания пользовательских директорий шрифтов, как описано ниже.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Этот метод полезен, если нужно установить только одну папку.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Этот метод полезен, когда шрифты находятся в нескольких папках, и пользователь хочет установить каждую папку отдельно, а не объединить все шрифты в одну папку.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Этот механизм полезен, когда пользователь хочет загружать шрифты из нескольких папок или одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

Оба метода [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) и [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) принимают второй параметр типа Boolean. Передача **true** в качестве второго параметра направит API Aspose.Cells на поиск файлов шрифтов в подпапках.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеперечисленных методов в начале приложения, то есть; перед вызовом любых других объектов API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Если все вышеперечисленные методы используются для установки источников шрифтов, то только последние настройки будут применены.

{{% /alert %}}

## **Механизм подстановки шрифтов**

API Aspose.Cells также позволяют указывать заменяющий шрифт для рендеринга. Это полезно, когда необходимый шрифт недоступен на машине, где выполняется конвертация. Пользователи могут задать список имен шрифтов для замены оригинальных. Для этого API предоставляет метод [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-), который принимает 2 параметра. Первый — это строка **string**, указывающая имя шрифта для замены. Второй — это массив строк **string**, содержащий список имен шрифтов для замены исходного.

Вот простой сценарий использования.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **Сбор информации**

Помимо вышеуказанных методов, API Aspose.Cells позволяют собирать информацию о выбранных источниках и заменах шрифтов.

1. Метод [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) возвращает массив типа [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase), содержащий список указанных источников шрифтов. Если источники не заданы, метод [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) возвратит пустой массив.
1. Метод [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) принимает параметр типа **string**, позволяющий указать имя шрифта, для которого задана замена. Если для указанного шрифта замена не задана, метод [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) вернет null.

## **Продвинутые темы**
- [Установите шрифт по умолчанию при отображении электронной таблицы в изображения](/cells/ru/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Установите свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions для приоритета](/cells/ru/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Поддерживаемые форматы шрифтов](/cells/ru/javascript-cpp/supported-font-formats/)
- [Электронная таблица в изображение - установите формат пикселей для визуализированного изображения](/cells/ru/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
