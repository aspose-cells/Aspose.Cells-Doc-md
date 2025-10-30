---
title: Creare e Gestire Grafici con Node.js tramite C++
linktitle: Grafici
description: Impara come usare Aspose.Cells per Node.js per creare grafici in Microsoft Excel. La nostra guida mostrerà vari tipi di grafici e come personalizzarne l’aspetto e la formattazione.
keywords: Aspose.Cells per Node.js, Creazione di Grafici, Microsoft Excel, Tipi di Grafici, Personalizzazione, Aspetto, Formattazione.
type: docs
weight: 130
url: /it/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

È possibile aggiungere una varietà di grafici ai fogli elettronici con Aspose.Cells. Aspose.Cells fornisce molti oggetti flessibili per la creazione dei grafici. Questo argomento discute gli oggetti per la creazione dei grafici di Aspose.Cells.

{{% /alert %}}

## **Creazione di grafici**

### **Creazione semplice di un grafico**
È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
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

Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando la collezione [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--). Ogni elemento nella collezione [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) rappresenta un oggetto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/). Un oggetto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) racchiude tutti gli altri oggetti di creazione di grafici necessari per personalizzare l’aspetto del grafico. La sezione successiva mostra come usare alcuni degli oggetti di creazione di grafici di base per creare un grafico semplice.

### **Crea un grafico utilizzando Aspose.Cells**

**Passaggi:**

1. Aggiungi alcuni dati alle celle del foglio di lavoro con il metodo [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-) dell’oggetto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/).
   Questo sarà utilizzato come origine dati per il grafico.
1. Aggiungi un grafico al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) della collezione [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection), racchiuso nell’oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/).
1. Specificare il tipo di grafico con l’enumerazione [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).
   Ad esempio, l’esempio sottostante utilizza il valore [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) come tipo di grafico.
1. Accedere al nuovo oggetto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) dalla collezione [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) passando il suo indice.
1. Usare qualsiasi degli oggetti di creazione di grafici racchiusi nell’oggetto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) per gestire il grafico.
   L’esempio sottostante utilizza l’oggetto di creazione di grafici [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) per specificare la sorgente dei dati del grafico.

Quando si aggiungono dati di origine al grafico, la fonte dei dati può essere un intervallo di celle (come "A1:C3"), o una sequenza di celle non contigue (come "A1, A3, A5"), o una sequenza di valori (come "1,2,3").

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizza diversi oggetti di grafici per creare grafici diversi.

È possibile creare molti tipi diversi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione chiamata [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Grafico a linee**

Nell'esempio sopra, basta cambiare [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) in *Line* per creare un grafico a linee. La fonte completa è fornita di seguito. Quando il codice viene eseguito, viene aggiunto un grafico a linee al foglio di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Grafico a bolle**

Per creare un grafico a bolle, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) deve essere impostato su [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) e alcune proprietà aggiuntive come BubbleSizes, Values e XValues devono essere impostate di conseguenza. Eseguendo il seguente codice, viene aggiunto un grafico a bolle al foglio di lavoro.

#### **Grafico a linee con marcatori di dati**

Per creare un grafico a linee con marcatori dati, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) deve essere impostato su *ChartType.LineWithDataMarkers* e alcune proprietà aggiuntive come area di sfondo, Marcatori di serie, Valori & XValues devono essere impostate di conseguenza. Eseguendo il seguente codice, viene aggiunto un grafico a linee con marcatori dati al foglio di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Argomenti avanzati**
- [Lettura e manipolazione dei grafici di Excel 2016](/cells/it/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Gestisci gli assi dei grafici di Excel](/cells/it/nodejs-cpp/chart-axes/)
- [Impostazione dell'aspetto del grafico](/cells/it/nodejs-cpp/setting-chart-appearance/)
- [Tipi di Grafico](/cells/it/nodejs-cpp/chart-types/)
- [Personalizzazione di Grafici](/cells/it/nodejs-cpp/customizing-charts/)
- [Imposta origine dati per il grafico](/cells/it/nodejs-cpp/data-formatting-in-charts/)
- [Gestisci le etichette dati dei grafici di Excel](/cells/it/nodejs-cpp/insert-datalabels-to-chart/)
- [Ottieni il foglio di lavoro del grafico](/cells/it/nodejs-cpp/get-worksheet-of-the-chart/)
- [Gestisci la leggenda dei grafici di Excel](/cells/it/nodejs-cpp/chart-legend/)
- [Manipolare posizione, dimensione e progettazione del grafico](/cells/it/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Creazione di un grafico a torta con linee guida](/cells/it/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Forme nei grafici](/cells/it/nodejs-cpp/controls-in-charts/)
- [Gestire i titoli dei grafici di Excel](/cells/it/nodejs-cpp/chart-and-axis-titles/)
- [Rendering del grafico](/cells/it/nodejs-cpp/chart-rendering/)
- [Ottieni il testo dell'equazione della retta di tendenza del grafico](/cells/it/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
