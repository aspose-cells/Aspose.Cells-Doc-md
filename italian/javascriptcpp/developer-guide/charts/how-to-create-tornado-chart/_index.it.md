---
title: Come creare un grafico a tornado con JavaScript tramite C++
linktitle: Come creare un grafico a tornado
type: docs
weight: 73
url: /it/javascript-cpp/create-tornado-chart/
description: Scopri come creare un grafico a tornado con Aspose.Cells for JavaScript tramite API C++.
keywords: JavaScript crea un grafico a tornado, aggiungi un grafico a tornado, inserisci un grafico a tornado
---

## **Introduzione**
Un grafico a tornado, noto anche come diagramma a tornado o grafico a tornado, è un tipo di visualizzazione dei dati che viene spesso utilizzato per l'analisi di sensibilità in Excel. Ti aiuta a capire l'impatto delle variabili in cambiamento su un particolare risultato o esito.

## **Come creare un grafico a tornado in Excel**
Puoi creare un grafico a tornado in Excel seguendo questi passaggi:
1. Seleziona i dati e vai su Inserisci --> Grafici --> Inserisci grafico a colonne o a barre --> Grafico a barre sovrapposte. Clicca su di esso.
<br>
<img src="1.png" width=70% />
2. Cambia l'asse Y: Fai clic con il pulsante destro sull'asse y. Fai clic su formatta asse. Nelle etichette, fai clic sul menu a discesa della posizione dell'etichetta e seleziona l'elemento Basso.
<br>
<img src="2.png" width=70% />
3. Seleziona una qualsiasi barra e vai al formato. Imposta una larghezza di intervallo appropriata.
<br>
<img src="3.png" width=70% />
4. Rimuoviamo il segno meno (-) dal grafico a tornado. Seleziona l'asse x. Vai al formato. Nelle opzioni asse, fai clic sul numero. Nella categoria, seleziona personalizzato. Nel codice di formato scrivi ###0,###0. Clicca su aggiungi.
<br>
<img src="4.png" width=70% />
5. fai clic sull'asse y e vai alle opzioni asse. Nelle opzioni asse, seleziona Categorie in ordine inverso.
<br>
<img src="5.png" width=70% />

## **Come aggiungere un grafico a tornado in Aspose.Cells for JavaScript tramite C++**
Si prega di consultare il seguente codice di esempio. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati di esempio. Successivamente, crea il grafico a barre sovrapposte basato sui dati iniziali e imposta le proprietà rilevanti. Infine, salva il lavoro in formato XLSX di output. La seguente schermata mostra il grafico a tornado creato da Aspose.Cells nel file Excel di output.
<br>
<img src="6.png" width=70% />

### **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
