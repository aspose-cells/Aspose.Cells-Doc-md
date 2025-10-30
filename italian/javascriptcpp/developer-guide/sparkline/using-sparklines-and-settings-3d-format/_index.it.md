---
title: Utilizzo di Sparklines e impostazioni di formattazione 3D con JavaScript tramite C++
linktitle: Utilizzo di Sparklines e Impostazioni Formato 3D
type: docs
weight: 40
url: /it/javascript-cpp/using-sparklines-and-settings-3d-format/
description: Impara come usare Sparklines e applicare la formattazione 3D nei file Excel con Aspose.Cells for JavaScript tramite C++. 
---

## **Utilizzo delle Sparklines**
Microsoft Excel 2010 può analizzare le informazioni in modi più variati che mai. Consente agli utenti di monitorare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. Le Sparklines sono mini-grafici che è possibile inserire all'interno delle celle, in modo da poter visualizzare dati e grafici sulla stessa tabella. Quando le sparklines vengono utilizzate correttamente, l'analisi dei dati è più rapida e diretta. Forniscono inoltre una visione semplice delle informazioni, evitando fogli di lavoro affollati con molti grafici elaborati.

Aspose.Cells for JavaScript tramite C++ fornisce un'API per manipolare gli sparklines nei fogli di calcolo.
### **Le Sparklines in Microsoft Excel**
Per inserire sparklines in Microsoft Excel 2010:

1. Selezionare le celle in cui si desidera che compaiano le sparklines. Per renderle facili da visualizzare, selezionare le celle a lato dei dati.
1. Fare clic su **Inserisci** nella barra multifunzione e quindi scegliere **colonna** nel gruppo **Sparklines**.
1. Selezionare o inserire il intervallo di celle nel foglio di lavoro che contengono i dati di origine. I grafici compariranno.

Le Sparklines ti aiutano a visualizzare le tendenze, ad esempio, il record di vittorie o sconfitte per una lega di softball. Le Sparklines possono persino sommare l'intera stagione di ogni squadra nella lega.
### **Sparklines usando Aspose.Cells for JavaScript tramite C++**
Gli sviluppatori possono creare, eliminare o leggere gli sparklines (nel file modello) usando l'API fornita da Aspose.Cells for JavaScript tramite C++. Le classi che gestiscono gli sparklines sono contenute nel modulo [SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/), quindi è necessario richiedere questo modulo prima di usare queste funzionalità.

Aggiungendo grafici personalizzati per un determinato intervallo di dati, i programmatori hanno la libertà di aggiungere diversi tipi di piccoli grafici alle aree di celle selezionate.

L'esempio di seguito mostra la funzione Sparklines. L'esempio mostra come:

1. Aprire un semplice file modello.
1. Leggere le informazioni delle sparklines per un foglio di lavoro.
1. Aggiungere nuove sparklines per un dato intervallo di dati in un'area di celle.
1. Salvare il file Excel su disco.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sparkline Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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

            // Instantiate a Workbook by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Read the Sparklines from the worksheet (if any)
            const sparklinesCount = sheet.sparklineGroups.count;
            let logHtml = '';
            for (let i = 0; i < sparklinesCount; i++) {
                const group = sheet.sparklineGroups.get(i);
                logHtml += `sparkline group: type:${group.type}, sparkline items count:${group.sparklines.count}<br/>`;
                const sparklineCount = group.sparklines.count;
                for (let j = 0; j < sparklineCount; j++) {
                    const sparkline = group.sparklines.get(j);
                    logHtml += `sparkline: row:${sparkline.row}, col:${sparkline.column}, dataRange:${sparkline.dataRange}<br/>`;
                }
            }

            // Add Sparklines
            // Define the CellArea D2:D10 (rows and columns are zero-based: D is column 4 -> index 4)
            const ca = CellArea.createCellArea(1, 4, 7, 4);
            // Add new Sparklines for a data range to a cell area
            const idx = sheet.sparklineGroups.add(SparklineType.Column, "Sheet1!B2:D8", false, ca);
            const newGroup = sheet.sparklineGroups.get(idx);
            // Create CellsColor and set color
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            newGroup.seriesColor = clr;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><div>' + logHtml + '</div>';
        });
    </script>
</html>
```
## **Impostazione del Formato 3D**
Potresti aver bisogno di stili di grafico 3D in modo da ottenere solo i risultati adatti al tuo scenario. Aspose.Cells for JavaScript tramite C++ fornisce l'API pertinente per applicare la formattazione 3D di Microsoft Excel 2007.

Di seguito è riportato un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Microsoft Excel 2007. Dopo aver eseguito il codice di esempio, verrà aggiunto un grafico a colonne (con effetti 3D) al foglio di lavoro.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>3D Chart Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, BevelPresetType, PresetMaterialType, LightRigType } = AsposeCells;

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
            // Creating a new workbook
            const book = new Workbook();

            // Add a Data Worksheet
            const dataSheet = book.worksheets.add("DataSheet");

            // Add Chart Worksheet
            const sheet = book.worksheets.add("MyChart");

            // Put some values into the cells in the data worksheet
            dataSheet.cells.get("B1").value = 1;
            dataSheet.cells.get("B2").value = 2;
            dataSheet.cells.get("B3").value = 3;
            dataSheet.cells.get("A1").value = "A";
            dataSheet.cells.get("A2").value = "B";
            dataSheet.cells.get("A3").value = "C";

            // Define the Chart Collection
            const charts = sheet.charts;
            // Add a Column chart to the Chart Worksheet
            const chartSheetIdx = charts.add(ChartType.Column, 5, 0, 25, 15);

            // Get the newly added Chart
            const chart = book.worksheets.get(2).charts.get(0);

            // Set the background/foreground color for PlotArea/ChartArea
            chart.plotArea.area.backgroundColor = Color.White;
            chart.chartArea.area.backgroundColor = Color.White;
            chart.plotArea.area.foregroundColor = Color.White;
            chart.chartArea.area.foregroundColor = Color.White;

            // Hide the Legend
            chart.showLegend = false;

            // Add Data Series for the Chart
            chart.nSeries.add("DataSheet!B1:B3", true);
            // Specify the Category Data
            chart.nSeries.categoryData = "DataSheet!A1:A3";

            // Get the Data Series
            const ser = chart.nSeries.get(0);

            // Apply the 3-D formatting
            const spPr = ser.shapeProperties;
            const fmt3d = spPr.format3D;

            // Specify Bevel with its height/width
            const bevel = fmt3d.topBevel;
            bevel.type = BevelPresetType.Circle;
            bevel.height = 2;
            bevel.width = 5;

            // Specify Surface material type
            fmt3d.surfaceMaterialType = PresetMaterialType.WarmMatte;

            // Specify surface lighting type
            fmt3d.surfaceLightingType = LightRigType.ThreePoint;

            // Specify lighting angle
            fmt3d.lightingAngle = 20;

            // Specify Series background/foreground and line color
            ser.area.backgroundColor = Color.Maroon;
            ser.area.foregroundColor = Color.Maroon;
            ser.border.color = Color.Maroon;

            // Saving the modified Excel file and providing download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = '3d_format.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
