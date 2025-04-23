---
title: Come controllare la visualizzazione del workbook con Node.js tramite C++
linktitle: Come controllare la visualizzazione del workbook
type: docs
weight: 600
url: /it/nodejs-cpp/how-to-control-workbook-view/
description: Impara come controllare la visualizzazione del Workbook tramite l’API Aspose.Cells for Node.js via C++.
keywords: Come controllare la visualizzazione del Workbook con Node.js tramite C++, impostare la visualizzazione di Excel con Node.js tramite C++, gestire la visualizzazione del Workbook con Node.js tramite C++, impostare la visualizzazione del Workbook con Node.js tramite C++, controllare la visualizzazione di Excel con Node.js tramite C++.
---

## **Possibili Scenari di Utilizzo**
Quando hai bisogno di regolare la visualizzazione delle pagine di Excel, devi sapere come controllare ogni modulo, come le barre di scorrimento orizzontali e verticali, se nascondere i file Excel aperti, e così via. Aspose.Cells for Node.js via C++ offre questa funzione. Aspose.Cells for Node.js via C++ fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **Come controllare la visualizzazione del Workbook usando Aspose.Cells for Node.js via C++**
Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Nascondere le barre di scorrimento orizzontali e verticali della visualizzazione del workbook.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating an Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

cell = cells.get("E10");
const temp = workbook.createStyle();
temp.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(temp);

// Hide horizontal and vertical scrollbars
workbook.getSettings().setIsHScrollBarVisible(false);
workbook.getSettings().setIsVScrollBarVisible(false);

workbook.save("out.xlsx");
```

Anteprima del file di risultato:
<br>
<image src="result.png" width="70%" />

