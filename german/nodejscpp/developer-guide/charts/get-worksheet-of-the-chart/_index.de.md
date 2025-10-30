---
title: Abrufen des Arbeitsblatts des Diagramms mit Node.js über C++
linktitle: Arbeitsblatt des Diagramms abrufen
description: Erfahren Sie, wie Sie das mit Excel verbundene Arbeitsblatt eines Diagramms mit Aspose.Cells for Node.js via C++ abrufen. Greifen Sie effizient auf die zugrunde liegenden Daten des Diagramms zu und manipulieren Sie diese.
keywords: Aspose.Cells für Node.js, Excel Diagramme, Arbeitsblätter, Datenmanipulation, zugrunde liegende Daten, Operationen, Node.js über C++
type: docs
weight: 1000
url: /de/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Manchmal möchten Sie auf ein Arbeitsblatt über einen Diagrammverweis zugreifen. Aspose.Cells bietet die [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)-Eigenschaft, die den Verweis auf das Arbeitsblatt zurückgibt, das das Diagramm enthält.

{{% /alert %}}

Das folgende Beispiel zeigt, wie die [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)-Eigenschaft verwendet wird. Der Code gibt zuerst den Namen des Arbeitsblatts aus, greift dann auf das erste Diagramm im Arbeitsblatt zu und gibt den Namen des Arbeitsblatts erneut aus, diesmal mit der [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)-Eigenschaft.

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

Unten ist die Konsolenausgabe, die das Beispiel des Codes ergibt. Wie Sie sehen können, druckt es den Arbeitsblattnamen beide Male gleich aus.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
