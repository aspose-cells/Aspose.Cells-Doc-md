---
title: Hämta arbetsbladet för diagrammet med Node.js via C++
linktitle: Hämta kalkylbladet för diagrammet
description: Lär dig att hämta det arbetsblad som är kopplat till ett Excel diagram med Aspose.Cells for Node.js via C++. Utforska och manipulera diagrammets underliggande data effektivt.
keywords: Aspose.Cells för Node.js, Excel diagram, arbetsblad, datamanipulation, underliggande data, operationer, Node.js via C++
type: docs
weight: 1000
url: /sv/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du komma åt ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller egenskapen [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

Följande exempel visar hur man använder [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)-egenskapen. Koden skriver först ut namnet på arbetsbladet, sedan hämtar den det första diagrammet på arbetsbladet. Den skriver sedan ut arbetsbladets namn igen, med hjälp av [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)-egenskapen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

Nedan är konsolresultatet som exempelkoden leder till. Som du kan se skriver den ut arbetsbladsnamnet samma namn båda gångerna.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
