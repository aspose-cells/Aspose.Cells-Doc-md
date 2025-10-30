---
title: Impostare la larghezza della colonna su un unità scalabile come em o percentuale con Node.js tramite C++
linktitle: Impostare la larghezza della colonna su un unità scalabile come em o percentuale
type: docs
weight: 130
url: /it/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Impara come impostare la larghezza della colonna su unità scalabili come em o percentuale in Aspose.Cells for Node.js via C++. Migliora la presentazione delle tabelle HTML generate.
---

Generare un file HTML da un foglio di calcolo è molto comune. La dimensione delle colonne è definita in "pt," che funziona in molti casi. Tuttavia, potrebbe esserci un caso in cui questa dimensione fissa potrebbe non essere necessaria. Ad esempio, se la larghezza di un pannello contenitore è 600px, dove questa pagina HTML viene visualizzata, potresti ottenere una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. È stato richiesto che questa dimensione fissa venga cambiata in un'unità scalabile come em o percentuale per ottenere una presentazione migliore. Il codice di esempio seguente può essere usato dove [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) è impostato su **true** per creare larghezze scalabili.

I file di origine e i file di output di esempio possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
