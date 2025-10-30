---
title: Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016 con Node.js via C++
description: Questo articolo introduce come usare la libreria Aspose.Cells per calcolare le funzioni MINIFS e MAXIFS in Microsoft Excel 2016 usando Node.js via C++. Carica un file Excel esistente o creane uno nuovo, poi usa i metodi di Aspose.Cells per calcolare queste funzioni e salva i risultati su disco.
keywords: Aspose.Cells, Excel, 2016, funzione MINIFS, funzione MAXIFS, calcolo Node.js via C++
type: docs
weight: 300
url: /it/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Possibili Scenari di Utilizzo**
Microsoft Excel 2016 supporta le funzioni MINIFS e MAXIFS. Queste funzioni non sono supportate in Excel 2013 o versioni precedenti. Aspose.Cells for Node.js via C++ supporta anche il calcolo di queste funzioni. Lo screenshot seguente illustra l'uso di queste funzioni. Leggi i commenti rossi all’interno dello screenshot per capire come funzionano queste funzioni.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016**
Il codice di esempio seguente carica il [file excel esempio](5115149.xlsx) e chiama il metodo [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) per eseguire il calcolo delle formule usando Aspose.Cells for Node.js via C++, e poi salva i risultati in un [file PDF di output](5115154.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
