---
title: Конвертация Excel в JSON с помощью JavaScript через C++
linktitle: Конвертировать Excel в JSON
type: docs
weight: 300
url: /ru/javascript-cpp/convert-excel-to-json/
description: Узнайте, как конвертировать файл Excel в JSON с помощью Aspose.Cells for JavaScript через C++.
keywords: Экспорт книги Excel в JSON JavaScript через C++, Конвертация Excel в JSON JavaScript через C++
---

{{% alert color="primary" %}}  
Aspose.Cells поддерживает преобразование рабочей книги в файл JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Конвертировать книгу Excel в JSON**  

Не нужно гадать, как конвертировать книгу Excel в JSON, потому что библиотека Aspose.Cells for JavaScript через C++ предоставляет лучшее решение. API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Чтобы экспортировать книгу в JSON, передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/) в качестве второго параметра метода [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/) для задания дополнительных настроек экспортирования листа в JSON.  

Следующий пример кода демонстрирует экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON-файл, сгенерированный кодом, для справки.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

Следующий пример кода использует класс JsonSaveOptions для задания дополнительных настроек и демонстрирует экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON-файл, сгенерированный кодом, для справки.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```
