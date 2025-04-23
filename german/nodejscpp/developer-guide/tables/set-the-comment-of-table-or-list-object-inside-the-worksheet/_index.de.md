---
title: Kommentar der Tabelle oder des Listenobjekts innerhalb des Arbeitsblatts in Node.js via C++ setzen
linktitle: Setzen des Kommentars für Tabelle oder Listenobjekt in einem Arbeitsblatt
type: docs
weight: 40
url: /de/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Lernen Sie, wie Sie das Kommentar der Tabelle oder des Listenobjekts im Arbeitsblatt mit Aspose.Cells for Node.js via C++ setzen. 
---

{{% alert color="primary" %}}

 Sie können das Kommentar des Tabellen- oder Listenobjekts im Arbeitsblatt mit der [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--)-Eigenschaft setzen. Das Kommentar ist in der Datei xl/tables/tableName.xml sichtbar.

{{% /alert %}}

## **Den Kommentar der Tabelle oder des Listenobjekts innerhalb des Arbeitsblatts festlegen**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115514.xlsx) und setzt den Kommentar für die erste Tabelle oder das erste Listenobjekt im Arbeitsblatt.

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
