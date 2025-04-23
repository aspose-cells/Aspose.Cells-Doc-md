---
title: Einen Sparkline mit Node.js über C++ einfügen
linktitle: Sparklines
type: docs
weight: 160
url: /de/nodejs-cpp/creating-sparklines/
description: Erstellen Sie eine Sparkline für Excel mit Aspose.Cells for Node.js via C++.
---

## **Eine Sparkline einfügen**
{{% alert color="primary" %}} 

Sparkline ist ein kleines Diagramm in einer Zelle eines Arbeitsblatts, das eine visuelle Darstellung der Daten bietet. Verwenden Sie Sparklines, um Trends in einer Wertefolge anzuzeigen, wie saisonale Zunahmen oder Rückgänge, Wirtschaftszyklen oder um Maximal- und Minimalwerte hervorzuheben. Platzieren Sie eine Sparkline in der Nähe ihrer Daten für maximale Wirkung. Es gibt drei Arten von Sparkline: Linie, Säule und Gestapelt.

{{% /alert %}} 

Es ist einfach, eine Sparkline mit Aspose.Cells for Node.js via C++ mit den folgenden Beispielcodes zu erstellen:



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

## **Erweiterte Themen**
- [Verwenden von Sparklines und Einstellungen 3D-Format](/cells/de/nodejs-cpp/using-sparklines-and-settings-3d-format/)
