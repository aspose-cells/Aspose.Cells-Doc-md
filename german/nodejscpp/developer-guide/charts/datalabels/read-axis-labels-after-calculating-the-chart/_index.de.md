---  
title: Lesen Sie Achsenbeschriftungen nach der Diagrammberechnung mit Node.js über C++  
linktitle: Achsenbeschriftungen nach Berechnen des Diagramms lesen  
description: Erfahren Sie, wie Sie Achsenbeschriftungen in Aspose.Cells for Node.js via C++ nach der Diagrammberechnung lesen. Unser Leitfaden zeigt, wie Sie Achsenbeschriftungen zugreifen und abrufen, einschließlich deren Formatierung und Positionierung.  
keywords: Aspose.Cells für Node.js, Diagramm, Achsenbeschriftungen, Berechnung, Lesen, Zugriff, Abruf, Formatierung, Positionierung, Node.js über C++  
type: docs  
weight: 90  
url: /de/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Mögliche Verwendungsszenarien**

Sie können die Achsenbeschriftungen Ihres Diagramms nach der Berechnung seiner Werte mit der [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--)-Methode lesen. Bitte verwenden Sie die [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--)-Methode für diesen Zweck, die die Achsenbeschriftungen als Liste zurückgibt.

## **Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms**

Siehe bitte den folgenden Beispielcode, der die [Beispieldatei für Excel](ReadAxisLabels.xlsx) lädt und die Kategorienachsenbeschriftungen des Diagramms im ersten Arbeitsblatt liest. Anschließend werden die Werte der Achsenbeschriftungen in der Konsole ausgegeben. Bitte sehen Sie sich die Konsolenausgabe des untenstehenden Beispielcodes als Referenz an.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **Konsolenausgabe**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

