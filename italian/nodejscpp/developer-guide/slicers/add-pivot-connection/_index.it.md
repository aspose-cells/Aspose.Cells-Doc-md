---
title: Aggiungi connessione pivot con Node.js tramite C++
linktitle: Aggiungi connessione pivot
type: docs
weight: 30
url: /it/nodejs-cpp/add-pivot-connection/
description: Impara come aggiungere una connessione pivot usando Aspose.Cells for Node.js via C++.
keywords: Aggiungi connessione pivot senza office 2013, office 2016, office 2019 e office 365 Node.js tramite C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi associare uno slicer e una tabella pivot in Excel, fai clic destro sullo slicer e seleziona "Connessioni rapporti...". Nell'elenco delle opzioni, puoi operare sulla casella di controllo. Se invece vuoi associare uno slicer e una tabella pivot usando ASPose.Cells API programmando, usa il metodo [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-). Il metodo assocerà lo slicer e la tabella pivot.

## **Associa Slicer e Tabella pivot**

Il seguente esempio carica il [file Excel di esempio](add-pivot-connection.xlsx) che contiene uno slicer esistente. Accede allo slicer e poi associa lo slicer e la tabella pivot. Infine, salva il file come [file Excel di output](add-pivot-connection-out.xlsx).

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
