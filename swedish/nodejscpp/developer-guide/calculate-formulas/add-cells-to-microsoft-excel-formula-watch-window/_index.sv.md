---
title: Lägg till celler till Microsoft Excel formelövervakningsfönster med Node.js via C++
linktitle: Lägg till celler i Microsoft Excel Formelövervakningsfönstret
description: Hur man använder Aspose.Cells biblioteket för att lägga till celler till formelövervakningsfönstret i Excel med Node.js via C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi manipulera cellerna i den och ställa in formler. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, Formelfönster, Celler, Tillägg, Node.js via C++
type: docs
weight: 60
url: /sv/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Möjliga användningsscenario**

Microsoft Excel Watch Window är ett användbart verktyg för att enkelt övervaka cellvärden och dess formler i ett fönster. Du kan öppna *Watch Window* med Microsoft Excel genom att klicka på *Formulas > Watch* *Window*. Det har knappen *Add Watch* som kan användas för att lägga till celler för inspektion. På liknande sätt kan du använda [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-)-metoden för att lägga till celler i *Watch Window* med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande exempel kod ställer in formeln för cellerna C1 och E1 och lägger till båda till Watch Window. Den sparar sedan arbetsboken som [utdata Excel-fil](67338481.xlsx). Om du öppnar den utdata Excel-filen och tittar i *Watch Window* kommer du att se båda cellerna som visas i denna skärmdump.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
