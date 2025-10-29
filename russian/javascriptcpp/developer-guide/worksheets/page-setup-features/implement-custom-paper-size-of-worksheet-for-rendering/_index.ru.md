---
title: Реализовать пользовательский размер бумаги листа для рендеринга с помощью JavaScript через C++
linktitle: Реализация пользовательского размера бумаги для рендеринга листа
type: docs
weight: 70
url: /ru/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: В этой статье объясняется, как использовать JavaScript API через C++ для установки пользовательского размера бумаги для нужных листов при программном рендеринге файла Excel в PDF формат.
keywords: установить пользовательский размер страницы при преобразовании Excel в PDF с помощью JavaScript через C++
---

## **Возможные сценарии использования**  

В MS Excel нет прямой опции для создания пользовательских размеров бумаги, однако вы можете установить пользовательский размер бумаги для нужных листов при преобразовании файла Excel в PDF. В этом документе объясняется, как задать пользовательский размер бумаги листа с помощью API Aspose.Cells.  

## **Настройка пользовательского размера бумаги для отображения на листе**  

Aspose.Cells позволяет реализовать желаемый размер бумаги листа. Вы можете использовать метод [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-) класса [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/), чтобы задать пользовательский размер страницы. В следующем примере кода показано, как задать пользовательский размер бумаги для первого листа книги. Также смотрите [выходной PDF](45056028.pdf), созданный этим кодом, для справки.  

## **Снимок экрана**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
