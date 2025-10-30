---
title: Personalizzazione dei grafici con JavaScript via C++
linktitle: Personalizzazione dei grafici
description: Impara come personalizzare i grafici in Script via C++. La nostra guida ti mostrerà come modificare layout, aggiungere e formattare serie di dati, regolare gli assi e applicare varie opzioni di formattazione per migliorare l aspetto e l usabilità dei tuoi grafici.
keywords: Script via C++, creazione grafici, personalizzazione, layout, serie di dati, assi, formattazione, aspetto, usabilità.
type: docs
weight: 40
url: /it/javascript-cpp/customizing-charts/
---

## **Creazione di grafici personalizzati**  

Finora, quando abbiamo discusso di grafici, abbiamo considerato i grafici standard con le loro impostazioni di formattazione standard. Definiamo solo la sorgente dati, impostiamo alcune proprietà, e il grafico viene creato con le impostazioni di formato predefinite. Ma le API di Aspose.Cells supportano anche la creazione di grafici personalizzati che permettono agli sviluppatori di creare grafici con le proprie impostazioni di formato.  

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.  

Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells è rappresentata da un oggetto [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) mentre l'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) funge da collezione di oggetti [**Series**](https://reference.aspose.com/cells/javascript-cpp/series). Quando si crea un grafico personalizzato, gli sviluppatori hanno libertà di usare diversi tipi di grafici per diverse serie di dati (raccolte nell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)).  

Il codice di esempio di seguito dimostra come creare grafici personalizzati. In questo esempio, utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Attualmente, Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, linee, colonne e colonne impilate, ma altri grafici saranno supportati in future versioni.  

{{% /alert %}}
