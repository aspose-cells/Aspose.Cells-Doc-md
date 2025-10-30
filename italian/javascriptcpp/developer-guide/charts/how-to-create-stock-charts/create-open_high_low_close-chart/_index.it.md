---
title: Crea un grafico azione apertura alto basso chiusura (OHLC) con JavaScript tramite C++
description: Impara come creare un grafico azione apertura alto basso chiusura usando Aspose.Cells for JavaScript tramite C++. La nostra guida dimostrerà come tracciare dati di mercato azionario, inclusi i prezzi di apertura, alto, basso e chiusura, su un grafico per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for JavaScript tramite C++, grafico azione apertura alto basso chiusura, dati di mercato azionario, analisi, visualizzazione.
type: docs
weight: 182
url: /it/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il grafico Open-High-Low-Close (OHLC) utilizza cinque colonne di dati, in ordine: categoria, apertura, alta, bassa e chiusura. L'intervallo di prezzi in ogni categoria è nuovamente indicato da una linea verticale, mentre l'intervallo tra apertura e chiusura è dato da una barra galleggiante più ampia; se il prezzo aumenta nella categoria (chiusura è superiore all'apertura), la barra è riempita con un colore, mentre se il prezzo diminuisce, la barra è riempita con un altro. Questo tipo di grafico è spesso chiamato grafico a candela.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Miglioramenti della visibilità nel grafico**
Spesso usiamo colori anziché bianco e nero per indicare prezzi in aumento e diminuzione. Nel primo set di candlestick sottostante, il rosso mostra prezzi in aumento e il verde in diminuzione.

![todo:image_alt_text](sample2.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
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
