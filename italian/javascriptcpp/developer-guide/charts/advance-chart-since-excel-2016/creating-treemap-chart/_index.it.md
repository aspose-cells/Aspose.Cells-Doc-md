---
title: Come creare un grafico Treemap con JavaScript tramite C++
linktitle: Come creare un grafico TreeMap
description: Impara come creare un grafico Treemap in Aspose.Cells for JavaScript tramite C++. La nostra guida ti aiuterà a comprendere le varie proprietà e opzioni di formattazione disponibili per i grafici Treemap, inclusi colori, etichette e rappresentazione dei dati.
keywords: Aspose.Cells for JavaScript tramite C++, grafico Treemap, crea, proprietà, formattazione, colori, etichette, rappresentazione dei dati, grafico circolare, grafica gerarchica.
type: docs
weight: 161
url: /it/javascript-cpp/creating-treemap-chart/
---

## **Possibili Scenari di Utilizzo**  
Un grafico a mappa a riquadri fornisce una visualizzazione gerarchica dei tuoi dati e rende facile individuare modelli, ad esempio quali articoli sono i più venduti in un negozio. I rami dell'albero sono rappresentati da rettangoli e ogni sotto-ramo è mostrato come un rettangolo più piccolo. Il grafico a mappa a riquadri visualizza le categorie per colore e prossimità e può facilmente mostrare molti dati che sarebbero difficili da visualizzare con altri tipi di grafico.  

![todo:image_alt_text](sample.png)  
## **Grafico TreeMap**  
Dopo aver eseguito il codice qui sotto, vedrai il grafico TreeMap come mostrato di seguito.  

![todo:image_alt_text](result.png)  
## **Codice di Esempio**  
Il seguente codice di esempio carica il [file Excel di esempio](treemap.xlsx) e genera il [file Excel di output](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
