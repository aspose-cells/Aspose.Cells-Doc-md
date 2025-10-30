---
title: Crea un grafico azione alto basso chiusura (HLC) con JavaScript tramite C++
linktitle: Crea un grafico di scorta High Low Close (HLC)
description: Impara come creare un grafico azione alto basso chiusura (HLC) usando Aspose.Cells for JavaScript tramite C++. La nostra guida passo passo dimostrerà come tracciare dati di mercato azionario, inclusi prezzo alto, basso e di chiusura, su un grafico per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for JavaScript tramite C++, grafico azione alto basso chiusura (HLC), dati di mercato azionario, analisi, visualizzazione.
type: docs
weight: 181
url: /it/javascript-cpp/create-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**  
 Il grafico stock High-Low-Close (HLC) utilizza quattro colonne di dati. La prima colonna è una categoria, di solito una data ma possono essere utilizzati anche nomi di azioni. Le altre tre colonne in ordine sono per high, low e prezzi di chiusura. L'intervallo di prezzo per ogni categoria è indicato da una linea verticale da low a high, e il prezzo di chiusura viene mostrato utilizzando un segno di tick che si estende a destra di questa linea.  

![todo:image_alt_text](sample.png)  
## **Miglioramenti della visibilità nel grafico**  
A volte, per rendere il grafico più intuitivo, possiamo modificare l'aspetto del marcatore (chiusura), o farlo visualizzare sull'asse secondario.  

![todo:image_alt_text](sample2.png)  
## **Codice di Esempio**  
Il codice di esempio seguente carica il [file Excel di esempio](High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

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
