---
title: JavaScript aracılığıyla Çalışma Sayfasında Boş Satırları ve Sütunları Silme, C++ ile
linktitle: Çalışma Sayfasındaki Boş Satır ve Sütunları Silme
type: docs
weight: 300
url: /tr/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Aspose.Cells for JavaScript kullanarak tüm boş satırları ve sütunları nasıl silineceğini öğrenin. 
---

{{% alert color="primary" %}}

Bir sayfadan boş satır ve sütunların tamamını silebilmek mümkündür. Bu, örneğin, Microsoft Excel dosyasından PDF dosyası oluştururken, yalnızca veri içerip içermeyen satır ve sütunları dönüştürmek istendiğinde faydalıdır.

Boş satır ve sütunları silmek için aşağıdaki Aspose.Cells yöntemlerini kullanın:

1. Boş satırları silmek için [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankRows--) yöntemini kullanın. Silinecek boş satırlar için, [**Row.isBlank()**](https://reference.aspose.com/cells/javascript-cpp/row/#isBlank--) sadece doğru olmalıdır, ayrıca bu satırlarda herhangi bir hücre için görünür bir yorum tanımlanmamış olmalı ve bunlarla kesişen bir pivota tablonun olmaması gerekir.
2. Boş sütunları silmek için [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankColumns--) yöntemini kullanın.

{{% /alert %}}

## Boş Satırları Silmek İçin JavaScript Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Delete Blank Rows Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;

            // Get first worksheet
            const sheet = sheets.get(0);

            // Delete blank rows from the worksheet
            sheet.cells.deleteBlankRows();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Blank rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Boş Sütunları Silmek İçin JavaScript Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Blank Columns Example</title>
    </head>
    <body>
        <h1>Delete Blank Columns Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = workbook.worksheets;

            // Get first Worksheet from WorksheetCollection
            const sheet = sheets.get(0);

            // Delete the Blank Columns from the worksheet
            sheet.cells.deleteBlankColumns();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Blank columns deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
