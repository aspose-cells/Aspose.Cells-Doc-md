---
title: Конвертация CSV в JSON с помощью JavaScript через C++
linktitle: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/javascript-cpp/convert-csv-to-json/
description: Конвертировать CSV файл в JSON с помощью простого в использовании API Aspose.Cells for JavaScript через C++.
keywords: Конвертация, конвертация CSV в JSON, CSV в JSON, CSV, JSON, конвертация CSV в JSON JavaScript через C++, код на C++, чтобы конвертировать CSV в JSON
---

## **Преобразовать CSV в JSON**

Поддержка Aspose.Cells для преобразования CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) предоставляет опции для экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) содержит следующие свойства.

- [**ExportRangeToJsonOptions.exportAsString**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#exportAsString--): Это экспортирует строковое значение ячеек в JSON.
- [**ExportRangeToJsonOptions.hasHeaderRow**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#hasHeaderRow--): Указывает, содержит ли диапазон строку заголовка.
- [**ExportRangeToJsonOptions.indent**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#indent--): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) экспортирует JSON с использованием настроек экспорта, установленных через класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/).

Следующий пример кода демонстрирует использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) для загрузки [исходного CSV-файла](104398879.csv) и вывода JSON в консоль.

### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Export CSV Range to JSON Example</title>
    </head>
    <body>
        <h1>Export CSV Range to JSON Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Export to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, JsonSaveOptions, JsonUtility } = AsposeCells;

        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runButton.disabled = false;
        });

        function escapeHtml(unsafe) {
            return unsafe
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '';
            downloadLink.textContent = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions = new LoadOptions(LoadFormat.Csv);
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            const worksheet = workbook.worksheets.get(0);
            const lastCell = worksheet.cells.lastCell;

            const jsonSaveOptions = new JsonSaveOptions();
            const range = worksheet.cells.createRange(0, 0, lastCell.row + 1, lastCell.column + 1);
            const data = JsonUtility.exportRangeToJson(range, jsonSaveOptions);

            // Display JSON in the result div
            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully!</p><pre>' + escapeHtml(data) + '</pre>';

            // Create a downloadable JSON file
            const blob = new Blob([data], { type: 'application/json' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'exported_range.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';
        });
    </script>
</html>
```

### **Вывод в консоль**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
