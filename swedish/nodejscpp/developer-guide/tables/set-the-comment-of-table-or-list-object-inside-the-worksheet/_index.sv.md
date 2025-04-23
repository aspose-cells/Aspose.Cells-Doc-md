---
title: Ställ in kommentaren för tabell eller lista objekt i arbetsbladet med Node.js via C++
linktitle: Ange kommentaren för tabellen eller lista objektet i arbetsbladet
type: docs
weight: 40
url: /sv/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Lär dig hur du ställer in kommentaren för tabell eller lista objekt i arbetsbladset med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Du kan ställa in kommentaren för tabell eller lista objekt inuti arbetsbladet med hjälp av [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--)-egenskapen. Kommentaren kommer att vara synlig inuti filen xl/tables/tableName.xml.

{{% /alert %}}

## **Ange kommentaren för tabell eller listobjekt inne i kalkylbladet**

Följande kodexempel laddar [käll-exkelfilen](5115514.xlsx), anger kommentaren för den första tabellen eller listobjektet i arbetsbladet.

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
