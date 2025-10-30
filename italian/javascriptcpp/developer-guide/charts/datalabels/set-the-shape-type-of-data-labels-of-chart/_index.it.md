---
title: Imposta il tipo di forma delle etichette dati del grafico con JavaScript tramite C++
linktitle: Imposta il tipo di forma dell etichetta dati del grafico
description: Impara come impostare il tipo di forma delle etichette dati nei grafici usando Aspose.Cells for JavaScript tramite C++. Questa guida spiegherà i diversi tipi di forma disponibili e mostrerà come scegliere la forma appropriata per le tue etichette dati per migliorare presentazione e usabilità.
keywords: Aspose.Cells for JavaScript tramite C++, grafici, etichette dati, tipi di forma, presentazione, usabilità.
type: docs
weight: 110
url: /it/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi cambiare il tipo di forma delle etichette dei dati del grafico usando la proprietà `DataLabels.shapeType`. Essa accetta il valore dell'enumerazione `DataLabelShapeType` e modifica di conseguenza il tipo di forma delle etichette dei dati. Alcuni dei suoi valori sono

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Imposta il tipo di forma delle etichette dati del grafico**
Il seguente esempio di codice cambia il tipo di forma delle etichette dei dati del grafico in `DataLabelShapeType.WedgeEllipseCallout`. Consulta il [file Excel di esempio](60489778.xlsx) utilizzato in questo codice e il [file Excel di output](60489779.xlsx) generato. Lo screenshot mostra l'effetto del codice sul file Excel di esempio.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Codice di Esempio**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

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

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
