---
title: Propagera formel automatiskt i tabell eller listobjekt när du matar in data i nya rader med Node.js via C++
linktitle: Ställer in tabellformel
type: docs
weight: 260
url: /sv/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Lär dig hur du automatiskt sprider formler i tabeller eller listobjekt när du matar in data i nya rader med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**
Ibland vill du att en formel i din tabell eller listobjekt ska automatiskt spridas till nya rader när du matar in ny data. Detta är standardbeteendet i Microsoft Excel. För att uppnå samma funktionalitet med Aspose.Cells for Node.js via C++, använd [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--) egenskapen.

## **Sprid formel automatiskt i tabell eller listobjekt medan du matar in data i nya rader**
Följande exempel på kod skapar en tabell eller listobjekt så att formeln i kolumn B automatiskt sprids till nya rader när du matar in ny data. Kontrollera den [utdataexcel-fil](5115469.xlsx) som genereras med denna kod. Om du skriver in ett tal i cell A3, kommer du att se att formeln i cell B2 automatiskt sprids till cell B3.

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
