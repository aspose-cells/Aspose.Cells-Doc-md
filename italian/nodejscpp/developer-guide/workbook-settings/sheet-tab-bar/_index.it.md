---  
title: Come controllare la barra delle schede del foglio con Node.js tramite C++  
linktitle: Come controllare la barra delle schede del foglio  
type: docs  
weight: 600  
url: /it/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Impara come controllare la barra delle schede del foglio usando Aspose.Cells for Node.js via C++.  
keywords: Come controllare la barra delle schede del foglio con Node.js tramite C++, Gestire la barra delle schede del foglio con Node.js tramite C++, Impostare la barra delle schede del foglio con Node.js tramite C++, Controllare la barra delle schede del foglio con Node.js tramite C++.  
---  

## **Possibili Scenari di Utilizzo**  
Quando hai bisogno di regolare la visualizzazione della barra del foglio Excel, devi sapere come controllare la barra delle schede del foglio, come nasconderla o mostrarla, cambiare la larghezza della barra delle schede, specificare la prima scheda visibile, e così via. Aspose.Cells for Node.js via C++ supporta queste funzionalità. Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Come controllare la barra delle schede del foglio usando Aspose.Cells for Node.js via C++**  
Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Visualizzare la scheda del foglio e impostare la larghezza della barra delle schede.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Anteprima del file di risultato:  
<br>  
<image src="result.png" width="70%" />  


{{< app/cells/assistant language="nodejs-cpp" >}}
