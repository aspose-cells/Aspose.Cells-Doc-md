---
title: Come creare un diagramma di Gantt con JavaScript tramite C++
linktitle: Come creare un diagramma di Gantt
type: docs
weight: 72
url: /it/javascript-cpp/how-to-create-gantt-chart/
description: Scopri come creare un diagramma di Gantt con Aspose.Cells for JavaScript tramite API C++.
keywords: JavaScript crea un diagramma di Gantt, aggiungi un diagramma di Gantt, inserisci un diagramma di Gantt
---

## **Che cos'è un diagramma di Gantt**

Un diagramma di Gantt è un tipo di diagramma a barre che illustra un programma di progetto. Mostra le date di inizio e fine delle varie componenti di un progetto. Ogni attività è rappresentata da una barra, con la sua lunghezza corrispondente alla durata. I diagrammi di Gantt indicano anche le dipendenze tra le attività, permettendo ai project manager di visualizzare la sequenza in cui le attività devono essere completate. Sono ampiamente usati nella gestione di progetti per pianificare, programmare e monitorare efficacemente i progetti.

## **Come creare un diagramma di Gantt in Excel**

Puoi creare un diagramma di Gantt in Excel seguendo questi passaggi:
1. Aggiungi alcuni dati per il diagramma di Gantt. 
<br>
<img src="00.png" width=50% />
1. Seleziona i dati e vai su Inserisci --> Grafici --> Inserisci grafico a colonne o barre --> Grafico a barre impilate. Nel nostro esempio, sono B1:B7, quindi inserisci un grafico **Barra impilata**.
<br>
<img src="1.png" width=50% />

1. Seleziona il grafico, **Seleziona dati** -> **Aggiungi**, imposta il **Nome serie** e i **Valori serie** come segue.
<br>
<img src="2.png" width=50% />

1. Seleziona il grafico, modifica le **Etichette dell'asse orizzontale (Categoria)**.
<br>
<img src="3.png" width=50% />

1. **Formatta l'asse** Y, seleziona **Categorie in ordine inverso**.
1. Seleziona la **Serie Blu** e imposta **Riempimento -> Nessun riempimento**.
1. **Formatta l'asse** X, imposta i valori **Minimo e Massimo** (01/05/2019: 43470, 30/01/2019: 43494).
<br>
<img src="4.png" width=50% />

1. **Aggiungi etichette dati** al grafico, ora otterrai un diagramma di Gantt.
<br>
<img src="0.png" width=50% />


## **Come aggiungere un diagramma di Gantt in Aspose.Cells**
Vedi il seguente esempio di codice. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati esempio. Poi crea il grafico a barre impilate in base ai dati iniziali e imposta le proprietà pertinenti. Infine, salva il workbook in formato [output XLSX](result.xlsx). Lo screenshot seguente mostra il diagramma di Gantt creato da Aspose.Cells nel file Excel di output.
<br>
<img src="5.png" width=60% />

### **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
