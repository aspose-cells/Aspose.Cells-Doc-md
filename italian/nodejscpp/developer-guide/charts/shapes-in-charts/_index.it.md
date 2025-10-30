---
title: Shapes in Charts with Node.js via C++
linktitle: Forme nei grafici
description: Impara come usare Aspose.Cells for Node.js via C++ per aggiungere controlli e personalizzare grafici in Microsoft Excel. Questa guida dimostra come manipolare gli elementi del grafico, regolare la formattazione e migliorare l’aspetto e l’usabilità complessiva dei tuoi grafici.
keywords: Aspose.Cells for Node.js via C++, Controlli del grafico, Personalizzazione del grafico, Microsoft Excel, Elementi del grafico, Formattazione.
type: docs
weight: 70
url: /it/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
A volte è necessario inserire oggetti disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico durante l'esecuzione.
{{% /alert %}}

## **Aggiunta del Controllo Etichetta al Grafico**

Le etichette forniscono un modo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo. Aspose.Cells consente di aggiungere e manipolare le etichette anche nei grafici.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) fornisce un metodo chiamato [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-), utilizzato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **sinistra** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.
- **larghezza** – la larghezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.

Il metodo restituisce l'oggetto [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/). La classe [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) rappresenta un'etichetta nel grafico. Ha alcuni membri importanti:

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (proprietà) – specifica una stringa di sottotitolo dell'etichetta.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (proprietà) – specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione (**exp_piechart.xls**) che ha un grafico al suo interno. Usiamo questo file per inserire un'etichetta nel grafico. Di seguito è riportato il codice originale per aggiungere un'etichetta al grafico. L'output seguente viene generato durante l'esecuzione del codice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Aggiunta del controllo TextBox al grafico**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, inserire del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte. La classe [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) fornisce un metodo chiamato [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), che viene utilizzato per aggiungere un controllo casella di testo a un grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **height** – l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **width** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/). La classe [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico. Di seguito è riportato il codice originale per aggiungere una casella di testo al grafico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Aggiunta di un'immagine al grafico**

Aspose.Cells consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o ai suoi contenuti, o inserisci un file immagine del marchio.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) fornisce un metodo chiamato [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), che viene utilizzato per aggiungere un oggetto immagine al grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **stream** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScale** – la scala dell'altezza dell'immagine, un valore percentuale.

Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). La classe [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire un'immagine nel grafico. Di seguito è riportato il codice originale per aggiungere un'immagine al grafico.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Aggiunta di una casella di controllo nel grafico**

Aspose.Cells consente di inserire caselle di controllo in un foglio grafico utilizzando l'enumerazione [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/). L'esempio seguente illustra come aggiungere una casella di controllo a un foglio grafico.

L'immagine seguente mostra il foglio di lavoro del grafico con la casella di controllo nel file di output.

![todo:image_alt_text](controls-in-charts_1.jpg)

Il [file di output](101089316.xlsx) generato dal frammento di codice seguente è allegato per il tuo riferimento.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **Argomenti avanzati**
- [Aggiungi WordArt Watermark al grafico](/cells/it/nodejs-cpp/add-wordart-watermark-to-chart/)

{{< app/cells/assistant language="nodejs-cpp" >}}
