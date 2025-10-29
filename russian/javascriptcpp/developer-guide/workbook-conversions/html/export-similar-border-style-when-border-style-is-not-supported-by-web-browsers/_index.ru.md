---
title: Экспортировать похожий стиль границы, когда стиль границы не поддерживается браузерами с помощью JavaScript через C++  
linktitle: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами  
type: docs  
weight: 70  
url: /ru/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Узнайте, как экспортировать границы, которые не поддерживаются браузерами при конвертации файлов Excel в HTML с помощью Aspose.Cells for JavaScript через C++.  
---  

## **Возможные сценарии использования**  

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. При конвертации такого файла Excel в HTML с помощью Aspose.Cells for JavaScript через C++, такие границы удаляются. Однако, Aspose.Cells также может поддерживать отображение таких границ с помощью свойства [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--). Установите его значение в **true**, и неподдерживаемые границы также будут экспортированы в HTML-файл.  

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**  

Следующий пример загружает [образец файла Excel](64716806.xlsx), содержащий некоторые неподдерживаемые границы, как показано на следующем скриншоте. Скриншот дополнительно иллюстрирует эффект свойства [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) внутри [выходного HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
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

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
