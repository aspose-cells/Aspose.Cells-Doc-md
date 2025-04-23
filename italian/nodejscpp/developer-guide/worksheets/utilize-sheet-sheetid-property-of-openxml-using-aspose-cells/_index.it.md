---
title: Utilizza la proprietà Sheet.SheetId di OpenXml usando Aspose.Cells for Node.js via C++
linktitle: Utilizzare la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells
type: docs
weight: 200
url: /it/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Questo articolo dimostra come utilizzare la proprietà Sheet.SheetId di OpenXml tramite manipolazione delle funzioni di Excel con Aspose.Cells for Node.js via C++ in modo programmatico.
keywords: proprietà sheet id di openxml node.js tramite C++, sheet id di excel worksheet node.js tramite C++
---

## **Possibili Scenari di Utilizzo**

La proprietà *Sheet.SheetId* è disponibile all’interno del modulo *DocumentFormat.OpenXml.Spreadsheet* ed è parte di OpenXml. Puoi vedere questa proprietà e il suo valore all’interno di *workbook.xml* come mostrato nello screenshot seguente. Aspose.Cells fornisce la proprietà equivalente come [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilizza la proprietà Sheet.SheetId di OpenXml usando Aspose.Cells for Node.js via C++**

Il codice di esempio seguente carica il [file Excel di esempio](51740716.xlsx), legge il suo ID della scheda o tabulato, quindi ne assegna un nuovo ID della scheda e lo salva come [file Excel di output](51740717.xlsx). Si prega di vedere anche l'output della console del codice sottostante per un riferimento.

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **Output della console**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
