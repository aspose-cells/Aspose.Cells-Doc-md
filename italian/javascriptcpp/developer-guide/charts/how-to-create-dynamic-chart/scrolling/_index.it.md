---
title: Come creare un grafico di scorrimento dinamico con JavaScript tramite C++
linktitle: Come creare un grafico dinamico a scorrimento
description: Impara come creare un grafico di scorrimento dinamico usando Aspose.Cells for JavaScript tramite C++. La nostra guida passo passo dimostrerà come implementare transizioni di dati fluide e scorrimento automatico nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells for JavaScript tramite C++, grafico di scorrimento dinamico, transizioni di dati, scorrimento fluido, visualizzazione continua, aggiornamento delle visualizzazioni.
type: docs
weight: 75
url: /it/javascript-cpp/create-dynamic-scrolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento è un tipo di rappresentazione grafica utilizzato per visualizzare dati che cambiano nel tempo. È progettato per fornire una visualizzazione in tempo reale dei dati, consentendo agli utenti di monitorare aggiornamenti e tendenze continui. Il grafico si aggiorna continuamente man mano che vengono aggiunti nuovi dati e scorre automaticamente per mostrare le informazioni più recenti.

I grafici dinamici a scorrimento sono comunemente utilizzati in vari settori, come finanza, analisi del mercato azionario, tracciamento del meteo e analisi dei social media. Consentono agli utenti di visualizzare e analizzare pattern di dati e prendere decisioni informate basate su informazioni in tempo reale.

Questi grafici sono tipicamente interattivi, consentendo all'utente di ingrandire o ridurre, scorrere attraverso dati storici e regolare gli intervalli temporali. Spesso supportano più serie di dati, fornendo una visione completa di diverse metriche e le loro correlazioni.

In generale, i grafici di scorrimento dinamici sono strumenti preziosi per monitorare e analizzare i dati a serie temporali, facilitando la presa delle decisioni in tempo reale e potenziando le capacità di visualizzazione dei dati.

## **Usa Aspose.Cells per creare un Grafico Scorrevole Dinamico**
Nei paragrafi seguenti, ti mostreremo come creare un grafico di scorrimento dinamico utilizzando Aspose.Cells for JavaScript tramite C++. Mostreremo il codice dell’esempio, nonché il file Excel creato con questo codice.

## **Codice di Esempio**
Il codice di esempio seguente genererà il [File del grafico di scorrimento dinamico](DynamicScrollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Note**
Nel file generato, è possibile operare sulla barra di scorrimento, mentre il grafico conta dinamicamente gli ultimi 10 set di dati. Ciò viene fatto utilizzando la formula "OFFSET" nel codice di esempio:
