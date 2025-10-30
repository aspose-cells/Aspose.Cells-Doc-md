---
title: Manipola la posizione, le dimensioni e il designer del grafico con JavaScript tramite C++
linktitle: Manipolare Posizione, Dimensione e Progettazione del Grafico
description: Impara come usare Aspose.Cells for JavaScript tramite C++ per manipolare efficacemente la posizione, le dimensioni e il designer del grafico in Microsoft Excel. La nostra guida dimostrerà come regolare queste proprietà per un layout e una visualizzazione migliorati.
keywords: Aspose.Cells for JavaScript tramite C++, Posizione, Dimensioni, Designer del grafico, Microsoft Excel, Layout, Visualizzazione.
type: docs
weight: 45
url: /it/javascript-cpp/manipulate-position-size-and-designer-chart/
---

## **Posizione e Dimensione del Grafico**
A volte si desidera cambiare la posizione o le dimensioni del grafico nuovo o esistente all'interno del foglio di calcolo. Aspose.Cells fornisce la proprietà [Chart.chartObject](https://reference.aspose.com/cells/javascript-cpp/chart/#chartObject--) per farlo. Puoi usare le sue sotto-proprietà per ridimensionare il grafico con una nuova altezza e larghezza o per riposizionarlo con nuove coordinate X e Y.

### **Controllo Posizione e Dimensione del Grafico**
Per modificare la posizione (coordinate X, Y) o la dimensione (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [Shape.x](https://reference.aspose.com/cells/javascript-cpp/shape/#x--)
1. [Shape.y](https://reference.aspose.com/cells/javascript-cpp/shape/#y--)
1. [Shape.height](https://reference.aspose.com/cells/javascript-cpp/shape/#height--)
1. [Shape.width](https://reference.aspose.com/cells/javascript-cpp/shape/#width--)

L’esempio seguente spiega l’uso delle API sopra; carica il workbook esistente che contiene un grafico nel suo primo foglio di lavoro. Poi ridimensiona e riposiziona il grafico usando Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Resize and Reposition Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the second worksheet in the Excel file (index 1)
            const worksheet = workbook.worksheets.get(1);

            // Load the chart from source worksheet (first chart)
            const chart = worksheet.charts.get(0);

            // Resize the chart
            chart.chartObject.width = 400;
            chart.chartObject.height = 300;

            // Reposition the chart
            chart.chartObject.x = 250;
            chart.chartObject.y = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart resized and repositioned successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Manipolazione dei Grafici del Designer**
Ci sono momenti in cui è necessario manipolare o modificare grafici nei file di modello del designer. Aspose.Cells supporta pienamente la manipolazione dei contenuti e degli elementi del grafico del designer. I dati, i contenuti del grafico, l’immagine di sfondo e la formattazione possono essere preservati con precisione.

### **Manipolazione dei Grafici del Designer nei File di Modello**
Per manipolare i grafici del designer nei file modello, usa l’API relativa ai grafici. Ad esempio, puoi usare la proprietà Worksheet.charts per ottenere la collezione di grafici esistenti nel file del modello.

#### **Creazione di un Grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo successivamente questo grafico.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Pyramid Chart</h1>
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
            await readyPromise;

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Manipolazione del Grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato in precedenza. Nell'output generato, si noti che l'etichetta di data di un punto dati è stata impostata su 'Regno Unito, 30K'.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pie Chart Data Label Update</title>
    </head>
    <body>
        <h1>Update Pie Chart Data Label Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Get the data labels in the data series of the third data point.
            const dataLabels = chart.nSeries.get(0).points.get(2).dataLabels;

            // Change the text of the label.
            dataLabels.text = "Unided Kingdom, 400K ";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Manipolazione di un Grafico a Linee nel Modello del Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e ne cambieremo i colori delle linee.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);

            // Add the third data series to it.
            chart.nSeries.add("{60, 80, 10}", true);

            // Add another data series (fourth) to it.
            chart.nSeries.add("{0.3, 0.7, 1.2}", true);

            // Plot the fourth data series on the second axis.
            chart.nSeries.get(3).plotOnSecondAxis = true;

            // Change the Border color of the second data series.
            chart.nSeries.get(1).border.color = AsposeCells.Color.Green;

            // Change the Border color of the third data series.
            chart.nSeries.get(2).border.color = AsposeCells.Color.Red;

            // Make the second value axis visible.
            chart.secondValueAxis.isVisible = true;

            // Save the excel file and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
