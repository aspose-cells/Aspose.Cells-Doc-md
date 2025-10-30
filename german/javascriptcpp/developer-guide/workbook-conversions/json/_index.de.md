---
title: JSON mit JavaScript via C++
linktitle: Json
type: docs
weight: 300
url: /de/javascript-cpp/convert-workbook-to-json/
description: Lernen Sie, wie Sie Excel Arbeitsmappen mit Aspose.Cells for JavaScript über C++ in JSON umwandeln.
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine Json-Datei (JavaScript Object Notation).
{{% /alert %}}

## **Excel-Arbeitsmappe in JSON konvertieren**

Das Aspose.Cells API unterstützt die Konvertierung von Tabellen in das JSON-Format. Um die Arbeitsmappe als JSON zu exportieren, übergeben Sie [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-Methode. Sie können auch die [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach JSON zu spezifizieren.

Das folgende Code-Beispiel zeigt den Export des aktiven Arbeitsblatts nach JSON unter Verwendung des [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json)-Aufzählungsmitglieds. Bitte beachten Sie den Code, um die [Quelldatei](book1.xlsx) in die durch den Code generierte [Ausgabedatei Json](book1.Json) umzuwandeln.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Konvertieren von CSV in JSON](/cells/de/javascript-cpp/convert-csv-to-json/)
- [In-Excel-in-JSON-konvertieren](/cells/de/javascript-cpp/convert-excel-to-json/)
- [JSON in CSV konvertieren](/cells/de/javascript-cpp/convert-json-to-csv/)
- [JSON-in-Excel-konvertieren](/cells/de/javascript-cpp/convert-json-to-excel/)
