---
title: Crea un grafico azioni volume apertura alto basso chiusura (VOHLC) con JavaScript tramite C++
description: Impara come creare un grafico di volume apertura alto basso chiusura usando Aspose.Cells for JavaScript tramite C++. La nostra guida dimostrerà come tracciare dati di mercato azionario, inclusi volume, prezzo di apertura, alto, basso e chiusura, su un grafico per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for JavaScript tramite C++, grafico di volume apertura alto basso chiusura, dati di mercato azionario, analisi, visualizzazione.
type: docs
weight: 184
url: /it/javascript-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il quarto grafico azionario che esamineremo è il grafico Volume Open High Low Close. Ancora una volta, è importante ripetere che i dati devono essere nell'ordine corretto. Se è necessario riorganizzare la tabella dei dati, fattelo prima di impostare il grafico. Questo grafico include una colonna per il volume immediatamente dopo la prima colonna (categoria), e i grafici includono un grafico a colonne sull'asse principale che mostra questo volume, mentre i prezzi sono spostati sull'asse secondario.

![todo:image_alt_text](data.png)
## **Grafico Azionario Volume-Apri-Alto-Basso-Chiusura (VHLC)**

![todo:image_alt_text](sample.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Volume-Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-Open-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-Open-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (preserve both arguments as an array)
            chart.chartDataRange = ["A1:F9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series (Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;
            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
