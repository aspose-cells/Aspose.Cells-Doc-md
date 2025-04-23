---
title: Imposta il Commento della Tabella o Oggetto Lista all’interno del Foglio di lavoro con Node.js tramite C++
linktitle: Imposta il Commento dell oggetto Tabella o Lista all interno del Foglio di Lavoro
type: docs
weight: 40
url: /it/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Impara come impostare il commento della tabella o oggetto lista all’interno del foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puoi impostare il commento della Tabella o Oggetto Lista all’interno del foglio di lavoro usando la proprietà [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--). Il commento sarà visibile all’interno del file xl/tables/tableName.xml.

{{% /alert %}}

## **Imposta il commento della tabella o dell'oggetto lista all'interno del foglio di lavoro**

Il seguente codice di esempio carica il [file di origine excel](5115514.xlsx), imposta il commento della prima tabella o primo oggetto elenco all'interno del foglio di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "table_comment.xlsx"));
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access first list object or table.
const lstObj = worksheet.getListObjects().get(0);
// Set the comment of the list object
lstObj.setComment("This is Aspose.Cells comment.");
// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "SetCommentOfTableOrListObject_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
