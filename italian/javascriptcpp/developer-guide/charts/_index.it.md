---
title: Creare e gestire grafici con JavaScript tramite C++
linktitle: Grafici
description: Impara come usare Aspose.Cells for JavaScript tramite C++ per creare grafici in Microsoft Excel. La nostra guida dimostrerà vari tipi di grafico e come personalizzare il loro aspetto e formattazione.
keywords: Aspose.Cells for JavaScript tramite C++, Creazione di grafici, Microsoft Excel, Tipi di grafici, Personalizzazione, Aspetto, Formattazione.
type: docs
weight: 130
url: /it/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

È possibile aggiungere una varietà di grafici ai fogli elettronici con Aspose.Cells. Aspose.Cells fornisce molti oggetti flessibili per la creazione dei grafici. Questo argomento discute gli oggetti per la creazione dei grafici di Aspose.Cells.

{{% /alert %}}

## **Creazione di grafici**

### **Creazione semplice di un grafico**
È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Cose da sapere per creare un grafico**

Prima di creare grafici, è importante comprendere alcuni concetti di base utili quando si utilizzano Aspose.Cells.

#### **Oggetti per la creazione dei grafici**

Gli oggetti di creazione di grafici sono elencati di seguito:

- Serie, una singola serie di dati in un grafico.
- Asse, l'asse di un grafico.
- Grafico, un singolo grafico di Excel.
- Area del grafico, l'area del grafico nel foglio di lavoro.
- ChartDataTable, una tabella dati del grafico.
- ChartFrame, l'oggetto frame in un grafico.
- ChartPoint, un singolo punto in una serie in un grafico.
- ChartPointCollection, una raccolta che contiene tutti i punti di una serie.
- Grafici, una collezione di oggetti Chart.
- DataLabels, una collezione di tutti gli oggetti DataLabel per la serie specificata.
- FillFormat, formato di riempimento per una forma.
- Pavimento, il pavimento di un grafico 3D.
- Legenda, la legenda del grafico.
- Linea, la linea del grafico.
- SeriesCollection, una collezione di oggetti Series.
- TickLabels, le etichette contrassegnate associate ai contrassegni su un asse del grafico.
- Titolo, il titolo di un grafico o asse.
- Linea di tendenza, una linea di tendenza in un grafico.
- TrendlineCollection, una collezione di tutti gli oggetti Linea di tendenza per la serie di dati specificata.
- Pareti, le pareti di un grafico 3D.

#### **Utilizzo di oggetti di tracciamento**

Come già detto, tutti gli oggetti di tracciamento sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire compiti specifici. Utilizzare gli oggetti di tracciamento per creare grafici.

Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando la collezione [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--). Ogni elemento nella collezione [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) rappresenta un oggetto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/). Un oggetto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) racchiude tutti gli altri oggetti di creazione di grafici necessari per personalizzare l’aspetto del grafico. La sezione successiva mostra come usare alcuni degli oggetti di creazione di grafici di base per creare un grafico semplice.

### **Crea un grafico utilizzando Aspose.Cells**



1. Aggiungi alcuni dati alle celle del foglio di lavoro con il metodo [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-) dell’oggetto [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).
   Questo sarà utilizzato come origine dati per il grafico.
2. Aggiungi un grafico al foglio chiamando il metodo [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-) della collezione [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection), racchiuso nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/).
3. Specificare il tipo di grafico con l'enumerazione [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).
   Ad esempio, l’esempio sottostante utilizza il valore [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) come tipo di grafico.
4. Accedere al nuovo oggetto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) dalla raccolta [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) passando il suo indice.
5. Usare uno qualsiasi degli oggetti di grafico racchiusi nell'oggetto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) per gestire il grafico.
   L’esempio sottostante utilizza l’oggetto di creazione di grafici [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) per specificare la sorgente dei dati del grafico.

Quando si aggiungono dati di origine al grafico, la fonte dei dati può essere un intervallo di celle (come "A1:C3"), o una sequenza di celle non contigue (come "A1, A3, A5"), o una sequenza di valori (come "1,2,3").

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizza diversi oggetti di grafici per creare grafici diversi.

È possibile creare molti tipi diversi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione chiamata [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).

I tipi di grafico predefiniti sono:

|**Tipi di grafico**|**Descrizione**|
| :- | :- |
|Column|Rappresenta il grafico a colonne raggruppate|
|ColumnStacked|Rappresenta il grafico a colonne sovrapposte|
|Column100PercentStacked|Rappresenta il grafico a colonne sovrapposte al 100%|
|Column3DClustered|Rappresenta il grafico a colonne raggruppate in 3D|
|Column3DStacked|Rappresenta il grafico a colonne sovrapposte in 3D|
|Column3D100PercentStacked|Rappresenta il grafico a colonne sovrapposte al 100% in 3D|
|Column3D|Rappresenta il grafico a colonne 3D|
|Bar|Rappresenta il grafico a barre raggruppate|
|BarStacked|Rappresenta il grafico a barre sovrapposte|
|Bar100PercentStacked|Rappresenta il grafico a barre sovrapposte al 100%|
|Bar3DClustered|Rappresenta il grafico a barre raggruppate 3D|
|Bar3DStacked|Rappresenta il grafico a barre sovrapposte 3D|
|Bar3D100PercentStacked|Rappresenta il grafico a barre sovrapposte al 100% 3D|
|Line|Rappresenta il grafico a linee|
|LineStacked|Rappresenta il grafico a linee sovrapposte|
|Line100PercentStacked|Rappresenta il grafico a linee sovrapposte al 100%|
|LineWithDataMarkers|Rappresenta il grafico a linee con marcatori di dati|
|LineStackedWithDataMarkers|Rappresenta il grafico a linee sovrapposte con marcatori di dati|
|Line100PercentStackedWithDataMarkers|Rappresenta il grafico a linee sovrapposte al 100% con marcatori di dati|
|Line3D|Rappresenta il grafico a linee 3D|
|Pie|Rappresenta il grafico a torta|
|Pie3D|Rappresenta il grafico a torta 3D|
|PiePie|Rappresenta il grafico a torta delle torte|
|PieExploded|Rappresenta il grafico a torta esplosa|
|Pie3DExploded|Rappresenta il grafico a torta 3D esplosa|
|PieBar|Rappresenta il grafico a barre delle torte|
|Scatter|Rappresenta il grafico a dispersione|
|ScatterConnectedByCurvesWithDataMarker|Rappresenta un grafico a dispersione collegato da curve, con indicatori di dati|
|ScatterConnectedByCurvesWithoutDataMarker|Rappresenta un grafico a dispersione collegato da curve, senza indicatori di dati|
|ScatterConnectedByLinesWithDataMarker|Rappresenta un grafico a dispersione collegato da linee, con indicatori di dati|
|ScatterConnectedByLinesWithoutDataMarker|Rappresenta un grafico a dispersione collegato da linee, senza indicatori di dati|
|Area|Rappresenta un grafico ad aree|
|AreaStacked|Rappresenta un grafico ad aree sovrapposte|
|Area100PercentStacked|Rappresenta un grafico ad aree 100% sovrapposte|
|Area3D|Rappresenta un grafico ad aree 3D|
|Area3DStacked|Rappresenta un grafico ad aree sovrapposte 3D|
|Area3D100PercentStacked|Rappresenta un grafico ad aree 100% sovrapposte 3D|
|Doughnut|Rappresenta un grafico a ciambella|
|DoughnutExploded|Rappresenta un grafico a ciambella esplosa|
|Radar|Rappresenta un grafico radar|
|RadarWithDataMarkers|Rappresenta un grafico radar con indicatori di dati|
|RadarFilled|Rappresenta un grafico radar riempito|
|Surface3D|Rappresenta un grafico a superficie 3D|
|SurfaceWireframe3D|Rappresenta un grafico a superficie in filo 3D|
|SurfaceContour|Rappresenta un grafico a contorni|
|SurfaceContourWireframe|Rappresenta un grafico a contorni in filo|
|Bubble|Rappresenta il grafico a bolle|
|Bubble3D|Rappresenta il grafico a bolle in 3D|
|Cylinder|Rappresenta il grafico a cilindro|
|CylinderStacked|Rappresenta il grafico a cilindro sovrapposto|
|Cylinder100PercentStacked|Rappresenta il grafico a cilindro sovrapposto al 100%|
|CylindericalBar|Rappresenta il grafico a barre cilindriche|
|CylindericalBarStacked|Rappresenta il grafico a barre cilindriche sovrapposte|
|CylindericalBar100PercentStacked|Rappresenta il grafico a barre cilindriche sovrapposte al 100%|
|CylindericalColumn3D|Rappresenta il grafico a colonne cilindriche in 3D|
|Cone|Rappresenta il grafico a cono|
|ConeStacked|Rappresenta il grafico a cono sovrapposto|
|Cone100PercentStacked|Rappresenta il grafico a cono sovrapposto al 100%|
|ConicalBar|Rappresenta il grafico a barre coniche|
|ConicalBarStacked|Rappresenta il grafico a barre coniche sovrapposte|
|ConicalBar100PercentStacked|Rappresenta il grafico a barre coniche sovrapposte al 100%|
|ConicalColumn3D|Rappresenta il grafico a colonne coniche in 3D|
|Pyramid|Rappresenta il grafico a piramide|
|PyramidStacked|Rappresenta il grafico a piramide sovrapposta|
|Pyramid100PercentStacked|Rappresenta il grafico a piramide sovrapposta al 100%|
|PyramidBar|Rappresenta il grafico a barre piramidali|
|PyramidBarStacked|Rappresenta il grafico a barre a piramide sovrapposte
|PyramidBar100PercentStacked|Rappresenta il grafico a barre a piramide 100% sovrapposte
|PyramidColumn3D|Rappresenta il grafico a colonne a piramide 3D

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, è possibile impostare solo l'intervallo da in alto a sinistra a in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" non è valido.

{{% /alert %}}

#### **Grafico a piramide**

Quando il codice di esempio viene eseguito, viene aggiunto un grafico a piramide al foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

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
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Grafico a linee**

Nell'esempio sopra, basta cambiare [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) in *Line* per creare un grafico a linee. La fonte completa è fornita di seguito. Quando il codice viene eseguito, viene aggiunto un grafico a linee al foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

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
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Grafico a bolle**

Per creare un grafico a bolle, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) deve essere impostato su [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) e alcune proprietà aggiuntive come BubbleSizes, Values e XValues devono essere impostate di conseguenza. Eseguendo il seguente codice, viene aggiunto un grafico a bolle al foglio di lavoro.

#### **Grafico a linee con marcatori di dati**

Per creare un grafico a linee con marcatori dati, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) deve essere impostato su *ChartType.LineWithDataMarkers* e alcune proprietà aggiuntive come area di sfondo, Marcatori di serie, Valori & XValues devono essere impostate di conseguenza. Eseguendo il seguente codice, viene aggiunto un grafico a linee con marcatori dati al foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
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
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Lettura e manipolazione dei grafici di Excel 2016](/cells/it/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Gestisci gli assi dei grafici di Excel](/cells/it/javascript-cpp/chart-axes/)
- [Impostazione dell'aspetto del grafico](/cells/it/javascript-cpp/setting-chart-appearance/)
- [Tipi di Grafico](/cells/it/javascript-cpp/chart-types/)
- [Personalizzazione di Grafici](/cells/it/javascript-cpp/customizing-charts/)
- [Imposta origine dati per il grafico](/cells/it/javascript-cpp/data-formatting-in-charts/)
- [Gestisci le etichette dati dei grafici di Excel](/cells/it/javascript-cpp/insert-datalabels-to-chart/)
- [Ottieni il foglio di lavoro del grafico](/cells/it/javascript-cpp/get-worksheet-of-the-chart/)
- [Gestisci la leggenda dei grafici di Excel](/cells/it/javascript-cpp/chart-legend/)
- [Manipolare posizione, dimensione e progettazione del grafico](/cells/it/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [Creazione di un grafico a torta con linee guida](/cells/it/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [Forme nei grafici](/cells/it/javascript-cpp/controls-in-charts/)
- [Gestire i titoli dei grafici di Excel](/cells/it/javascript-cpp/chart-and-axis-titles/)
- [Rendering del grafico](/cells/it/javascript-cpp/chart-rendering/)
- [Ottieni il testo dell'equazione della retta di tendenza del grafico](/cells/it/javascript-cpp/get-equation-text-of-chart-trendline/)
