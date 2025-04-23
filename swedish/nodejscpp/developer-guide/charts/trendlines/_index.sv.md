---
title: Hämta ekvationstext för diagramtrendlinje med Node.js via C++
description: Lär dig hur man använder Aspose.Cells for Node.js via C++ för att hämta ekvationstexten för en trendlinje i ett diagram i Microsoft Excel. Vår guide visar hur man får åtkomst och extraherar ekvationen för en trendlinje för vidare analys eller visning.
keywords: Aspose.Cells for Node.js via C++, Diagramtrendlinje, Ekvationstext, Microsoft Excel, Dataanalys, Visning.
linktitle: Trendlinjer
type: docs
weight: 110
url: /sv/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvationstexten för diagramtrendlinje med Aspose.Cells for Node.js via C++. Aspose.Cells ger egenskapen [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) som returnerar ekvationstexten för diagramtrendlinjen. För att använda denna egenskap måste du först anropa [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) metoden.

{{% /alert %}}

Följande skärm visar diagrammet med en trendlinje och dess ekvationstext visas i röd färg. Vi kommer att hämta denna text med hjälp av [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) egenskapen i följande kodexempel.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Node.js kod för att få ekvationstext för diagramtrendlinje

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

## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
