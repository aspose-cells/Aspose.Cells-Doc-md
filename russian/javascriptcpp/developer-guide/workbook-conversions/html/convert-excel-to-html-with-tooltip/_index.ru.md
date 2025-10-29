---
title: Конвертация Excel в HTML с подсказкой с помощью JavaScript через C++  
linktitle: Преобразовать Excel в HTML c всплывающей подсказкой  
type: docs  
weight: 200  
url: /ru/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Узнайте, как преобразовывать файлы Excel в формат HTML с подсказками для полного отображения текста с помощью Aspose.Cells for JavaScript через C++.  
---

## **Преобразование Excel в HTML со всплывающей подсказкой**

Могут возникать случаи, когда текст в сгенерированном HTML обрезается, и вы хотите отображать полный текст в виде подсказки при наведении. Aspose.Cells for JavaScript через C++ поддерживает это, предоставляя свойство [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--). Установка свойства [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) в **true** добавит полный текст в виде подсказки в сгенерированный HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Следующий пример кода загружает [исходный Excel-файл](98107416.xlsx) и генерирует [выходной HTML-файл](98107417.zip) с подсказкой.

Образец кода

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
