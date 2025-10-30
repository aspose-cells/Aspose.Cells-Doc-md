---  
title: Disegnare Timeline durante il rendering di Excel in PDF con Node.js via C++  
linktitle: Disegna la Timeline durante la rappresentazione di Excel in PDF  
type: docs  
weight: 60  
url: /it/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Gestire le timeline dei file Excel con Aspose.Cells for Node.js via C++.  
keywords: Render della timeline in PDF senza Office 2013, Office 2016, Office 2019 e Office 365 Node.js via C++  
---  

## **Disegna la Timeline durante la rappresentazione di Excel in PDF**  
Se hai un file Excel a cui è applicata una timeline e desideri esportare l'Excel in PDF con le impostazioni della timeline, Aspose.Cells for Node.js via C++ supporta questa funzionalità di default. Basta esportare il file Excel con timeline in PDF, e il PDF generato mostrerà la timeline applicata.  

Il seguente codice di esempio carica il [file di Excel di esempio](input.xlsx) che contiene un timeline esistente. Salva poi il workbook come [file PDF di output](out.pdf). La seguente schermata confronta il file di Excel di origine e il file PDF generato.  

<img src="out.png" width="60%">  

## **Codice di Esempio**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
