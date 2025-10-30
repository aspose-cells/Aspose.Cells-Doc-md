---
title: Come impostare una serie come invisibile con JavaScript tramite C++
linktitle: Come impostare la serie come invisibile
description: Impara come impostare una serie invisibile in un grafico Excel utilizzando Aspose.Cells for JavaScript tramite C++. 
keywords: Grafico Excel, Serie, Invisibile, IsFiltered JavaScript tramite C++.
type: docs
weight: 74
url: /it/javascript-cpp/how-to-set-series-invisible/
---

## Come impostare le serie come invisibili nel grafico Excel

In Excel, puoi cliccare con il tasto destro su un grafico, cliccare su "Seleziona dati", e nella finestra popup puoi impostare se una serie è visibile spuntando o deselezionando l'opzione. Puoi scaricare il seguente [file di esempio](SeriesFiltered.xlsx) e operarlo in Excel come mostrato nella figura per ottenere questa funzione. Successivamente, ti spiegheremo come farlo usando la libreria Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Come impostare le serie come invisibili usando Aspose.Cells 

Usiamo il seguente codice per impostare le serie come invisibili usando Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Puoi ottenere il seguente [File di input](SeriesFiltered.xlsx) e [file di output](output.xlsx).

Come mostrato nella figura sotto, le prime due serie, che erano visibili originariamente, sono diventate invisibili nel file di output.
![todo:image_alt_text](output.png)
