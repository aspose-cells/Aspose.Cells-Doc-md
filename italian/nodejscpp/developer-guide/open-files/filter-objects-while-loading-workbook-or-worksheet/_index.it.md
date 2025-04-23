---
title: Filtra Oggetti durante il caricamento di Workbook o Foglio di lavoro con Node.js tramite C++
linktitle: Filtra gli Oggetti durante il caricamento del Workbook o del Foglio di Lavoro
type: docs
weight: 330
url: /it/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Impara come filtrare i dati durante il caricamento di workbooks o fogli di lavoro usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**
Si usi la proprietà [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) mentre si filtrano dati dal workbook. Se si desidera filtrare i dati da fogli di lavoro individuali, sarà necessario sovrascrivere il metodo [LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-). Si fornisca il valore appropriato dall’enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) durante la creazione o l’utilizzo di [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter).

L’enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) ha i seguenti valori possibili.

- Tutti
- Impostazioni del libro
- Cellavuota
- Cella booleana
- Dati cella
- Errore cella
- Numerico cella
- Stringa cella
- Valore cella
- Chart
- Formattazione condizionale
- Convalida dati
- Nomi definiti
- Proprietà documento
- Formula
- Collegamenti ipertestuali
- Area unita
- Tabella pivot
- Impostazioni
- Forma
- Dati del Foglio
- Impostazioni del Foglio
- Struttura
- Stile
- Tabella
- VBA
- XmlMap

## **Filtra oggetti durante il caricamento della cartella di lavoro**
Il codice di esempio seguente illustra come filtrare i grafici dalla cartella di lavoro. Si prega di controllare il [file excel di esempio](5115258.xlsx) utilizzato in questo codice e il [PDF di output](5115257.pdf) generato da esso. Come si può vedere nel PDF di output, tutti i grafici sono stati filtrati fuori dalla cartella di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **Filtra oggetti durante il caricamento del foglio di lavoro**
Il codice di esempio seguente carica il [file Excel di origine](5115255.xlsx) e filtra i seguenti dati dai suoi fogli di lavoro utilizzando un filtro personalizzato.

- Filtra i Grafici dalla cartella di lavoro denominata NoCharts.
- Filtra le Forme dalla cartella di lavoro denominata NoShapes.
- Filtra la formattazione condizionale dalla cartella di lavoro denominata NoConditionalFormatting.

Una volta caricato il [file Excel di origine](5115255.xlsx) con un filtro personalizzato, si prendono le immagini di tutti i fogli di lavoro uno per uno. Ecco le immagini di output per il riferimento. Come si può vedere, la prima immagine non contiene grafici, la seconda immagine non ha forme e la terza immagine non ha formattazione condizionale.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

Così si utilizza la classe CustomLoadFilter come per i nomi dei fogli di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
