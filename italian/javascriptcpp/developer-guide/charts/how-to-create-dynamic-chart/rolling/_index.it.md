---
title: Come creare un grafico dinamico a rotazione con JavaScript tramite C++
linktitle: Come creare un grafico dinamico a scorrimento
description: Impara come creare un grafico dinamico a rotazione usando Aspose.Cells for JavaScript tramite C++. La nostra guida dimostrerà come implementare transizioni di dati fluide e medie mobili nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells for JavaScript tramite C++, grafico dinamico a rotazione, transizioni di dati, medie mobili fluide, visualizzazione continua, aggiornamento delle visualizzazioni.
type: docs
weight: 74
url: /it/javascript-cpp/create-dynamic-rolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento si riferisce a una rappresentazione grafica che visualizza costantemente punti dati in continuo spostamento e aggiornamento nel tempo. È un tipo di grafico che si aggiorna continuamente, mostrando una finestra mobile dei punti dati più recenti mentre scarta i punti dati più vecchi man mano che ne arrivano di nuovi.

I grafici dinamici a scorrimento sono comunemente utilizzati per visualizzare tendenze e pattern in dati in tempo reale o in streaming. Sono particolarmente utili in scenari in cui gli aspetti temporali e i cambiamenti nel tempo sono fondamentali, come l'analisi di mercato azionario, il monitoraggio meteorologico o il tracciamento delle performance in tempo reale.

Questi grafici di solito impiegano meccanismi di animazione o autoscrolling per assicurare che le informazioni più aggiornate siano sempre presentate. La lunghezza della finestra mobile può essere personalizzata per mostrare un periodo temporale specifico, come l'ultima ora, giorno o settimana.

In sintesi, un grafico dinamico a scorrimento è una rappresentazione grafica continuamente aggiornata che visualizza gli ultimi punti dati mentre scarta quelli più vecchi, consentendo agli utenti di osservare tendenze e pattern in tempo reale.

## **Usa Aspose Cells per creare un grafico dinamico a scorrimento**
Nei paragrafi successivi, ti mostreremo come creare un grafico dinamico a scorrimento utilizzando Aspose.Cells. Ti mostreremo il codice dell'esempio, nonché il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del Grafico Dinamico a Scorrimento](DynamicRollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Note**
Nel file generato, puoi continuare ad aggiungere dati nelle colonne A e B, mentre il grafico conta dinamicamente gli ultimi 5 set di dati. Ciò viene fatto utilizzando la formula "SCARTO" nel codice di esempio:
