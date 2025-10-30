---
title: Filtro Nomi definiti durante il caricamento di Workbook con Node.js tramite C++
linktitle: Filtra i Nomi Definiti durante il caricamento del Workbook
type: docs
weight: 50
url: /it/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells consente di filtrare o rimuovere i nomi definiti presenti all’interno del workbook. Si usi [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) per caricare i nomi definiti e [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) per rimuoverli durante il caricamento del workbook. Si noti che, se si rimuovono i nomi definiti, le formule all’interno del workbook potrebbero non funzionare più correttamente.

## **Filtra i nomi definiti durante il caricamento del foglio di lavoro**

Il seguente esempio carica il file Excel di esempio](61767860.xlsx) che contiene una formula nella cella **C1** con i nomi definiti, cioè *SUM(MyName1, MyName2)*. Dato che usiamo [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) per rimuovere i nomi definiti durante il caricamento del workbook, la formula nella cella C1 nel [file Excel di output](61767861.xlsx) si interrompe e visualizza *#NAME?*. Si veda il seguente screenshot che mostra l’effetto del codice sul file Excel di esempio.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
