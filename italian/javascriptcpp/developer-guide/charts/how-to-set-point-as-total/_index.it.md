---
title: Come impostare un punto come totale con JavaScript tramite C++
linktitle: Come impostare un punto come totale
description: Impara a impostare i punti come totale nei grafici WaterFall usando Aspose.Cells for JavaScript tramite C++.
keywords: Grafico WaterFall, Punto, Imposta come totale, JavaScript tramite C++
type: docs
weight: 72
url: /it/javascript-cpp/how-to-set-point-as-total/
---

## Cos'è "Impostare il punto come totale" in un grafico Excel

In alcuni grafici Excel, come ad esempio il grafico WaterFall, alcuni valori dei punti sono la somma dei punti precedenti, e potrebbe essere necessario "impostare il punto come totale". Mostreremo il codice di esempio e l'illustrazione di seguito.

## Un grafico WaterFall necessita di "Impostare il punto come totale" 

![todo:image_alt_text](set-as-total1.png)

Questa immagine mostra un grafico WaterFall in Excel. Si vede che ci sono quattro punti dati iniziando con "Total", e sono usati per calcolare tutti i punti dati precedenti. In questa immagine, le impostazioni non sono esattamente corrette. Quando selezioniamo un punto "Total 2024", vediamo che l'opzione "Imposta come totale" non è selezionata in Excel. Allegato sotto il [file Excel di esempio](SampleSheet.xlsx) che necessita di modifiche, useremo Aspose.Cells for JavaScript tramite C++ per configurarlo correttamente.

## Usa Aspose.Cells for JavaScript tramite C++ per "Imposta punto come totale" 

Usiamo il seguente codice per configurare correttamente il file:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Puoi ottenere il [file di output corretto](output.xlsx)

Come mostrato nell'immagine seguente, i quattro punti dati "Total" sono impostati correttamente, e puoi vedere la differenza rispetto al grafico precedente.

![todo:image_alt_text](set-as-total2.png)
