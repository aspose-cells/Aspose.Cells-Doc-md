---
title: Trova se il Foglio di Lavoro è un Foglio di Dialogo con Node.js tramite C++
linktitle: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 90
url: /it/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Questo articolo fornisce istruzioni e codice di esempio per determinare programmaticamente se un foglio di Excel è un Foglio di Dialogo utilizzando Aspose.Cells for Node.js via C++.
keywords: trova il tipo di dialogo del foglio di lavoro excel con Node.js tramite C++, dialogo foglio di lavoro Node.js tramite C++
---

## **Possibili Scenari di Utilizzo**

Il Foglio di Dialogo è un vecchio formato di foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere stato inserito da una versione più vecchia di Microsoft Excel ad esempio 2003, come mostrato in questa schermata. Può anche essere inserito con VBA in versioni più recenti ad esempio Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puoi verificare se il foglio è un foglio di dialogo o un altro tipo di foglio con la proprietà [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) fornita da Aspose.Cells for Node.js via C++. Se restituisce il valore dell’enumerazione [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), allora significa che stai gestendo un foglio di dialogo.

## **Trova se il foglio di lavoro è un foglio di dialogo**

Il codice di esempio seguente carica il [file Excel di esempio](64716820.xlsx) che contiene un foglio di dialogo. Controlla la proprietà [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), la confronta con [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) e quindi stampa il messaggio. Per favore, guarda l’output della console del codice di esempio di seguito per ulteriori informazioni.

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Output della console**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
