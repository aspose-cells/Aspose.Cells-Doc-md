---
title: Hur man kontrollerar fryst tillstånd utan Excel med Node.js via C++
linktitle: Fruset tillstånd
type: docs
weight: 190
url: /sv/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: I denna artikel kommer du att lära dig hur man programatiskt kontrollerar det frysta tillståndet för ett Excel ark med Node.js och C++ bibliotek.

---

## **Introduktion**

I denna artikel kommer vi att lära oss hur man programatiskt kontrollerar det frysta tillståndet för ett Excel-ark. Vi kan enkelt avgöra om arbetsbladet är fryst eller delat i MS Excel. Men finns det ett sätt att ta reda på om det är fryst eller delat med Node.js? Vi kan enkelt göra det med Aspose.Cells for Node.js via C++.

## **Är fönsterfönster frysta**
Med Aspose.Cells for Node.js via C++ kan vi kontrollera om fönstret är fryst och hur många rader och kolumner som är låsta.

Använd [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) egenskapen för att kontrollera fönsterpanar och få låsta rader och kolumner med [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--) metoden.
1. Konstruera Arbetsbok för att öppna filen.
2. Kontrollera om arbetsbladet är fruset.
3. Hämta de låsta raderna och kolumnerna.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
