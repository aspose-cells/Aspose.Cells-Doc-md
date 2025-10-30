---
title: Formeln automatisch in Tabellen oder Listenobjekten propagieren, während Sie in neuen Zeilen Daten eingeben, mit Node.js über C++
linktitle: Tabellenformel festlegen
type: docs
weight: 260
url: /de/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Lernen Sie, wie Sie Formeln in Tabellen oder Listenobjekten automatisch propagieren, während Sie Daten in neuen Zeilen mit Aspose.Cells for Node.js via C++ eingeben.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass eine Formel in Ihrer Tabelle oder Listenobjekt automatisch auf neue Zeilen übertragen wird, während Sie neue Daten eingeben. Dies ist das Standardverhalten von Microsoft Excel. Um die gleiche Funktionalität mit Aspose.Cells for Node.js via C++ zu erreichen, verwenden Sie bitte [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--) Eigenschaften.

## **Formel automatisch in Tabelle oder Listenobjekt propagieren, während Sie Daten in neuen Zeilen eingeben**
Der folgende Beispielcode erstellt eine Tabelle oder Listenobjekt so, dass die Formel in Spalte B automatisch auf neue Zeilen übertragen wird, wenn Sie neue Daten eingeben. Bitte überprüfen Sie die [Ausgabedatei] (5115469.xlsx), die mit diesem Code generiert wurde. Wenn Sie eine beliebige Zahl in Zelle A3 eingeben, werden Sie sehen, dass die Formel in Zelle B2 automatisch nach B3 propagiert wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
