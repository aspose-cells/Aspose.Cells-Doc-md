---
title: Konvertera CSV till JSON med JavaScript via C++
linktitle: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/javascript-cpp/convert-csv-to-json/
description: Konvertera CSV fil till JSON med den enkla Aspose.Cells for JavaScript via C++ API.
keywords: Konvertera, Konvertera CSV till JSON, CSV till JSON, CSV, JSON, Konvertera CSV till JSON JavaScript via C++, c++ kod för att konvertera CSV till JSON
---

## **Konvertera CSV till JSON**

Aspose.Cells stöder konvertering av CSV till JSON. För detta tillhandahåller API:n klasserna [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/). Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) ger valmöjligheter för att exportera intervall till JSON. Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) har följande egenskaper.

- [**ExportRangeToJsonOptions.exportAsString**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#exportAsString--): Detta exporterar cellernas strängvärde till JSON.
- [**ExportRangeToJsonOptions.hasHeaderRow**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#hasHeaderRow--): Detta indikerar om intervallet innehåller en rubrikrad.
- [**ExportRangeToJsonOptions.indent**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#indent--): Indikerar indenteringen.

Klass [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) exporterar JSON med de exportalternativ som ställts in med klass [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/).

Följande kod exempel visar användningen av klasserna [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) för att ladda [kälcsv-fil](104398879.csv) och skriver ut JSON-resultatet i konsolen.

### **Exempelkod**

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

### **Konsoloutput**
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
