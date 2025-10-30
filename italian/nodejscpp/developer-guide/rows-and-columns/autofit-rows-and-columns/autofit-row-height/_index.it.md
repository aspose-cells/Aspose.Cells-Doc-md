---
title: Auto adatta l’altezza della riga automaticamente durante il caricamento del file con Node.js tramite C++
linktitle: Adattamento automatico dell altezza della riga in modo automatico durante il caricamento del file
type: docs
weight: 120
url: /it/nodejs-cpp/autofit-row-height/
description: Scopri come adattare automaticamente le righe la cui altezza non è personalizzata quando si carica un file usando Aspose.Cells for Node.js via C++.
keywords: Auto adatta l’altezza della riga durante il caricamento del file con Node.js tramite C++, regola automaticamente l’altezza della riga all’apertura del file Excel con Node.js tramite C++ 
---

## **Possibili Scenari di Utilizzo**
L’altezza della riga si adatta automaticamente al font del contenuto, ma quando l’altezza della riga memorizzata non corrisponde all’altezza del contenuto nel file, MS Excel regola automaticamente l’altezza della riga durante il caricamento del file, mentre Aspose.Cells for Node.js via C++ non lo farà automaticamente per migliorare le prestazioni. Se desideri usare il programma Aspose.Cells per adattare automaticamente le altezze delle righe durante il caricamento dei file, puoi raggiungerlo tramite il parametro [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) nel tuo codice.

Puoi fare riferimento ai seguenti dati immagine. Possiamo osservare che l’altezza della riga memorizzata alla linea 11 è 15, ma Excel ha regolato automaticamente l’altezza della riga durante il caricamento del file.
<br>
<img src="1.png" width=70% />

## **Regola l’altezza della riga usando Aspose.Cells for Node.js via C++**
Se carichi direttamente il file e lo salvi in PDF, i dati non saranno completamente visualizzati in PDF perché la sua altezza della linea memorizzata è di soli 15.
<br>
<img src="2.png" width=70% />
<br>
Se imposti il parametro [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) su true quando carichi il file, allora Aspose.Cells regolerà automaticamente l’altezza delle righe. L’altezza della riga regolata può soddisfare efficacemente i requisiti di visualizzazione del testo.
<br>
<img src="3.png" width=70% />

## **Codice di esempio Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
