---  
title: Sposta un intervallo di celle in un foglio di lavoro con Node.js tramite C++  
linktitle: Sposta intervallo di celle in un foglio di lavoro  
type: docs  
weight: 370  
url: /it/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Impara come spostare un intervallo di celle in un foglio di lavoro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Questo articolo mostra come spostare un intervallo di celle in un foglio di lavoro.  
{{% /alert %}}  

## **Sposta Intervallo di Celle in un Foglio di Lavoro**  
Il codice di esempio utilizza un file modello per dimostrare il compito.  

**Il file di input**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Si prega di vedere il file generato seguente con l'intervallo da A1:B5 spostato in C1:D5.  

**Il file di output  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

