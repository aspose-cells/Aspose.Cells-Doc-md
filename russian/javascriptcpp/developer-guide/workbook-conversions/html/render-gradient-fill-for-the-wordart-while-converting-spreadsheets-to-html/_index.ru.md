---
title: Отрисовка градиентной заливки для WordArt при преобразовании таблиц в HTML с помощью JavaScript через C++
linktitle: Отображение градиентной заливки для WordArt при преобразовании электронных таблиц в HTML
type: docs
weight: 90
url: /ru/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Узнайте, как отображать градиентную заливку для WordArt при преобразовании таблиц в HTML с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  
До версии Aspose.Cells 17.1 Aspose.Cells не отображал градиентную заливку WordArt при конвертации Excel файла в формат HTML. Начиная с версии Aspose.Cells 17.1, эта поддержка добавлена. Следующий скриншот показывает сравнение влияния градиентной заливки при конвертации файла с помощью Aspose.Cells 17.1 и более старой версии.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Отображение градиентного заполнения для WordArt при конвертации электронных таблиц в HTML**  
Следующий пример конвертирует [исходный файл Excel](22774111.xlsx) в [выходной HTML](22774109.zip). В исходном файле Excel есть объект WordArt с градиентной заливкой, как показано на скриншоте выше.  

## **Образец кода**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
