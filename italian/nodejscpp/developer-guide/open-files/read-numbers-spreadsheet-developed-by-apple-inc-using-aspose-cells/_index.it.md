---
title: Leggi Foglio di Calcolo Numbers sviluppato da Apple Inc. usando Aspose.Cells for Node.js via C++
linktitle: Leggi il foglio elettronico Numbers sviluppato da Apple Inc. utilizzando Aspose.Cells
type: docs
weight: 140
url: /it/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Impara come leggere i fogli di calcolo Numbers sviluppati da Apple Inc. usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Numbers è un'applicazione di fogli di calcolo sviluppata da Apple Inc. Aspose.Cells può leggere i fogli di calcolo Numbers, ma non supporta la scrittura su di essi. Può leggere i dati, lo stile e le formule dei fogli di calcolo Numbers.

## **Leggi Foglio di Calcolo Numbers sviluppato da Apple Inc. usando Aspose.Cells for Node.js via C++**

Il seguente esempio di codice carica l'[Esempio di Foglio di Calcolo Numbers](sampleNumbersByAppleInc.numbers) e lo converte in [Formato PDF di Output](outputNumbersByAppleInc.pdf). Dovrai utilizzare la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) e specificare [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) come parametro nel suo costruttore per caricarlo correttamente. Scarica entrambi dai link forniti. Puoi provare il codice con qualsiasi foglio di calcolo Numbers. Leggi anche i commenti del codice per ulteriori aiuti.

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

