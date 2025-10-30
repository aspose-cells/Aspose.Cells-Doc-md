---
title: Filtra il progetto VBA durante il caricamento di un file Excel con Node.js tramite C++
linktitle: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 140
url: /it/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Impara come filtrare i progetti VBA durante il caricamento di cartelle di lavoro Excel usando Aspose.Cells for Node.js via C++.
---

## **Filtra il progetto VBA durante il caricamento di una cartella di lavoro Excel in Node.js tramite C++**

Alcuni file .xlsm/.xslb hanno un numero estremamente elevato di macro (o macro molto lunghe). Aspose.Cells for Node.js via C++ caricherà indiscriminatamente questi dati (meta) quando apri tali cartelle di lavoro. Potresti dover controllare questo tramite [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) quando hai bisogno solo di estrarre i nomi dei fogli per un gran numero di cartelle di lavoro, saltando così contenuti non necessari. Questo filtro è fornito introducendo una nuova opzione, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).

## **Codice di Esempio**

Il seguente codice di esempio carica un documento di lavoro in modo che solo il VBA venga filtrato. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
