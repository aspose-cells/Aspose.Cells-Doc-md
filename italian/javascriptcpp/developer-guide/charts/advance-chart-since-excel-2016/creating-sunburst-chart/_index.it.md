---
title: Come creare un grafico Sunburst con JavaScript tramite C++
linktitle: Come creare un grafico Sunburst
description: Impara come creare un grafico sunburst in Aspose.Cells for JavaScript tramite C++, un grafico che presenta i dati in un cerchio. La nostra guida ti aiuterà a configurare varie proprietà e formati del grafico, inclusi etichette dati, legende, colori e altro.
keywords: Aspose.Cells for JavaScript tramite C++, grafico sunburst, crea, imposta proprietà, etichette dati, legenda, formattazione, colore, cerchio, rendering dati.
type: docs
weight: 162
url: /it/javascript-cpp/creating-sunburst-chart/
---

## **Possibili Scenari di Utilizzo**
I grafici a mappa ad albero sono utili per confrontare le proporzioni all’interno della gerarchia; tuttavia, i grafici a mappa ad albero non sono ottimali per mostrare i livelli gerarchici tra le categorie più grandi e ogni punto dati. Un grafico sunburst è molto più efficace per mostrare ciò. Il grafico sunburst è ideale per visualizzare dati gerarchici. Ogni livello della gerarchia è rappresentato da un anello o cerchio, con il cerchio più interno come il vertice della gerarchia. Un grafico sunburst senza dati gerarchici (un livello di categorie) assomiglia a un grafico a ciambella. Tuttavia, un grafico sunburst con più livelli di categorie mostra come gli anelli esterni si relazionano con quelli interni. Il grafico sunburst è più efficace nel mostrare come un anello si suddivide nei suoi componenti, mentre un altro tipo di grafico gerarchico, il grafico mappa ad albero, è ideale per confrontare le dimensioni relative.

![todo:image_alt_text](sample.png)
## **Grafico sunburst**
Dopo aver eseguito il codice qui sotto, vedrai il grafico Sunburst come mostrato di seguito.

![todo:image_alt_text](result.png)
## **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](sunburst.xlsx) e genera il [file Excel di output](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
