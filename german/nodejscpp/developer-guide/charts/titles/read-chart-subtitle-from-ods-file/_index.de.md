---
title: Diagrammunterschrift aus ODS Datei mit Node.js über C++ lesen
linktitle: Lese Diagramm Untertitel aus ODS Datei
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ die Diagrammunterschrift aus einer OpenDocument Spreadsheet (ODS) Datei lesen. Unser Leitfaden zeigt, wie man die Unterschrift eines Diagramms extrahiert und darauf zugreift für weitere Analysen oder Anzeigen.
keywords: Aspose.Cells for Node.js via C++, Diagrammunterschrift lesen, OpenDocument Spreadsheet, ODS Datei, Diagrammextraktion, Datenanalyse
type: docs
weight: 160
url: /de/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **Diagramm-Untertitel aus ODS-Datei lesen**

Aspose.Cells ermöglicht das Lesen von Diagrammunterschriften in ODS-Dateien durch Verwendung der Eigenschaft [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). Das folgende Beispiel lädt die [Beispiel-ODS-Datei](89620481.ods) und liest die Diagrammunterschrift mit der Eigenschaft [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) und gibt sie im Konsolenfenster aus. Bitte siehe die Konsolenausgabe des unten gegebenen Codes als Referenz.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
