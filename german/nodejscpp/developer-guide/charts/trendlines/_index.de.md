---
title: Equation Text der Trendlinie eines Diagramms mit Node.js über C++ abrufen
description: Erfahren Sie, wie Sie Aspose.Cells for Node.js via C++ verwenden, um den Gleichungstext einer Trendlinie in einem in Microsoft Excel erstellten Diagramm abzurufen. Unser Leitfaden zeigt, wie Sie auf die Gleichung einer Trendlinie zugreifen und sie für weitere Analysen oder Anzeige extrahieren.
keywords: Aspose.Cells for Node.js via C++, Diagramm Trendlinie, Gleichungstext, Microsoft Excel, Datenanalyse, Anzeige.
linktitle: Trendlinien
type: docs
weight: 110
url: /de/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Sie können den Gleichungstext der Trendlinie eines Diagramms mit Aspose.Cells for Node.js via C++ abrufen. Aspose.Cells bietet die [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) Eigenschaft, die den Gleichungstext der Trendlinie zurückgibt. Um diese Eigenschaft zu verwenden, müssen Sie zunächst die [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) Methode aufrufen.

{{% /alert %}}

Das folgende Bildschirmfoto zeigt das Diagramm mit einer Trendlinie, deren Gleichungstext in roter Farbe angezeigt wird. Wir werden diesen Text mit der [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--)-Eigenschaft im folgenden Beispielcode abrufen.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Node.js-Code zum Abrufen des Gleichungstexts der Diagrammtrendlinie

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
