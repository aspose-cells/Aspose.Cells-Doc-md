---
title: HTML с JavaScript через C++
linktitle: HTML
type: docs
weight: 230
url: /ru/javascript-cpp/convert-excel-to-html/
---

## **Преобразование книги Excel в HTML**
API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions), чтобы дать возможность управлять несколькими аспектами итогового HTML.

Пример кода ниже показывает, как сохранить рабочую книгу в виде HTML-файла с помощью JavaScript через C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **Преобразование книги Excel в файлы MHTML**
MHTML объединяет обычный HTML с внешними ресурсами (то есть содержимым, которое обычно связано, например, изображения, анимации, аудио и так далее) в один файл. Они используются для электронных писем с расширением .mht. Aspose.Cells поддерживает чтение и запись MHTML файлов.

Пример кода ниже показывает, как сохранить рабочую книгу в виде файла MHTML с помощью JavaScript через C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
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

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге](/cells/ru/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Избегайте экспоненциальной записи больших чисел при импорте из HTML](/cells/ru/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Изменить тип HTML ссылки](/cells/ru/javascript-cpp/change-the-html-link-target-type/)
- [Преобразование Excel в HTML со всплывающей подсказкой](/cells/ru/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ru/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [Удаление избыточных пробелов после переноса строки при импорте HTML](/cells/ru/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Отключить отображение устаревших комментариев при сохранении в HTML](/cells/ru/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Отключить экспорт фреймовых сценариев и свойств документа](/cells/ru/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel в HTML - использование параметра PresentationPreference для лучшего макета](/cells/ru/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Исключить неиспользуемые стили во время преобразования Excel в HTML](/cells/ru/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Развертывание текста справа налево при экспорте файла Excel в HTML](/cells/ru/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML](/cells/ru/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Экспортировать комментарии при сохранении файла Excel в HTML](/cells/ru/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Экспортировать свойства рабочей книги и листа в формате HTML при конвертации Excel в HTML](/cells/ru/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Экспорт Excel в HTML с сеткой](/cells/ru/javascript-cpp/export-excel-to-html-with-gridlines/)
- [Экспортировать диапазон области печати в HTML](/cells/ru/javascript-cpp/export-print-area-range-to/)
- [Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами](/cells/ru/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Экспорт CSS таблицы рабочего листа отдельно в выходном HTML](/cells/ru/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML](/cells/ru/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId](/cells/ru/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Предотвратить экспорт скрытого содержимого листа при сохранении в HTML](/cells/ru/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Предоставление пути к экспортированному файлу HTML листа через интерфейс IFilePathProvider](/cells/ru/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Распознавание самозакрывающихся тегов](/cells/ru/javascript-cpp/recognise-self-closing-tags/)
- [Визуализация градиентного заливки для WordArt при преобразовании таблиц в HTML](/cells/ru/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Установить ширину столбца в масштабируемую единицу, например em или процент](/cells/ru/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML](/cells/ru/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType](/cells/ru/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Поддерживайте макет тегов DIV при загрузке HTML в книгу Excel](/cells/ru/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Включить пользовательские свойства CSS при сохранении в HTML](/cells/ru/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
