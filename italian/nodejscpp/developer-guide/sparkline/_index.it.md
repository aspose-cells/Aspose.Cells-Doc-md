---
title: Inserisci Sparkline con Node.js tramite C++
linktitle: Sparklines
type: docs
weight: 160
url: /it/nodejs-cpp/creating-sparklines/
description: Crea uno sparkline per Excel usando Aspose.Cells for Node.js via C++.
---

## **Inserisci una sparkline**
{{% alert color="primary" %}} 

Lo Sparkline è un piccolo grafico in una cella del foglio di lavoro che fornisce una rappresentazione visiva dei dati. Usa gli sparklines per mostrare le tendenze in una serie di valori, come aumenti o diminuzioni stagionali, cicli economici o per evidenziare valori massimi e minimi. Posiziona uno sparkline vicino ai suoi dati per un impatto maggiore. Esistono tre tipi di Sparkline: Linea, Colonna e Impilato.

{{% /alert %}} 

È semplice creare uno sparkline con Aspose.Cells for Node.js via C++ seguendo i codici di esempio:



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

## **Argomenti avanzati**
- [Utilizzo di Sparklines e Impostazioni 3D Formato](/cells/it/nodejs-cpp/using-sparklines-and-settings-3d-format/)
