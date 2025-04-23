---
title: Infoga Sparkline med Node.js via C++
linktitle: Sparklines
type: docs
weight: 160
url: /sv/nodejs-cpp/creating-sparklines/
description: Skapa sparkline för Excel med Aspose.Cells for Node.js via C++.
---

## **Infoga en sparkline**
{{% alert color="primary" %}} 

Sparkline är en liten diagram i en arbetsbladscell som ger en visuell presentation av data. Använd sparklines för att visa trender i en serie värden, som säsongsandelar eller -minskningar, ekonomiska cykler eller för att lyfta fram maximala och minimala värden. Placera en sparkline nära dess data för största effekt. Det finns tre typer av Sparkline: Linje, Kolumn och Staplad.

{{% /alert %}} 

Det är enkelt att skapa en sparkline med Aspose.Cells for Node.js via C++ med följande exempelkod:



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **Fortsatta ämnen**
- [Använda funktionsspår och inställningar 3D-format](/cells/sv/nodejs-cpp/using-sparklines-and-settings-3d-format/)
