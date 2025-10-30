---
title: Excel in JSON mit JavaScript über C++ konvertieren
linktitle: Konvertieren Sie Excel in JSON
type: docs
weight: 300
url: /de/javascript-cpp/convert-excel-to-json/
description: Erfahren Sie, wie Sie eine Excel Datei mit Aspose.Cells for JavaScript über C++ in JSON konvertieren.
keywords: Arbeitsmappe nach JSON exportieren mit JavaScript über C++, Excel nach JSON konvertieren mit JavaScript über C++
---

{{% alert color="primary" %}}  
Aspose.Cells unterstützt die Konvertierung eines Arbeitsbuchs in eine JSON (JavaScript-Objekt-Notation)-Datei.  
{{% /alert %}}  

## **Excel-Arbeitsmappe in JSON konvertieren**  

Sie brauchen sich nicht zu wundern, wie Sie eine Excel-Arbeitsmappe in JSON konvertieren, denn die Aspose.Cells for JavaScript über C++-Bibliothek bietet die beste Lösung. Die API Aspose.Cells unterstützt die Konvertierung von Tabellenkalkulationen in das JSON-Format. Um die Arbeitsmappe nach JSON zu exportieren, übergeben Sie [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/) als zweiten Parameter der [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-Methode. Sie können auch die [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach JSON festzulegen.  

Das folgende Codebeispiel demonstriert das Exportieren eines Excel-Arbeitsbuchs nach JSON. Bitte beachten Sie den Code zur Konvertierung der [Quelldatei](sample.xlsx) in die durch den Code generierte JSON-Datei.  

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

Das folgende Codebeispiel verwendet die JsonSaveOptions-Klasse, um zusätzliche Einstellungen festzulegen, und zeigt das Exportieren eines Excel-Arbeitsbuchs nach JSON. Bitte beachten Sie den Code zur Konvertierung der [Quelldatei](sample.xlsx) in die durch den Code generierte JSON-Datei.  

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
