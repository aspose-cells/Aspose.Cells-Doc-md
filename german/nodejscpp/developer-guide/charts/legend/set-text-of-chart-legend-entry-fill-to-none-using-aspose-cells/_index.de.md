---
title: Setzen Sie den Text des Legendeneintrags des Charts auf keine Füllung mit Aspose.Cells for Node.js via C++
linktitle: Legenden Eintragsfüllung des Diagramms auf keinen Text setzen mit Aspose.Cells
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ die Füllfarbe des Legendeneintrags auf keine setzen. Dieser Leitfaden zeigt, wie Sie die Füllfarbe von Legendeneinträgen in Microsoft Excel Diagrammen für eine bessere Visualisierung und Anpassung ändern.
keywords: Aspose.Cells for Node.js via C++, Diagramm Legendeneintragsfüllung, Microsoft Excel, Visualisierung, Anpassung.
type: docs
weight: 320
url: /de/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Wenn Sie die Füllfarbe des Legendeneintrags des Diagramms auf keine setzen möchten, damit sie nicht im Diagramm-Legendenbereich angezeigt wird, setzen Sie [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) auf **true**.

{{% /alert %}}

Der folgende Beispielcode setzt den Text der zweiten Diagrammlegendeneintragsfüllung auf keine. Laden Sie bitte die [Beispieldatei Excel](5115219.xlsx) herunter, die in diesem Code verwendet wird, und die [Ausgabedatei Excel](5115217.xlsx), die von ihr generiert wird, zur Referenz.

Das folgende Screenshot hebt die Wirkung dieses Codes auf die [Beispieldatei Excel](5115219.xlsx) hervor.

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
