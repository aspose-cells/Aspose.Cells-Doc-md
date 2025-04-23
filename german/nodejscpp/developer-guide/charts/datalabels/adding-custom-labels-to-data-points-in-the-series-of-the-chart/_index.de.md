---  
title: Hinzufügen benutzerdefinierter Beschriftungen zu Datenpunkten in der Serie des Diagramms mit Node.js via C++  
linktitle: Hinzufügen benutzerdefinierter Beschriftungen zu Datenpunkten in der Serie des Diagramms  
description: Lernen Sie, wie Sie benutzerdefinierte Beschriftungen zu Datenpunkten in der Serie eines Diagramms mithilfe von Aspose.Cells for Node.js via C++ hinzufügen. Dieser Leitfaden zeigt, wie Sie das Aussehen, die Position und das Format der Beschriftungen anpassen können, während Sie sie mit Ihrer Datenquelle verknüpfen, um eine genaue Darstellung zu gewährleisten.  
keywords: Aspose.Cells für Node.js, Diagramme, benutzerdefinierte Beschriftungen, Datenpunkte, Serien, Aussehen, Position, Formatierung, Datenquelle, Darstellung.  
type: docs  
weight: 100  
url: /de/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Sie können benutzerdefinierte Beschriftungen zu Datenpunkten in der Serie des Diagramms hinzufügen. Aspose.Cells bietet die Eigenschaft [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--), um diese benutzerdefinierten Beschriftungen hinzuzufügen. Dieser Artikel erklärt, wie Sie diese Eigenschaft verwenden, um benutzerdefinierte Beschriftungen zu Datenpunkten in der Serie des Diagramms hinzuzufügen.

{{% /alert %}}  

Der folgende Code erstellt einen **Streudiagramm verbunden durch Linien mit Datenmarkern** und fügt dann **benutzerdefinierte Beschriftungen** zu den **Datenpunkten** in der **Serie** des **Diagramms** hinzu. Jede benutzerdefinierte Beschriftung zeigt den **Seriennamen** und den **Punktnamen** an. Sie können stattdessen jeden anderen Text verwenden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

