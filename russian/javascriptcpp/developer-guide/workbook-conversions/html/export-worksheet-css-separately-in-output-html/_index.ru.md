---
title: Экспортировать CSS листов в отдельности в выводимый HTML с помощью JavaScript через C++
linktitle: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML
type: docs
weight: 80
url: /ru/javascript-cpp/export-worksheet-css-separately-in-output/
description: Узнайте, как экспортировать CSS листов отдельно при преобразовании файла Excel в HTML с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Aspose.Cells for JavaScript через C++ предоставляет функцию экспорта CSS листов отдельно при конвертации файла Excel в HTML. Используйте [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--) свойство для этой цели и установите его в **true** при сохранении файла Excel в формат HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий пример создает файл Excel, добавляет текст в ячейку **B5** красным цветом, а затем сохраняет его в формате HTML с использованием свойства [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--). Пожалуйста, смотрите [выходной HTML](60489766.zip), сгенерированный по коду, для ознакомления. Внутри него вы найдете **stylesheet.css** как итог выполнения примера.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet CSS Separately Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color, Utils } = AsposeCells;

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
            // Create a new workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - export worksheet css separately
            const opts = new HtmlSaveOptions();
            opts.exportWorksheetCSSSeparately = true;

            // Save the workbook in html 
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportWorksheetCSSSeparately.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Экспорт книги с одним листом в HTML**

Когда рабочая книга с несколькими листами конвертируется в HTML с помощью Aspose.Cells for JavaScript через C++, создается HTML-файл вместе с папкой, содержащей CSS и несколько HTML-файлов. При открытии этого HTML-файла в браузере видны вкладки. То же поведение требуется для рабочей книги с одним листом при её преобразовании в HTML. Ранее для рабочих книг с одним листом не создавалась отдельная папка, создавался только HTML-файл. Такой HTML-файл при открытии в браузере вкладки не показывает. MS Excel также создает правильную папку и HTML для одного листа, поэтому то же поведение реализовано с помощью API Aspose.Cells. Скачать пример можно по следующей ссылке для использования в приведенном ниже примере:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, EncodingType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML save options
            const options = new HtmlSaveOptions();

            // Set optional settings (converted from setters to properties)
            options.encoding = EncodingType.UTF8;
            options.exportImagesAsBase64 = true;
            options.exportGridLines = true;
            options.exportSimilarBorderStyle = true;
            options.exportBogusRowData = true;
            options.excludeUnusedStyles = true;
            options.exportHiddenWorksheet = true;

            // Save the workbook in HTML format with specified HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSampleSingleSheet.htm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
