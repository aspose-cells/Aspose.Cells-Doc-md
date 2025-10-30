---
title: Objekte filtern beim Laden der Arbeitsmappe oder des Arbeitsblatts mit Node.js über C++
linktitle: Filterobjekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 330
url: /de/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Erfahren Sie, wie Sie beim Laden von Arbeitsmappen oder Arbeitsblättern mit Aspose.Cells for Node.js via C++ Daten filtern.
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie die Eigenschaft [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) beim Filtern von Daten aus der Arbeitsmappe. Wenn Sie jedoch Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie die Methode [LoadFilter.startSheet(Worksheet)] überschreiben. Bitte geben Sie beim Erstellen oder Arbeiten mit [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) den entsprechenden Wert aus der Aufzählung [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) an.

Die Aufzählung [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) hat die folgenden möglichen Werte.

- Alle
- Bucheinstellungen
- Zelle Leer
- Zelle Bool
- Zelldaten
- Zellenfehler
- Zellnumerisch
- Zellenzeichenfolge
- Zellwert
- Chart
- Bedingte Formatierung
- Datenvalidierung
- Definierte Namen
- Dokumenteigenschaften
- Formel
- Hyperlinks
- Zusammengeführter Bereich
- Pivot-Tabelle
- Einstellungen
- Form
- Tabellendaten
- Tabelleneinstellungen
- Struktur
- Stil
- Tabelle
- VBA
- XmlMap

## **Filterobjekte beim Laden der Arbeitsmappe**
Der folgende Beispielcode veranschaulicht, wie Diagramme aus der Arbeitsmappe gefiltert werden. Bitte überprüfen Sie die [Beispiel-Excel-Datei](5115258.xlsx), die in diesem Code verwendet wird, und das [Ausgabe-PDF](5115257.pdf), das von ihm generiert wurde. Wie Sie im Ausgabe-PDF sehen können, wurden alle Diagramme aus der Arbeitsmappe gefiltert.

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

## **Filterobjekte beim Laden des Arbeitsblatts**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115255.xlsx) und filtert die folgenden Daten aus ihren Arbeitsblättern mithilfe eines benutzerdefinierten Filters.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert bedingte Formatierungen aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

Sobald es die [Quell-Excel-Datei](5115255.xlsx) mit einem benutzerdefinierten Filter lädt, nimmt es die Bilder aller Arbeitsblätter nacheinander. Hier sind die Ausgabe-Bilder zur Referenz. Wie Sie sehen können, hat das erste Bild keine Diagramme, das zweite Bild hat keine Formen und das dritte Bild hat keine bedingte Formatierung.

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

So verwenden Sie die Klasse CustomLoadFilter gemäß der Arbeitsblattnamen.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
