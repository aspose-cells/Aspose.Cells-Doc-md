---
title: Imposta il testo dell elemento dell legenda del grafico su nessuno usando Aspose.Cells for JavaScript tramite C++
linktitle: Imposta il testo dell elemento legenda del grafico su nessuno utilizzando Aspose.Cells
description: Impara come usare Aspose.Cells for JavaScript via C++ per impostare il riempimento di un elemento della legenda di un grafico su nessuno. Questa guida dimostrerà come modificare il colore di riempimento degli elementi della legenda nei grafici di Microsoft Excel per una migliore visualizzazione e personalizzazione.
keywords: Aspose.Cells for JavaScript via C++, Riempimento degli Elementi della Legenda del Grafico, Microsoft Excel, Visualizzazione, Personalizzazione.
type: docs
weight: 320
url: /it/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Se desideri impostare il testo del riempimento dell'ingresso della legenda del grafico su nessuno in modo che non venga visualizzato all’interno della leggenda del grafico, imposta [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--) su **true**.

{{% /alert %}}

Il codice di esempio seguente imposta il testo del secondo riempimento dell'elemento legenda del grafico su nessuno. Scarica il [file Excel di esempio](5115219.xlsx) utilizzato in questo codice e il [file Excel di output](5115217.xlsx) generato da esso per ulteriori informazioni.

screenshoot seguente evidenzia l'effetto di questo codice sul [file Excel di esempio](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
