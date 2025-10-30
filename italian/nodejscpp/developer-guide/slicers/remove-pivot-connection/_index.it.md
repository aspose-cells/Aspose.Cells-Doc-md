---
title: Rimuovi Connessione Pivot con Node.js tramite C++
linktitle: Rimuovere la connessione pivot
type: docs
weight: 30
url: /it/nodejs-cpp/remove-pivot-connection/
description: Impara come rimuovere la connessione pivot usando Aspose.Cells for Node.js via C++.
keywords: Rimuovi connessione pivot senza office 2013, office 2016, office 2019 e office 365 Node.js tramite C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi disassociare uno slicer e una tabella pivot in Excel, devi fare clic con il tasto destro sullo slicer e selezionare l'elemento "Connessioni rapporto...". Nell'elenco delle opzioni, puoi operare sulla casella di controllo. In modo simile, se desideri disassociare uno slicer e una tabella pivot utilizzando l'API Aspose.Cells programmativamente, utilizza il metodo [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-). Disassocerà lo slicer e la tabella pivot.

## **Dissociare lo slicer e la tabella pivot**

Il seguente esempio di codice carica il [file Excel di esempio](remove-pivot-connection.xlsx) che contiene uno slicer esistente. Accede agli slicer e poi disassociano lo slicer e la tabella pivot. Infine, salva il workbook come [file Excel di output](remove-pivot-connection-out.xlsx).

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
