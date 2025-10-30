---
title: JSON u C++ ile JavaScript kullanarak Excel e Dönüştürme
linktitle: JSON u Excel dosyasına Dönüştürme
type: docs
weight: 300
url: /tr/javascript-cpp/convert-json-to-excel/
description: JSON u Excel dosyasına dönüştürmenin nasıl yapılacağını Aspose.Cells for JavaScript C++ ile öğrenin.
keywords: Office 2013, Office 2016, Office 2019 ve Office 365 kullanmadan JSON u JavaScript ile C++ kullanarak içe aktarma.
---

{{% alert color="primary" %}}

Aspose.Cells, JSON (JavaScript Nesne Gösterimi) dosyasını Excel Workbook'una dönüştürmeyi destekler.

{{% /alert %}}

## **JSON'u Excel Workbook'e dönüştür**
JSON'u Excel dosyasına dönüştürmenin nasıl yapılacağını merak etmeye gerek yok, çünkü Aspose.Cells for JavaScript C++ en iyi çözümü sağlar. Aspose.Cells API, JSON formatını tablolar haline dönüştürmeye destek sağlar. JSON'u çalışma kitabına içe aktarmak için [**JsonLoadOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonloadoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, JSON'u Excel Çalışma Kitabına içe aktarmayı göstermektedir. Lütfen başvuru için kodu inceleyin [kaynak dosyası](örnek.json) kod tarafından oluşturulan xlsx dosyası.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Convert JSON to XLSX</h1>
        <input type="file" id="fileInput" accept=".json" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // create a Workbook object from uploaded file (JSON)
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // save file to xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the XLSX file.</p>';
        });
    </script>
</html>
```

Aşağıdaki kod örneği, JsonLoadOptions sınıfını kullanarak ek ayarların gösterildiği, JSON'u Excel Workbook'a ithal etmeyi sağlar. [Kaynak dosyası](sample.json) 'yi XLSX formatına dönüştürmek için kodu inceleyebilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Load JSON into Workbook and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an options of loading the file.
            const options = new JsonLoadOptions();
            options.multipleWorksheets = true;

            // Loads the workbook from JSON file
            const book = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save file to xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

Aşağıdaki kod örneği, JSON dizesini Excel Workbook'a ithal etmeyi gösterir. JSON'u ithal ederken düzenin konumunu da belirtebilirsiniz. Dönüşüm için kodu kullanarak JSON dizesini XLSX dosyasına dönüştürmeyi görebilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Import JSON as Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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

        // Converted logic from JavaScript to browser-compatible code
        const inputJson = JSON.stringify([
            { BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
        ]);
        const sheetName = "Sheet1";
        const row = 3;
        const column = 2;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a Workbook object
            const book = new Workbook();
            const worksheet = book.worksheets.get(sheetName);

            // set JsonLayoutOptions to treat Arrays as Table
            const jsonLayoutOptions = new JsonLayoutOptions();
            jsonLayoutOptions.arrayAsTable = true;

            // Import JSON data into worksheet cells at specified row and column
            AsposeCells.JsonUtility.importData(inputJson, worksheet.cells, row, column, jsonLayoutOptions);

            // Save file to xlsx format and prepare download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">JSON imported as table and file generated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
