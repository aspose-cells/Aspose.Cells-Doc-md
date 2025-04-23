---
title: Usando Sparklines e impostazioni di formato 3D con Node.js tramite C++
linktitle: Utilizzo di Sparklines e Impostazioni Formato 3D
type: docs
weight: 40
url: /it/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Impara come usare sparklines e applicare la formattazione 3D nei file Excel con Aspose.Cells for Node.js via C++. 
---

## **Utilizzo delle Sparklines**
Microsoft Excel 2010 può analizzare le informazioni in modi più variati che mai. Consente agli utenti di monitorare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. Le Sparklines sono mini-grafici che è possibile inserire all'interno delle celle, in modo da poter visualizzare dati e grafici sulla stessa tabella. Quando le sparklines vengono utilizzate correttamente, l'analisi dei dati è più rapida e diretta. Forniscono inoltre una visione semplice delle informazioni, evitando fogli di lavoro affollati con molti grafici elaborati.

Aspose.Cells for Node.js via C++ fornisce un'API per manipolare le sparklines nei fogli di calcolo.
### **Le Sparklines in Microsoft Excel**
Per inserire sparklines in Microsoft Excel 2010:

1. Selezionare le celle in cui si desidera che compaiano le sparklines. Per renderle facili da visualizzare, selezionare le celle a lato dei dati.
1. Fare clic su **Inserisci** nella barra multifunzione e quindi scegliere **colonna** nel gruppo **Sparklines**.
1. Selezionare o inserire il intervallo di celle nel foglio di lavoro che contengono i dati di origine. I grafici compariranno.

Le Sparklines ti aiutano a visualizzare le tendenze, ad esempio, il record di vittorie o sconfitte per una lega di softball. Le Sparklines possono persino sommare l'intera stagione di ogni squadra nella lega.
### **Sparklines usando Aspose.Cells for Node.js via C++**
Gli sviluppatori possono creare, eliminare o leggere sparklines (nel file modello) usando l'API fornita da Aspose.Cells for Node.js via C++. Le classi che gestiscono le sparklines sono contenute nel modulo [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/), quindi è necessario richiedere questo modulo prima di usare queste funzionalità.

Aggiungendo grafici personalizzati per un determinato intervallo di dati, i programmatori hanno la libertà di aggiungere diversi tipi di piccoli grafici alle aree di celle selezionate.

L'esempio di seguito mostra la funzione Sparklines. L'esempio mostra come:

1. Aprire un semplice file modello.
1. Leggere le informazioni delle sparklines per un foglio di lavoro.
1. Aggiungere nuove sparklines per un dato intervallo di dati in un'area di celle.
1. Salvare il file Excel su disco.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **Impostazione del Formato 3D**
Potresti aver bisogno di stili di grafico 3D per ottenere solo i risultati per il tuo scenario. Aspose.Cells for Node.js via C++ fornisce l'API pertinente per applicare la formattazione 3D di Microsoft Excel 2007.

Di seguito è riportato un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Microsoft Excel 2007. Dopo aver eseguito il codice di esempio, verrà aggiunto un grafico a colonne (con effetti 3D) al foglio di lavoro.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
