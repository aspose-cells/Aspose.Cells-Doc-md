---
title: Gestisci DataLabels dei grafici di Excel con JavaScript tramite C++
description: Impara come gestire efficacemente le etichette dei dati nei grafici di Excel usando Script via C++. Questa guida completa copre varie operazioni di gestione, tra cui aggiunta, rimozione e modifica delle etichette per migliorare leggibilità e usabilità del grafico.
keywords: Script via C++, grafici Excel, etichette dei dati, gestione, leggibilità, usabilità, aggiunta, rimozione, modifica.
linktitle: Etichette dei dati
type: docs
weight: 50
url: /it/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

Le etichette dei dati sono una parte importante di un grafico.  
Possiamo conoscere facilmente il valore, la percentuale, ecc. di ciascuna serie  

{{% /alert %}}  

## **Opzioni delle etichette dei dati**  
Script via C++ permette anche di gestire le etichette dei dati del grafico in tempo reale, con l'oggetto [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/), è semplice spostare, aggiornare e formattare le etichette dei dati del grafico.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Gestisci le etichette dei dati del grafico**  
È semplice gestire le etichette dei dati del grafico con Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/).  

Il seguente snippet di codice dimostra come gestire le DataLabels:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Argomenti avanzati**  
- [Aggiunta di etichette personalizzate ai punti dati della serie del grafico](/cells/it/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Disabilita il testo a capo per le etichette dei dati del grafico](/cells/it/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Ridimensiona la forma dell'etichetta dati del grafico per adattarla al testo](/cells/it/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Etichetta dati personalizzata in formato testo ricco del punto del grafico](/cells/it/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Imposta il tipo di forma delle etichette dati del grafico](/cells/it/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Mostra l'intervallo di celle come etichette dati](/cells/it/javascript-cpp/showing-cell-range-as-the-data-labels/)
