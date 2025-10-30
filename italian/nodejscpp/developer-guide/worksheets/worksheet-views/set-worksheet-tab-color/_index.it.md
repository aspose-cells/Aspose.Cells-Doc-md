---  
title: Imposta il colore della scheda del foglio di lavoro con Node.js tramite C++  
linktitle: Impostare il Colore della Scheda del Foglio di Lavoro  
type: docs  
weight: 120  
url: /it/nodejs-cpp/set-worksheet-tab-color/  
description: Questo articolo dimostra un esempio di codice che imposta il colore della scheda del foglio Excel programmaticamente usando Node.js tramite C++.  
keywords: imposta il colore della scheda Excel Node.js tramite C++, codice per impostare il colore della scheda Excel Node.js tramite C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells consente di cambiare il colore delle singole schede del foglio di lavoro per renderle evidenti rispetto alle altre. Ad esempio, è possibile rendere Rosso le Spese, Verde le Vendite, Blu i Beni, ecc.

{{% /alert %}}  
## **Impostare il Colore della Scheda del Foglio di Lavoro con Microsoft Excel**  
1. Fare clic con il pulsante destro del mouse su una scheda nell'insieme di schede nella parte inferiore della scheda corrente.  
1. Seleziona **Colore scheda**.  
1. Seleziona un colore dalla tavolozza.  
1. Fai clic su **OK**.  
## **Impostazione colore scheda foglio di calcolo con Aspose.Cells**  
Il codice di esempio di seguito mostra come impostare il colore della scheda con Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
