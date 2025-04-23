---  
title: So setzen Sie einen Punkt als Gesamtwert mit Node.js über C++  
linktitle: So setzen Sie einen Punkt als Gesamtwert  
description: Erfahren Sie, wie Sie Punkte in Wasserfall Diagrammen mithilfe von Aspose.Cells for Node.js via C++ auf den Gesamtwert setzen.  
keywords: Wasserfall Diagramm, Punkt, Als Gesamt setzen, Node.js über C++  
type: docs  
weight: 72  
url: /de/nodejs-cpp/how-to-set-point-as-total/  
---  

## Was bedeutet "Punkt als Gesamtwert setzen" in Excel-Diagrammen

In einigen Excel-Diagrammen, zum Beispiel Wasserfalldiagrammen, sind einige Punktdaten die Summe der vorherigen Punkte, und Sie müssen möglicherweise "Punkt als Gesamtwert setzen". Wir zeigen den Beispielcode und die Abbildung unten.

## Ein Wasserfall-Diagramm muss "Punkt als Gesamtwert setzen" 

![todo:image_alt_text](set-as-total1.png)

Dieses Bild zeigt ein Wasserfalldiagramm in Excel. Wir sehen, dass es vier Datenpunkte gibt, die mit "Total" beginnen, und sie dienen dazu, alle vorherigen Datenpunkte zu zählen. In diesem Bild sind die Einstellungen nicht ganz korrekt. Wenn wir den Punkt "Total 2024" auswählen, sehen wir, dass die Option "Als Gesamtwert setzen" in Excel nicht aktiviert ist. Im Anhang finden Sie die [Beispiel-Excel-Datei](SampleSheet.xlsx), die angepasst werden muss, und wir verwenden Aspose.Cells for Node.js via C++, um sie korrekt einzurichten.

## Verwendung von Aspose.Cells for Node.js via C++, um "Punkt als Gesamtwert zu setzen" 

Wir verwenden den folgenden Code, um die Datei richtig einzurichten:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Sie können die folgende korrekte [Ausgabedatei](output.xlsx) herunterladen

Wie im untenstehenden Bild gezeigt, sind die vier "Total"-Datenpunkte korrekt eingestellt, und Sie können den Unterschied zum vorherigen Diagramm erkennen.

![todo:image_alt_text](set-as-total2.png)  
