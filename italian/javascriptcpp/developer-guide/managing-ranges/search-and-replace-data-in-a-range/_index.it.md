---
title: Cerca e sostituisci dati in un intervallo con JavaScript tramite C++
linktitle: Cerca e Sostituisci Dati in un Intervallo
type: docs
weight: 170
url: /it/javascript-cpp/search-and-replace-data-in-a-range/
description: Questo articolo mostra come cercare e sostituire dati in un intervallo in Excel usando JavaScript tramite codice C++.
keywords: javascript cerca e sostituisci dati in excel, javascript cerca dati in excel, javascript cerca e sostituisci dati in un intervallo, javascript cerca dati in un intervallo, javascript ricerca dati in un intervallo, javascript ricerca dati in intervallo, javascript ricerca dati in excel, javascript cerca dati in intervallo, cerca e sostituisci dati in excel con javascript, cerca e sostituisci dati in un intervallo con javascript, cerca e sostituisci dati in intervallo con javascript
---

{{% alert color="primary" %}}

A volte è necessario cercare e sostituire dati specifici in un intervallo ignorando qualsiasi valore di cella al di fuori dell'intervallo desiderato. Aspose.Cells for JavaScript tramite C++ ti consente di limitare una ricerca a un intervallo specifico. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells for JavaScript tramite C++ fornisce il metodo [**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-) per specificare un intervallo durante la ricerca di dati. Il codice seguente cerca e sostituisce dati in un intervallo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
