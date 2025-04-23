---
title: Dividi schermo del foglio Excel con Node.js tramite C++
linktitle: Schermata divisa
type: docs
weight: 190
url: /it/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: In questo articolo, imparerai come visualizzare alcune righe e/o colonne in pannelli separati dividendo il foglio in due o quattro parti programmaticamente usando l Addon Node.js C++.
keywords: Congela le righe superiori, Congela la prima riga.
---

## **Introduzione**

In questo articolo, impareremo come visualizzare alcune righe e/o colonne in pannelli separati dividendo il foglio di lavoro in due o quattro parti. Quando si lavora con grandi set di dati, è necessario vedere alcune aree del stesso foglio contemporaneamente per confrontare diverse sottosezioni di dati. La funzione di divisione dello schermo può soddisfare le tue esigenze.

## **Come dividere lo schermo in Excel**
Per suddividere un foglio di lavoro in due o quattro parti, procedi come segue:

1. Seleziona la riga/colonna/cella prima della quale desideri posizionare la suddivisione.
2. Sulla scheda Visualizza, nel gruppo Finestre, fai clic sul pulsante Suddivisione.

**![Schermata divisa](Split-Screen.png)**

## **Suddividi il foglio di lavoro verticalmente sulle colonne**

Per separare due aree del foglio di calcolo verticalmente, seleziona la colonna a destra della colonna in cui desideri che appaia la suddivisione e fai clic sul pulsante Suddivisione in Excel.

 È facile dividere verticalmente un foglio di lavoro in colonne programmaticamente con Aspose.Cells for Node.js via C++, basta selezionare una cella nella riga superiore come cella attiva, quindi dividere con [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) metodo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Suddividi il foglio di lavoro orizzontalmente sulle righe**
Per separare la finestra di Excel orizzontalmente, seleziona la riga sotto la riga in cui desideri che avvenga la suddivisione in Excel.

 È facile dividere orizzontalmente un foglio di lavoro in righe programmaticamente con Aspose.Cells for Node.js via C++, basta selezionare una cella nella colonna a sinistra come cella attiva, quindi dividere con [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) metodo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Dividi il foglio di lavoro in quattro parti.**
Per visualizzare contemporaneamente quattro diverse sezioni dello stesso foglio di lavoro, dividi lo schermo sia verticalmente che orizzontalmente in Excel.

 È facile dividere verticalmente un foglio di lavoro in colonne programmaticamente con Aspose.Cells for Node.js via C++, basta selezionare una cella diversa dalla prima riga e colonna come cella attiva, quindi dividere con [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) metodo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **Come rimuovere la divisione**
Per rimuovere la divisione del foglio di lavoro, basta fare clic sul pulsante Dividi di nuovo.

Aspose.Cells for Node.js via C++ fornisce un metodo [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) per rimuovere le impostazioni di divisione.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

