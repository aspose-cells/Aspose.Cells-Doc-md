---
title: Установите ширину столбца в масштабируемую единицу, такую как em или проценты, с помощью JavaScript через C++
linktitle: Установка ширины столбца в масштабируемую единицу, такую как em или процент
type: docs
weight: 130
url: /ru/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Узнайте, как установить ширину столбца в масштабируемых единицах, таких как em или проценты, в Aspose.Cells for JavaScript через C++. Улучшите отображение сгенерированных таблиц HTML.
---

Генерация HTML-файла из электронной таблицы очень распространена. Размер столбцов определяется в "pt", что работает во многих случаях. Однако может возникнуть ситуация, когда эта фиксированная величина не требуется. Например, если ширина контейнера панели составляет 600 пикселей, где отображается эта HTML-страница, могут появиться горизонтальные полосы прокрутки, если сгенерированная таблица будет шире. Требовалось, чтобы эта фиксированная ширина была заменена на масштабируемую единицу, такую как em или проценты, для лучшего отображения. Следующий пример кода можно использовать, где [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) устанавливается в **true** для создания масштабируемой ширины.

Образец исходного файла и выходные файлы можно загрузить по следующим ссылкам:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
